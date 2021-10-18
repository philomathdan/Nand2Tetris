# Chapter 1 Notes and Solutions

## Prerequisites
I recommend gaining some familiarity with truth tables and basic logic operators _before_ starting this chapter.  In particular, I found it very helpful to know DeMorgan's Laws and how to translate a conditional statement (if-then) into an Or statement.  If you're unfamiliar with things like this, I highly recommend reading through Sections 1.1-1.3 in [this text](https://www.whitman.edu/mathematics/higher_math_online/chapter01.html).  (The rest of that text is very nice reading too.)

## HDL
There were a few aspects of the hardware description language I needed to be reminded of:
- The basic format of a part listing looks like `PartName(a = pin1, b = pin2, ..., out = pin3)`.  Here, the a, b, and out are names of pins in the gate PartName.  These are specified by the gate's API and can't be changed.  However, the pin1, pin2, and pin3 can be decided by you.  These may refer to the external pins of the gate being designed, or they could refer to an internal connection in your design.  In the latter case, you're free to name them as you wish.
- Each pin has infinite fan-out.  That is, it's value can be sent out to any number of other pins.
- To assign the value 0 to a pin (or bus), set it to `false` and likewise, to assign the value 1 to a pin (or bus), set it to `true`.

## Solutions
In designing these gates, I would start with one or both of the following.  For some, I would say in English what the gate's functionality meant to me.  For example, "Xor(a,b) means a or b but not both."  For others, I might similarly describe in English the outcome of that gate's truth table.  For example, "Not(in) is 0 if in is 1, and is 1 otherwise."  I could then translate this verbal description into some sort of logical formula, and then use things like DeMorgan's Laws or other logical equivalences to try to write the formula in terms of gates I'd already found.  Finally, I would draw a diagram of the gate according to my final formula.  This made it much easier for me to write down the correct HDL code, keep track of internal pins, etc.  

My completed HDL files are above, along with a sketched diagram for each gate.  Below are my thoughts in approaching each gate.  If you have found a different solution for any of these, I would love to learn about it!

### Not
Nand(a,b) is 0 if a and b are both 0, and is 1 otherwise.  Likewise Not(in) is 0 if in is 0, and is 1 otherwise.  By this comparison we can see that Not(in) is equivalent to Nand(in,in).  (Note that Nand(in, 1) and Nand(1,in) also work.)

### And
This one didn't take too much thinking, given that we already have Nand and Not:  And(a,b) is equivalent to Not(Nand(a,b)).

### Or
Here, it's a huge help to know DeMorgan's Laws:  Or(a,b) is equivalent to Not(Not(Or(a,b))), and Not(Or(a,b)) is equivalent to And(Not(a),Not(b)) by DeMorgan's Laws.  Thus, altogether we can conclude Or(a,b) is equivalent to Nand(Not(a),Not(b)).

### Xor
As noted above, Xor(a,b) means "a or b but not both."  That is, we want Or(a,b) And Nand(a,b).   In other words, we want And(Or(a,b),Nand(a,b)).

(Side-note:  Xor(a,b) is 1 if a != b and 0 otherwise.  So, Xor tests for inequality.)

### Mux
Here, the functionality is: "If sel, then b, and if not sel, then a."  Since the conditional "if X then Y" is equivalent to "(not X) or Y," we can write Mux(a,b) as And(Or(Not(sel),b),Or(sel,a)).

**Edit**:  My friend Dave came up with a formula that looks almost opposite to mine, but turns out to be logically equivalent:  
Or(And(b,sel),And(a,Not(sel))).

### DMux
Here, we have two separate outputs, a and b, each of which takes on either of two values depending on the value of sel.  But this is simply the functionality of a Mux gate, one for output a and one for output b.  In other words, a is given by Mux(in,0,sel) and b is given by Mux(0,in,sel).

**Edit**:  My friend Dave came up with the more elegant solution a = And(in,Not(sel)), b = And(in,sel).

### Not16, Or16, And16, Mux16
These are simply parallel versions of the 1-bit gates already constructed, one for each bit in the gate.  They're hardly worth sketching separate diagrams for, but I did so anyway, for completeness I guess. :-) 

### Or8Way
This is just a string of 7 Or operators which, because Or is commutative and associative, can be evaluated in any chronological order.  I wrote mine with the inner-most parentheses on the left, and worked from left to right:  (...(((in[0] Or in[1]) Or in[2]) Or in[3])...)Or in[7].  You can, of course, arrange your parentheses differently, e.g. making a symmetric tree for the gate diagram.  But, this will use the same number of Or gates. 

### Mux4Way16
Here, we can select between a and b with a Mux16 gate and sel[0], and likewise for selecting between c and d.  Finally, we can select between these two resulting branches with a Mux16 gate and sel[1].  

### Mux8Way16
This is almost the same thing as Mux4Way16, but the initial Mux16 gates must be Mux4Way16 gates and we select on each of them using sel[0..1].  (The subsequent Mux16 gate is then selected with sel[2].)

### DMux4Way
This is the dual of Mux4Way, but for 1 bit.  We can select between sending the input to the a/b branch or the c/d branch using a DMux gate and sel[1].  Subsequently, we can decide between sending the input to a or b using another DMux gate and sel[0], and likewise for sending the input to c or d.  Note that sel[0] will select for both the a/b branch and the c/d branch no matter what, but the branch that is not chosen by sel[1] will only receive and 0 as its input, so the value of sel[0] won't change anything on that branch.  

### DMux8Way
This is almost the same thing as DMux4Way, except that the subsequent DMux gates are replaced with DMux4Way gates and we select on each using sel[0..1].  (Selection on the initial gate is done with sel[2].)
