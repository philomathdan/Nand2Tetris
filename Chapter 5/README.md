### Nand2Tetris Chapter 5 Notes:

Here are my solutions and sketches for the Chapter 5 projects.  This was the most challenging chapter so far, especially the CPU chip, which took me several tries to get right.  This time, rather than commenting within each HDL file, I'll post all my comments for these projects here.

**Memory:**

This is very similar to the RAM chips from Chapter 3, except the pieces are of mixed sizes and the Keyboard register is read only.  Because of the latter point, Keyboard requires no load bit.  However, I still used a DMux chip to determine if load is sent to Screen, even though this leaves one pin on that DMux gate unused.  An alternative would be to send (load2 And (Not address[13])) to the load pin for screen, where load2 is the wire coming from the first DMux gate.  However, this approach would use more chips.

Also, I made no attempt to check whether this chip is being sent addresses above 24576.  In fact, in my design any address above 24575 could be used to read from Keyboard.  This seems like a bad design, but the project description didn't give clear instructions on 
how to handle this situation (saying only "access to any address > 24576 is invalid"). And so I decided to keep my design as simple as possible while still (hopefully) meeting the project requirements.  

**CPU:**

Here, I followed the general layout given in Figure 5.9 on p. 94 of the text, and most of details of my solution can be found in my sketch  above.  Some things to note however:
* I split off wires labeled a, c1, c2, c3, c4, c5, c6, d1, d2, d3, j1, j2, and j3 from the instruction, but made sure that they had value 0 if the MSB of the instruction was 0, i.e. if the instruction was just a memory address for the A register.  I'm not sure if this is necessary, but it seemed much safer.  
* By generous design of the authors, the computation bits c1, c2, c3, c4, c5, and c6 match up exactly with the ALU control bits zx, nx, zy, ny, f, and no.
* Dealing with the jump bits and the PC was tricky.  I first created another 1 bit output from the ALU:  pos = Not(zr Or ng) and fed the load pin of PC with (j1 And ng) Or (j2 And zr) Or (j3 And pos).  Also, I set the inc pin to be triggered by default with Not(load Or reset).  
* Finally, note that the A register and PC chip have 16-bit wide outgoing buses, but memory addresses require just 15 bits.  So, you have
to select the first 15 bits from those when sending them to RAM chips.

**Computer:**

Here, I followed the layout given in Figure 5.10 on p. 97 of the text, with essentially no changes.  I even labeled the connecting wires as they did, even though this results in potentially confusing commands in the HDL file, such as reset = reset, outM = outM, etc.  
