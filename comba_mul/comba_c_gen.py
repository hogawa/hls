from typing import List


def comba_c_gen(varlist_a: List, varlist_b: List, varlist_out: List):
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
    exp_buffer += ("\t" + varlist_out[1] + " = L(acc1);\n")
    exp_buffer += ("\n")
    for i in range(2, len(varlist_out)):
        exp_buffer += ("\tsum = HIGH64(acc" + str(i - 1) + ") + LOW64(acc" + str(i) + ") + carry;\n")
        exp_buffer += ("\t" + varlist_out[i] + " = LOW64(sum);\n")
        if i < len(varlist_out) - 1:
            exp_buffer += ("\tcarry = HIGH64(sum);\n")
            exp_buffer += ("\n")

    return exp_buffer


if __name__ == "__main__":
    mode = "standalone"
    func_name = "comba256x256"
    vlist_a = ["a[0]", "a[1]", "a[2]", "a[3]"]
    vlist_b = ["b[0]", "b[1]", "b[2]", "b[3]"]
    vlist_out = ["out0", "out1", "out2", "out3", "out4", "out5", "out6", "out7"]

    if mode == "standalone":
        print("#include <stdint.h>")
        print("")
        print("#define CMB_MULL(X,Y) (X * Y)")
        print("#define CMB_MULH(X,Y) (((__uint128_t)X * Y) >> 64)")
        print("")
        print("void " + func_name + "(uint64_t *out, uint64_t *a, uint64_t *b) {")
    
    print(comba_c_gen(vlist_a, vlist_b, vlist_out), end='')
    
    if mode == "standalone":
        print("}")
