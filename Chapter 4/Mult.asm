  @2
  M = 0       // Set R2 = 0.
  @0
  D = M       // Load R0 into D.
  @count      // Set aside a register named count.
  M = D       // Load D (R0) in count.
(LOOP)
  @count
  D = M       // Load count into D.
  @END
  D;JLE       // If count <= 0, jump to END
  @count
  D = M       // Load count into D.
  @2
  M = M + D   // R2 += count
  @count
  M = M - 1   // count -= 1
  @LOOP
  0;JMP       // Jump to LOOP.
(END)
  @END
  0;JMP       // Infinite loop to stay at END
