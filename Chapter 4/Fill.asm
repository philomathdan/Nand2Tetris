// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// ************************************************************
// loc is a variable holding the address of where we are on the screen.
// This changes locs value to the start of the screen.
(RESETLOC) 
@SCREEN
D=A
@loc
M=D

(LOOP)
// First check if loc needs to be reset.
@8192 // 256 rows * 32 words/row = # of 16 bit words in screen
D=A
@SCREEN
D=D+A // First word outside screen.
@loc
D=D-M
@RESETLOC
D;JEQ // Jump if loc points to first word outside screen.
// Now check if any key is pressed.
@KBD
D=M
@FILLBLACK
D;JGT // Jump to FILLBLACK if any key is pressed.
// Otherwise fill in white.
@loc
A=M
M=0
@MOVELOC
0;JMP // Skip FILLBLACK and increment loc
(FILLBLACK)
@loc
A=M
M=-1
(MOVELOC)
@loc
M=M+1
@LOOP
0;JMP
