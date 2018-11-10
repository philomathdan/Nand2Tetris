### Nand2Tetris Chapter 7 Notes:

This chapter took me a very long time to work through.  I even had to read it twice before starting the project.  Perhaps this was due in part to the fact that a lot of this chapter is devoted to discussing virtual machines in general and covering material not strictly needed until the next chapter.  For this chapter's project though, the most relevant material appears to be contained in Section 7.2.2, Figure 7.5, and pages 142-143.  After starting on the project, a particular point of confusion for me was where in memory things like the segments would reside.  However, for this project we only need to know where the addresses of the segments' bases should be located.  For now, the addresses themselves will be supplied by the test files.  (I believe that we will need to supply them ourselves in the next chapter though.)

My approach to writing this program was to write out the assembly code for each possible VM code line, and then write python functions for producing these (see details below).  Because of all the overlap in the various assembly code groups, I used four functions: math operations, (in)equalities, push, and pop.  Along the way I came across a couple of sticky issues, namely:
* For the (in)equality assembly code, I needed to use jump statements, and therefore needed to place psuedo-commands.  Of course, one needs to make sure the labels for these are unique each time the (in)equality function is called, even across several .vm files.  
* For the pop command on the local, argument, this, or that segments, I required an additional data register, and so used R13.  I don't know if this is necessary, but I couldn't seem to avoid it.  

My VM translator, provided above, is written in Python 3 and is used as follows:

```python3 vmtranslator.py filename.vm```

For now, my program only accepts a single .vm file argument.  I've already written the additional code needed for handling a directory of .vm files, but I'm not including it yet because I haven't fully tested it.  The Chapter 8 project materials include a test directory for this though, so I will include it in that project.

Below is the assembly code I used for each of the possible VM commands.

Unary operators neg, not:
```
@SP
A = M-1
M = -M    // alternatively !M
```
Binary operators add, sub, and, or:
```
@SP
AM = M-1
D = M
A = A-1
M = M+D    // alternatively M-D, M&D, M|D
```
(In)equalities:
```
@SP
AM = M-1
D = M
A = A-1
D = M - D
@SETTRUEfileNameIneqCount    // translated to appropriate string
D;JEQ     // alternatively D;JGT, D;JLT
@SETFALSEfileNameIneqCount
0;JMP
(SETTRUEfileNameIneqCount)
@SP
A = M-1
M = -1
@ENDfileNameIneqCount
0;JMP
(SETFALSEfileNameIneqCount)
@SP
A = M-1
M = 0
(ENDfileNameIneqCount)
```
push argument n (alternatively local, this, that):
```
@ARG    // alternatively LCL, THIS, THAT
D = M
@n
A = A+D
D = M
@SP
A = M
M = D
@SP
M = M+1
```
push static n:
```
@fileName.n    // translated to appropriate string
D = M
@SP
A = M
M = D
@SP
M = M+1
```
push constant n:
```
@n
D = A
@SP
A = M
M = D
@SP
M = M+1
```
push pointer n (alternatively temp ):
```
@3    // alternatively 5
D = M
@SP
A = M
M = D
@SP
M = M+1
```
pop argument n (alternatively local, this, that):
```
@ARG    // alternatively LCL, THIS, THAT
D = M
@n
D = D+A
@R13
M = D
@SP
A = M-1
D = M
@R13
A = M
M = D
@SP
M = M-1
```
pop static n:
```
@SP
A = M-1
D = M
@fileName.n    // translated to appropriate string
M = D
@SP
M = M-1
```
pop pointer n (alternatively temp):
```
@SP
A = M-1
D = M
@3    // alternatively 5
M = D
@SP
M = M-1
```
