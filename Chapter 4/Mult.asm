// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// ************************************************************
//
// This program adds R0 copies of R1 and puts the result in R2
//
// ************************************************************

  // First store the value R0 into a variable called counter.
  // This way we don't destroy the value R0 by decrementing it.
  @R0
  D=M
  @counter
  M=D

  // Now make sure R2 is 0 to start with.
  @R2
  M=0

(LOOP)
  // Check counter value to see if we're done.
  @counter
  D=M
  @END
  D;JEQ
  // Add R1 to R2.
  @R1
  D=M
  @R2
  M=M+D
  // Decrement counter.
  @counter
  M=M-1
  // Return to the top of (LOOP).
  @LOOP
  0;JMP

(END)
  @END
  0;JMP
