### Nand2Tetris Chapter 1 Notes:

I found it very helpful to read the [HDL survival guide](http://nand2tetris.org/software/HDL%20Survival%20Guide.html) (not included in the text).  Two useful details for this chapter are:
* Each input pin can be fed either of the constants true (1) or false (0).
* Portions of buses can be specified as ranges of indices, such as in[0..2] for the first three pins of in.

My method for solving these was to first work out the logic in terms of previously constructed gates, and then to sketch a diagram to keep track of the internal connections.

Below are my HDL files and my sketches for each gate (though I didn't make sketches for Not16, Or16, And16, or Mux16 since those are just the single bit versions repeated over and over.) In most of the HDL files, I added some comments about my thought process for finding a solution.

Probably your solutions for these relatively simple gates will look a lot like mine, but if you've found better/different ones I'd love to see them.
