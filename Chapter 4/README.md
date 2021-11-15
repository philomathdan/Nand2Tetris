# Chapter 4 Notes and Solutions

### Some Comments
 * For me, the trickiest part of assembly language is keeping track of which registers contain a data value I'm interested in, and which contain an address of a data value I'm interested in.  
 * Perhaps the trickiest register is the A register, since it serves so many uses.  In particular, special attention should be paid to the last paragraph of Section 4.2.3 on avoiding conflicted uses of this register.
* Speaking Section 4.2.3, a good portion of this is dedicated to binary machine code which is not needed for completing the projects in this chapter.  However, this will be needed for the next two chapters.  

### Mult.asm
My program added R0 copies of R1 togher and put the result in R3.  I leave the values R0 and R1 in place, although this isn't required in the problem.  I just didn't like the idea of losing either of the original values.

### Mult_optimized.asm
After completing Mult.asm, I realized it's a terrible algorithm if R0 is big and R1 is small.  So, I wrote a more complicated version that optimizes for this (and so should have a shorter run-time in general).  For this, I labeled the smaller value between R0 and R1 as `small` and the larger value `big`.  I then added `small` copies of `big` together and put the result in R3.  Again, the values R0 and R1 are left unchanged.

### Fill.asm
Here, I kept a register named `loc` that kept the address of where we were in the screen region of memory.  Then everything goes into a loop.  On each iteration I check whether `loc` needs to be reset to `SCREEN`, then check if a key is pressed, then write -1 or 0 to the register `loc` points to, and finally increment `loc`.

When you test this in the CPUEmulator, make sure you select No Animation on the Animate drop-down menu (or else it will run painfully slowly and will probably prompt you to make this switch anyway) and select Screen on the View drop-down menu.
