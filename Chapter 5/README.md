# Chapter 5 Notes and Solutions

### Memory

As with previous memory chips, the most significant bits are used to determine which sub-chip to access, and the remaining bits are sent as an address to that sub-chip.  In particular, since Screen starts at address 2<sup>14</sup> and Keyboard is at address 2<sup>14</sup>+2<sup>13</sup>,
  * if address[14] = 0, then RAM16K is accessed using address[0..13], 
  * if address[14] = 1 but address[13] = 0, then Screen is accessed using address[0..12], and
  * Keyboard is accessed with address = 110000000000000.
  
In the specifications for this chip, addresses beyond the Keyboard register are said to be "invalid."  However, no direction is given for how to handle invalid addresses, though presumably only valid addresses will be supplied by the assembler.  In any case, I decied to design two versions:
  * Memory.hdl assumes only valid addresses are sent and makes no provisions for invalid ones.
  * Memory_Safe.hdl deals with invalid addresses by not allowing any register to be written to and setting out to the value 0.

For Memory_Safe.hdl, I created a bit labeled validaddr and only allowed loads if this held the value 1.  For out though, something has to be set there no matter what.
Originally I set out to -1 for invalid addresses, thinking this looked like more of an error flag value.  However, I discovered that Memory.tst _does_ send an invalid address with load = 0 and expects out to be 0 in this case.  Thus, I changed the behavior of Memory_Safe.hdl accordingly.  

But all this made me wonder what Memory.hdl was doing for invalid addresses, since evidently it passed the same test.  Tracing things through, I saw that out will hold the value of Keyboard in this case (which will be 0 if no key is pressed).  But far worse, if load = 1 for an invalid address, RAM16K will be over-writen at address[0..14].  Thus, Memory_Safe.hdl seems much better, at the cost of a few extra gates.  

### CPU

Much of the design work for CPU.hdl (maybe too much) is done for us in Figure 5.8 of the text.  Handling A-instructions is fairly easy, as we just need to make sure that a value of 0 in instruction[15] loads the value of instruction into the A register.  In contrast, C-instructions are involved in essentially all the parts of the CPU.  To keep track of individual instruction bits, I labeled C-instructions as follows:

1 1 1 a c<sub>1</sub> c<sub>2</sub> c<sub>3</sub> c<sub>4</sub> c<sub>5</sub> c<sub>6</sub> d<sub>1</sub> d<sub>2</sub> d<sub>3</sub> j<sub>1</sub> j<sub>2</sub> j<sub>3</sub>

To make sure I was only dealing with bits from C-instructions, I defined each of these as a = And(instruction[15],instruction[12]) and so forth.  For things like the compution portion, this probably wasn't necessary, but for the destination and jump portion, it really matters.  I wouldn't want an A-instruction loading registers or changing the value of PC after all.  With this safety provision, much of the wiring is pretty straight forward.  The c values go directly to the ALU, for example, and the d values load the A-register and D-register and write to memory.   The j values, along with zr and ng from the ALU, can be used to determine whether the PC should load a new address using the following logic:

pcload = (j<sub>1</sub> And ng) Or (j<sub>2</sub> And zr) Or (j<sub>3</sub> And Not(ng or zr)) 

Regarding the PC chip, we apparently always want inc set to 1, which makes me wonder why this control bit was ever added to the PC chip.  I realize it makes it applicable for more general use, but we never take advantage of that.  So, what's the point?  

Finally, the outputs addressM and pc only expect 15 bit addresses, so the outputs of the A-register and PC must be truncated accordingly.

### Computer

The design for this was given to us in Figure 5.9 of the text, and there's not much left to figure out.  I found it a bit disappointing that they didn't leave more of this up to us.  Unlike the CPU, Computer isn't very complicated, and we should be able to put it together without this much assistance.  In any case, I didn't uplad a picture for this, as my picture wouldn't differ much from the one provided in the text.
