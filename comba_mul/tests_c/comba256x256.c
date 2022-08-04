/**
 * Auto-generated with comba_c_gen.py
 */
#include <stdint.h>

#define CMB_MULL(X,Y) (__uint128_t)(X * Y)
#define CMB_MULH(X,Y) (((__uint128_t)X * (__uint128_t)Y) >> 64)
#define CMB_L64(X)    (X & 0xFFFFFFFFFFFFFFFF)
#define CMB_H64(X)    (X >> 64)

void comba256x256(uint64_t *out, uint64_t *a, uint64_t *b) {
	__uint128_t acc0 = CMB_MULL(a[0], b[0]);
	__uint128_t acc1 = CMB_MULL(a[1], b[0]) + CMB_MULL(a[0], b[1]) + CMB_MULH(a[0], b[0]);
	__uint128_t acc2 = CMB_MULL(a[2], b[0]) + CMB_MULL(a[1], b[1]) + CMB_MULL(a[0], b[2]) + CMB_MULH(a[1], b[0]) + CMB_MULH(a[0], b[1]);
	__uint128_t acc3 = CMB_MULL(a[3], b[0]) + CMB_MULL(a[2], b[1]) + CMB_MULL(a[1], b[2]) + CMB_MULL(a[0], b[3]) + CMB_MULH(a[2], b[0]) + CMB_MULH(a[1], b[1]) + CMB_MULH(a[0], b[2]);
	__uint128_t acc4 = CMB_MULL(a[3], b[1]) + CMB_MULL(a[2], b[2]) + CMB_MULL(a[1], b[3]) + CMB_MULH(a[3], b[0]) + CMB_MULH(a[2], b[1]) + CMB_MULH(a[1], b[2]) + CMB_MULH(a[0], b[3]);
	__uint128_t acc5 = CMB_MULL(a[3], b[2]) + CMB_MULL(a[2], b[3]) + CMB_MULH(a[3], b[1]) + CMB_MULH(a[2], b[2]) + CMB_MULH(a[1], b[3]);
	__uint128_t acc6 = CMB_MULL(a[3], b[3]) + CMB_MULH(a[3], b[2]) + CMB_MULH(a[2], b[3]);
	__uint128_t acc7 = CMB_MULH(a[3], b[3]);

	// Final carry propagation
	uint8_t carry = 0;
	__uint128_t sum = 0;

	out[0] = acc0;
	out[1] = CMB_L64(acc1);

	sum = CMB_H64(acc1) + CMB_L64(acc2) + carry;
	out[2] = CMB_L64(sum);
	carry = CMB_H64(sum);

	sum = CMB_H64(acc2) + CMB_L64(acc3) + carry;
	out[3] = CMB_L64(sum);
	carry = CMB_H64(sum);

	sum = CMB_H64(acc3) + CMB_L64(acc4) + carry;
	out[4] = CMB_L64(sum);
	carry = CMB_H64(sum);

	sum = CMB_H64(acc4) + CMB_L64(acc5) + carry;
	out[5] = CMB_L64(sum);
	carry = CMB_H64(sum);

	sum = CMB_H64(acc5) + CMB_L64(acc6) + carry;
	out[6] = CMB_L64(sum);
	carry = CMB_H64(sum);

	sum = CMB_H64(acc6) + CMB_L64(acc7) + carry;
	out[7] = CMB_L64(sum);
}
