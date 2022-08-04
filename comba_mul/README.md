# Comba multiplication algorithm

## General ideas:

- Delay carry computations (carry delay)
- Requires 2N-bit accumulators when implementing with N-bit words

## Description:

First stage: generation and accumulation of low-limb products:
```
                                     a3      a2      a1      a0
x                                    b3      b2      b1      b0
---------------------------------------------------------------
                                L(a3b0) L(a2b0) L(a1b0) L(a0b0)
                        L(a3b1) L(a2b1) L(a1b1) L(a0b1)
                L(a3b2) L(a2b2) L(a1b2) L(a0b2)
        L(a3b3) L(a2b3) L(a1b3) L(a0b3)
---------------------------------------------------------------
           acc6    acc5    acc4    acc3    acc2    acc1    acc0
```

Second stage: generation and accumulation of high-limb products:
```
                                     a3      a2      a1      a0
x                                    b3      b2      b1      b0
---------------------------------------------------------------
                        H(a3b0) H(a2b0) H(a1b0) H(a0b0)
                H(a3b1) H(a2b1) H(a1b1) H(a0b1)
        H(a3b2) H(a2b2) H(a1b2) H(a0b2)
H(a3b3) H(a2b3) H(a1b3) H(a0b3)
---------------------------------------------------------------
   acc7    acc6    acc5    acc4    acc3    acc2    acc1
```

Third stage: final carry propagation
```
out[0]    <- acc0
out[1]    <- L(acc1)
c, out[2] <- H(acc1) + L(acc2)
c, out[3] <- H(acc2) + L(acc3) + c
c, out[4] <- H(acc3) + L(acc4) + c
c, out[5] <- H(acc4) + L(acc5) + c
c, out[6] <- H(acc5) + L(acc6) + c
out[7]    <- H(acc6) + acc7 + c
```

## Usage:

To generate the 256x256->512-bit multiplier. The list of input and output variables must be passed as a string separated by commas and without spaces:
```
$ python3 comba_c_gen.py standalone comba256x256 a[0],a[1],a[2],a[3] b[0],b[1],b[2],b[3] out[0],out[1],out[2],out[3],out[4],out[5],out[6],out[7]
```
