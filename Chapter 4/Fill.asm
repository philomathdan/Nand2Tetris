// This program relies on the fact that the address alotted to KBD occurs
// directly after the memory alotted to the screen.  If this were not the
// case we would have to change line 13 to be to be the address of whatever
// register directly follows the screen memory.

  @SCREEN
  D = A       //  Load address of start of screen into D.
  @loc        //  Set aside a register named loc (location in screen memory).
  M = D       //  Initialize the variable loc at start of screen memory.
(LOOP)
  @loc
  D = M       //  Load current loc value into D.
  @KBD
  D = A - D   //  Load KBD address (end of screen) - loc into D.
  @RESET
  D;JEQ       //  If loc == KBD address, jump to RESET.
  @KBD
  D = M       //  Load KBD value in D.
  @BLACK
  D;JGT       //  If KBD value > 0, jump to BLACK.
  @loc
  D = M       //  Load current loc value into D.
  A = D       //  Load loc as address value into A.
  M = 0       //  Set Memory[loc] = 0 (white).
  @ENDLOOP
  0;JMP       //  Jump to ENDLOOP.
(BLACK)
  @loc
  D = M       //  Load current loc value into D.
  A = D       //  Load loc as address value into A.
  M = -1      //  Set Memory[loc] = -1 (black).
(ENDLOOP)
  @loc
  M = M + 1   //  loc += 1
  @LOOP
  0;JMP       //  Jump to LOOP.
(RESET)
  @SCREEN
  D = A       //  Load address of start of screen into D.
  @loc
  M = D       //  Set loc value to start of screen location.
  @LOOP
  0;JMP       //  Jump to LOOP.
