# Chapter 2 Notes and Solutions

Above are my solutions and gate diagrams.  Here are some brief thoughts on each gate.

### HalfAdd
Just looking at the truth tables for this gate, it's clear that sum can be given by Xor, and carry can be given by And.  

### FullAdd
For the sum, we can take the sum portion of two half adders:  sum(sum(a,b),c).  To combine the two resulting carry bits, note that these can never both be 1.  Thus, it's ok to combine these with just an Or gate.  

### Add16
Here, I just added as usual, right to left, inputting each carry bit into the next addition column.  The final carry bit is ignored, per our instructions.

### Inc16
Initially I just re-used Add16, but with 1 as one of the inputs.  But eventually I noticed that we can be more efficient by using only HalfAdders throughout, as each output bit is only computed with two input bits.

### ALU
This is mostly a sequence of Mux16 gates, keeping the order of evaluation as described by the authors.  To evaluate zr, I used DeMorgan's law to evaluate Not(out[0] Or out[1] Or ... Or out[15]).  For ng, we can use the fact that negative numbers have a most significant bit value of 1.
