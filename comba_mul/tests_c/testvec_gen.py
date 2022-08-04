import math
import random
import sys


def bigint_u64_vec(x: int) -> str:
    """Generates a string of a C-like array representation with 64-bit elements from a big integer

    :param x: the big integer input
    :return: the C-like array print
    """
    str_ret = ""
    n_bits = x.bit_length()
    n_limbs = int(math.ceil(n_bits / 64))
    str_ret += ("{ ")
    for i in range(n_limbs):
        y = x & 0xFFFFFFFFFFFFFFFF
        str_ret += (hex(y))
        if i < n_limbs - 1:
            str_ret += (", ")
        x = x >> 64
    str_ret += (" }")
    return str_ret


def gen_testvec_u64(n_bits: int):
    """ Generates a ternary corresponding to a test case: 1st multiplicand, 2nd multiplicand, output

    :param b_bits: number of bits from the multiplicands
    """
    a = random.randint(0, (1 << n_bits) - 1)
    b = random.randint(0, (1 << n_bits) - 1)
    exp = a * b
    return a, b, exp


if __name__ == "__main__":
    n_tests = int(sys.argv[1])
    n_bits = int(sys.argv[2])

    a_buf, b_buf, exp_buf = [], [], []
    for i in range(n_tests):
        a_val, b_val, exp_val = gen_testvec_u64(n_bits)
        a_buf.append(bigint_u64_vec(a_val))
        b_buf.append(bigint_u64_vec(b_val))
        exp_buf.append(bigint_u64_vec(exp_val))
    
    print("/**")
    print(" * Auto-generated with testvec_gen.py")
    print(" */")

    print("uint64_t a[" + str(n_tests) + "][" + str(int(n_bits / 64)) + "] = {")
    for i in range(n_tests):
        print("\t" + a_buf[i], end='')
        if i < n_tests - 1:
            print(",")
    print("\n};\n")

    print("uint64_t b[" + str(n_tests) + "][" + str(int(n_bits / 64)) + "] = {")
    for i in range(n_tests):
        print("\t" + b_buf[i], end='')
        if i < n_tests - 1:
            print(",")
    print("\n};\n")

    print("uint64_t expc[" + str(n_tests) + "][" + str(2 * int(n_bits / 64)) + "] = {")
    for i in range(n_tests):
        print("\t" + exp_buf[i], end='')
        if i < n_tests - 1:
            print(",")
    print("\n};\n")
