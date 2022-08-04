#include <assert.h>
#include <stdint.h>
#include <stdio.h>

#ifdef COMBA256X256
 void comba256x256(uint64_t *out, uint64_t *a, uint64_t *b);
 #define comba_mul comba256x256
 #include "comba256x256_test_vectors_sample.c"
#elif defined(COMBA320X320)
 void comba320x320(uint64_t *out, uint64_t *a, uint64_t *b);
 #define comba_mul comba320x320
 #include "comba320x320_test_vectors_sample.c"
#elif defined(COMBA384X384)
 void comba384x384(uint64_t *out, uint64_t *a, uint64_t *b);
 #define comba_mul comba384x384
 #include "comba384x384_test_vectors_sample.c"
#elif defined(COMBA448X448)
 void comba448x448(uint64_t *out, uint64_t *a, uint64_t *b);
 #define comba_mul comba448x448
 #include "comba448x448_test_vectors_sample.c"
#elif defined(COMBA512X512)
 void comba512x512(uint64_t *out, uint64_t *a, uint64_t *b);
 #define comba_mul comba512x512
 #include "comba512x512_test_vectors_sample.c"
#endif

int main() {
    int n_rows = sizeof(a)/sizeof(a[0]);
    int n_cols = sizeof(expc[0])/sizeof(expc[0][0]);

    for (int i = 0; i < n_rows; i++) {
        uint64_t out[n_cols];
        comba_mul(out, a[i], b[i]);
        for (int j = 0; j < n_cols; j++) {
            assert(out[j] == expc[i][j]);
        }
    }

    printf("[PASS] passing all %d testvectors\n", n_rows);

    return 0;
}
