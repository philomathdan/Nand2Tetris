### Nand2Tetris Chapter 6 Notes:

After so many chapters of working within the confines of HDL or the Hack assembly language, it's nice to return to "simple" programming in this chapter. :-)  

Above is my assembler, written in Python 3.  It's used by entering 
```
python3 assembler.py filename.asm 
```
which will produce filename.hack.  

The first challenge for me in writing this program was to think about what steps were required to fully process the assembly file, given how it might look to start with.  I decided to pass through the lines of code a total of four times as follows:

1. Remove all comments, spaces, and blank lines (including those that are created after removing comments).
2. Remove each pseudo-command and add that label and the address of the next line to a dictionary of labels and addresses.
3. Replace each label (from a pseudo-command or a variable) with the appropriate numerical address.  These are kept in the same dictionary as step 2.
4. Translate each line into machine language.

Perhaps these steps can be combined somehow, but it's not obvious to me how.  For example, I can't set the address for a pseudo-command label until I'm sure the next line isn't blank or a comment.  Likewise I can't assign labels to addresses until I learn which ones refer to pseudo-commands and which refer to variables (as a reference to a pseudo-command could occur before that command's location is known).  

Obviously Step 4 involves the most activity.  The _A_-instructions are now simple to deal with: remove the @ symbol, translate to binary, and fill with leading zeros to ensure the length is 16.  For _C_-instructions, I first separate out the computation portion (along with the a bit), the destination portion, and the jump portion.  The destination portion can be dealt with simply by adding 1, 2 or 4 according to which registers are present.  For the computation and jump portions though, I placed all the possibilities into dictionaries.  This is perhaps rather brute force or inelegent, but it seemed simplest to me (though, for the computation portion, I needed to include two entries for the commutative operations, which seemed cumbersome). In the handling of each of these three portions, I added an error message if the portion couldn't be properly translated.  These were originally placed for trouble-shooting when I was writing the program, but I thought they would be nice to keep in the finished product.  However, these messages really _should_ also include the corresponding line number in the original asm file, but I didn't go to the trouble of keeping track of those, being anxious to get on to the next chapter.
