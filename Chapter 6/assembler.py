import sys

# Open the file assembly file named when this program was called.

assemblyFileName = sys.argv[1]
assemblyFile = open(assemblyFileName, 'r')


# Put lines from original file into a list.

rawLines = []

for line in assemblyFile:               
    rawLines.append(line.strip())

assemblyFile.close()


# Clean the raw lines by finding and removing comments and removing any white space.    

cleanedLines = []

for line in rawLines:
    comIndex = line.find('//')
    if comIndex > -1:                   
        line = line[:comIndex]          
    line = ''.join(line.split())        
    if len(line) > 0:                   
        cleanedLines.append(line)


# A dictionary of address labels, initiated with the predefined labels        

memoryLabels = {'SP':0, 'LCL':1, 'ARG':2,'THIS':3,'THAT':4,
             'R0':0,'R1':1,'R2':2,'R3':3, 'R4':4,'R5':5, 'R6':6,
             'R7':7,'R8':8,'R9':9,'R10':10,'R11':11,'R12':12,'R13':13,
             'R14':14,'R15':15,'SCREEN':16384,'KBD':24576}
    

# Remove pseudo-commands and add those labels and the appropriate addresses to
# the address label dictionary created above.

noPseudoLines = []
linecount = -1
for line in cleanedLines:
    if line[0] == '(':
        memoryLabels[line[1:-1]] = linecount + 1
    else:
        noPseudoLines.append(line)
        linecount += 1

# Use the address label dictionary to replace all labels with their numerical address.
# User created variables are given addresses starting at 16.

noSymbolList = []
labelAddress = 16
for line in noPseudoLines:
    if line[0] == '@':
        lineRest = line[1:]
        if not lineRest.isdigit():
            if lineRest not in memoryLabels:
                memoryLabels[lineRest] = labelAddress
                labelAddress += 1
            line = '@' + str(memoryLabels[lineRest])
    noSymbolList.append(line)

    
# A dictionary of translations for jump commands

jumpCommands = {'':'000', 'JGT':'001', 'JEQ':'010', 'JGE':'011', 'JLT':'100',
            'JNE':'101', 'JLE':'110', 'JMP':'111'}


# A dictionary of translations for ALU commands, including the a bit at the start
# For commutative operations there are two entries to handle both orders.

ALUCommands = {'0':'0101010', '1':'0111111', '-1':'0111010', 'D':'0001100',
           'A':'0110000', 'M':'1110000', '!D':'0001101', '!A':'0110001',
           '!M':'1110001', '-D':'0001111', '-A':'0110011', '-M':'1110011',
           'D+1':'0011111', '1+D':'0011111', 'A+1':'0110111', '1+A':'0110111',
           'M+1':'1110111', '1+M':'1110111', 'D+1':'0011111', '1+D':'0011111',
           'A+1':'0110111', '1+A':'0110111', 'M+1':'1110111', '1+M':'1110111',
           'D-1':'0001110', 'A-1':'0110010', 'M-1':'1110010', 'D+A':'0000010',
           'A+D':'0000010', 'D+M':'1000010', 'M+D':'1000010', 'D-A':'0010011',
           'D-M':'1010011', 'A-D':'0000111', 'M-D':'1000111', 'D&A':'0000000',
           'A&D':'0000000', 'D&M':'1000000', 'M&D':'1000000', 'D|A':'0010101',
           'A|D':'0010101', 'D|M':'1010101', 'M|D':'1010101'}


# Perform the final translation to machine code, and write each line to the hack file. 
# A-commands are simply translated to binary (and extended to 16 digits).
# C-commands are separated into computation, destination, and jump portions.


hackFile = open(assemblyFileName[:-4]+'.hack', 'w')

for line in noSymbolList:
    
    if line[0] == '@':
        hackFile.write(str(bin(int(line[1:])))[2:].zfill(16) + '\n')

    else:
        eqindex = line.find('=')
        if eqindex > -1:
            dest = line[:eqindex]
            line = line[eqindex+1:]
        else:
            dest = ''
        scindex = line.find(';')
        if scindex > -1:
            comp = line[:scindex]
            jump = line[scindex+1:]
        else:
            comp = line
            jump = ''

        destValue = 0
        if 'M' in dest:
            destValue += 1
        if 'D' in dest:
            destValue += 2
        if 'A' in dest:
            destValue += 4
        for x in dest:
            if x not in 'MDA':
                print('Incorrect destination command:', dest)
        destCode = str(bin(destValue))[2:].zfill(3)

        if comp in ALUCommands:
            compCode = ALUCommands[comp]
        else:
            print('Incorrect computation command:', comp)
            compCode = '0000000'

            
        if jump in jumpCommands:
            jumpCode = jumpCommands[jump]
        else:
            print('Incorrect jump command:', jump)
            jumpCode = '000'

        hackFile.write('111'+compCode+destCode+jumpCode+'\n')

            
hackFile.close()



            





 











