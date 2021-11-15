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
// This program either
// (1) adds R0 copies of R1 and puts the result in R2 if R0 < R1, or
// (2) adds R1 copies of R0 and puts the result in R2 if R0 >= R1.
//
// ************************************************************

  // First Make sure R2 = 0
  @R2
  M=0

  // Decide if R0 < R1
  @R0
  D=M
  @R1
  D=D-M // R0-R1
  @R0SMALL
  D;JLT // Jump if R0-R1 < 0

  // Otherwise R1 <= R0
  @R1
  D=M
  @small
  M=D // small = R1
  @R0
  D=M
  @big
  M=D // big = R0
  @LOOP
  0;JMP // Proceed to the LOOP (skip R0SMALL)

(R0SMALL)
  @R0
  D=M
  @small
  M=D // small = R0
  @R1
  D=M
  @big
  M=D // big = R1

(LOOP)
  // Check small value to see if we're done.
  @small
  D=M
  @END
  D;JEQ
  // Add big to R2.
  @big
  D=M
  @R2
  M=M+D
  // Decrement small.
  @small
  M=M-1
  // Return to the top of (LOOP).
  @LOOP
  0;JMP

(END)
  @END
  0;JMP
