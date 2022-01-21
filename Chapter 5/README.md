# Chapter 5 Notes and Solutions

### Memory

As with previous memory chips, the most significant bits are used to determine which sub-chip to access, and the remaining bits are sent as an address to that sub-chip.  In particular, since `Screen` starts at address 2<sup>14</sup> and `Keyboard` is at address 2<sup>14</sup>+2<sup>13</sup>,
  * if `address[14] = 0`, then `RAM16K` is accessed using `address[0..13]`, 
  * if `address[14] = 1` but `address[13] = 0`, then `Screen` is accessed using `address[0..12]`, and
  * `Keyboard` is accessed with `address = 110000000000000`.
  
In the specifications for this chip, addresses beyond the `Keyboard` register are "invalid."  However, no direction is given for how to handle invalid addresses, though presumably only valid addresses will be supplied by the assembler.  In any case, I decied to design two versions:
  * `Memory.hdl` assumes only valid addresses are sent and makes no provisions for invalid ones.
  * `Memory_Safe.hdl` deals with invalid addresses by not allowing any register to be written to, and setting `out` to the value 0.

For `Memory_Safe.hdl`, I created a bit labeled `validaddr` and only allowed loads if this held the value 1.  For `out` though, something has to be set there no matter what.
Originally I set `out` to -1 for invalid addresses, thinking this looked like more of an error flag value.  However, I discovered that `Memory.tst` _does_ send an invalid address with `load = 0` and expects `out` to be 0 in this case.  Thus, I changed the behavior of `Memory_Safe.hdl` accordingly.  

But this made me wonder what `Memory.hdl` was doing for invalid addresses, since evidently it passed the same test.  Tracing things through, I saw that `out` will hold the value of `Keyboard` in this case (which will be 0 if no key is pressed).  But far worse, if `load = 1` for an invalid address, `RAM16K` will be over-writen at `address[0..14]`.  Thus, `Memory_Safe.hdl` seems much better, at the cost of a few extra gates.  
