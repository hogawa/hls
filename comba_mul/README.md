# Comba multiplication algorithm

## Principles:

- Delay carry computations (carry delay)
- Requires 2N-bit accumulators when implementing with N-bit words

## Description:

First stage: generation and accumulation of low-limb products:
```
                      a3   a2   a1   a0
x                     b3   b2   b1   b0
---------------------------------------
                    a3b0 a2b0 a1b0 a0b0
               a3b1 a2b1 a1b1 a0b1
          a3b2 a2b2 a1b2 a0b2
     a3b3 a2b3 a1b3 a0b3
---------------------------------------
acc7 acc6 acc5 acc4 acc3 acc2 acc1 acc0
```

Second stage: generation and accumulation of high-limb products:
```
                      a3   a2   a1   a0
x                     b3   b2   b1   b0
---------------------------------------
               a3b0 a2b0 a1b0 a0b0
          a3b1 a2b1 a1b1 a0b1
     a3b2 a2b2 a1b2 a0b2
a3b3 a2b3 a1b3 a0b3
---------------------------------------
acc7 acc6 acc5 acc4 acc3 acc2 acc1 acc0
```

Third stage: final carry propagation
