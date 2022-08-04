#include <assert.h>
#include <stdint.h>
#include <stdio.h>

// Comba multiplication generated with comba_c_gen.py
void comba256x256(uint64_t *out, uint64_t *a, uint64_t *b);

// Test vectors generated with testvec_gen.py
#include "comba256x256_test_vectors.c"

int main() {
    int n_rows = sizeof(a)/sizeof(a[0]);
    int n_cols = sizeof(expc[0])/sizeof(expc[0][0]);

    for (int i = 0; i < n_rows; i++) {
        uint64_t out[n_cols];
        comba256x256(out, a[i], b[i]);
        for (int j = 0; j < n_cols; j++) {
            assert(out[j] == expc[i][j]);
        }
    }

    printf("[PASS] passing all %d testvectors\n", n_rows);

    return 0;
}
