### Nand2Tetris Chapter 4 Notes:

Since this isn't the only chapter covering the Hack assembly language, it left me with some questions on a few details.  So, it was a big help to read this [Introduction to Hack Assembly Language](http://www.marksmath.com/tecs/hack-asm/hack-asm.html).  However, I'm still
unclear on using the symbols R0, ... , R15, and I was unable to find an example of that.  These don't seem to be necessary though, since I can refer to those registers directly.
***
**Update:** The use of R0, ... , R15 became clearer to me while reading Chapter 6.  As an example, to load the A register with the address of the first register in Memory, we can use @R0.  This is exactly equivalent to @0, and the included assembler and CPU emulator will automatically translate to the latter.  I'm still not sure _why_ one would use @R0 instead of simply @0 though.  
***
Writing programs in the Hack assemply language was difficult but also enlightening, as it made me think about control flow differently.  It felt like I was working down "close to the metal."  It's dark and warm down there, and quiet too, save for the soft clinking of 0s and 1s. ;-)

**Multiplication Program (Mult.asm):**

Here, I multiplied the two quantities using repeated addition.  Specifically, to calculate R0*R1 I summed R0 copies of R1.  Since I didn't want to destroy R0 by decrementing it, I first copied the value to another register.  This isn't part of the problem specification, but just a personal preference.  Here is a Python version of the program:
```python
R2 = 0
count = R0
while count > 0:
    R2 += count
    count += 1
```
My assembly program looks much like the example in the text for adding the digits 1 through 100, 
and I provided similar comments within my asm file.  

**I/O-Handling Program (Fill.asm):**

This one took me a long time to figure out, and I'm still not fully satisfied with the result.  Recall that SCREEN refers to the address of the first register in screen memory and KBD refers to address of the register holding keyboard input.  Also, KBD occurs immediately after the screen memory, and so it can do double duty as a measure for when we've run past screen memory.  My program uses this fact, which means it will break if screen memory size changes.  I considered using another label for the first register after screen memory, but thought that might make my program more difficult to read.  So, I left this as a comment at the top of my asm file.  As above, the Python version of this program is pretty simple:
```python
loc = SCREEN  #loc represents location in memory
while True:
    if loc == KBD:
        loc = SCREEN
    if Memory[KBD] == 0:
        Memory[loc] = 0 #white
    else:
        Memory[loc] = -1 #black
    loc += 1
```
The main difficulty for me in writing the assembly version of this was that the only thing we have to control flow is a conditional jump, and this program requires several.  I'm sure there are shorter versions than mine, but I tried to keep mine simple to understand.  If someone has a significantly different approach, I'd love to see it.
