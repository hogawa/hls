from typing import List
import sys


def comba_c_gen(varlist_a: List, varlist_b: List, varlist_out: List) -> str:
    """Prints a C code of multi-precision multiplication using 64-bit words

    :param varlist_a: list of variables representing the first multiplicand (from least to most significant)
    :param varlist_b: list of variables representing the second multiplicand (from least to most significant)
    :param varlist_out: list of variables representing the output (from least to most significant)
    :return: C code snippet of the Comba multiplication process
    """
    # For now, we are considering inputs with same number of limbs
    assert(len(varlist_a) == len(varlist_b))
    assert(len(varlist_out) == 2 * len(varlist_a))
    assert(len(varlist_out) == 2 * len(varlist_b))

    # Number of limbs in inputs
    n = len(varlist_a)

    # Create dict for accumulator representation
    accms = {}
    for i in range(2*n):
        accms["acc" + str(i)] = []

    # First stage: generation and accumulation of low-limb products
    for i in range(n):
        for j in range(n):
            key = "acc" + str(i + j)
            accms[key].append("CMB_MULL(" + varlist_a[j] + ', ' + varlist_b[i] + ")")

    # Second stage: generation and accumulation of high-limb products
    for i in range(n):
        for j in range(n):
            key = "acc" + str(i + j + 1)
            accms[key].append("CMB_MULH(" + varlist_a[j] + ', ' + varlist_b[i] + ")")

    # Export to C
    exp_buffer = ""

    for acc in accms:
        exp_buffer += ("\t__uint128_t " + acc + " = ")
        n_elem = len(accms[acc])
        for i in range(n_elem):
            exp_buffer += (accms[acc][i])
            if i < n_elem - 1:
                exp_buffer += (" + ")
            else:
                exp_buffer += (";\n")

    exp_buffer += ("\n")
    exp_buffer += ("\t// Final carry propagation\n")
    exp_buffer += ("\tuint8_t carry = 0;\n")
    exp_buffer += ("\t__uint128_t sum = 0;\n")
    exp_buffer += ("\n")
    exp_buffer += ("\t" + varlist_out[0] + " = acc0;\n")
    exp_buffer += ("\t" + varlist_out[1] + " = CMB_L64(acc1);\n")
    exp_buffer += ("\n")
    for i in range(2, len(varlist_out)):
        exp_buffer += ("\tsum = CMB_H64(acc" + str(i - 1) + ") + CMB_L64(acc" + str(i) + ") + carry;\n")
        exp_buffer += ("\t" + varlist_out[i] + " = CMB_L64(sum);\n")
        if i < len(varlist_out) - 1:
            exp_buffer += ("\tcarry = CMB_H64(sum);\n")
            exp_buffer += ("\n")

    return exp_buffer


if __name__ == "__main__":
    """
    TODO: improve argument passing - maybe use argparse?
    """
    mode = sys.argv[1]
    func_name = sys.argv[2]
    vlist_a = sys.argv[3].split(",")
    vlist_b = sys.argv[4].split(",")
    vlist_out = sys.argv[5].split(",")

    if mode == "standalone":
        print("#include <stdint.h>")
        print("")
        print("#define CMB_MULL(X,Y) (__uint128_t)(X * Y)")
        print("#define CMB_MULH(X,Y) (((__uint128_t)X * (__uint128_t)Y) >> 64)")
        print("#define CMB_L64(X)    (X & 0xFFFFFFFFFFFFFFFF)")
        print("#define CMB_H64(X)    (X >> 64)")
        print("")
        print("void " + func_name + "(uint64_t *out, uint64_t *a, uint64_t *b) {")
    
    print(comba_c_gen(vlist_a, vlist_b, vlist_out), end='')
    
    if mode == "standalone":
        print("}")
