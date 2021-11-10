# Chapter 3 Notes and Solutions

### Bit
The functionality of Bit is almost the same as Mux, but with an added time delay.  So, connecting a Mux gate and a DFF gate makes sense.  I was somewhat disappointed when the authors just gave away this answer in the text.

### Register
This is simply 8 bits in parallel.

### RAM
All of the RAM chips have the same structure.  For RAM8, we can send in to 8 Registers.  The trick then is in using the address to load the right Register and send the right Register to out.  The former is done with a DMux8Way and the latter is done with a Mux8Way16.  For the larger RAM chips, we just replace the Registers with successively larger RAM chips, making sure to sub-bus the high bits of the address for the DMux and Mux gates and the low bits of the address for those component RAM chips.  

### PC
if-then-else statements can be handled with Mux gates, and a sequence of if-then-elses is just a sequence of Mux gates.  However, the order is reversed.  E.g. the default case is the first option in the first Mux gate.  Finally, a Register is added just to cause the necessary time delay.
