import sys


"""
This function receives a string representation of one of the allowed math operations
and returns, as a list, all the equivalent assembly commands.
"""
def mathAssembly(op):
    
    unaryOps = {'neg':'-', 'not':'!'}
    binaryOps = {'add':'+', 'sub':'-', 'and':'&', 'or':'|'}

    if op in unaryOps:
        return ['@SP\n','A = M-1','M = '+unaryOps[op]+'M']
    if op in binaryOps:
        return ['@SP','AM = M-1','D = M','A = A-1','M = M'+binaryOps[op]+'D']

        
"""
This function receives a string representation of one of the allowed inequality
operations and a unique label string assigned to that operation by the calling
function.  It returns a list of all the assembly commands representing the
inequality operation. 
"""
def ineqAssembly(op,label):
    
    ineqs = {'eq':'JEQ', 'gt':'JGT', 'lt':'JLT'}

    return ['@SP','AM = M-1','D = M','A = A-1','D = M - D','@SETTRUE'+label,
                'D;'+ineqs[op],'@SETFALSE'+label,'0;JMP','(SETTRUE'+label+')',
                '@SP','A = M-1','M = -1','@END'+label,'0;JMP','(SETFALSE'+label+')',
                '@SP','A = M-1','M = 0','(END'+label+')']



"""
This function receives string representations of the segment, index, and filename
and returns the assembly code representing the virtual machine command 'push segment n'.
The filename is used to provide a unique lable in the case the static segment is
provided.
"""
def pushAssembly(segment,n,fileName):

    endCode = ['@SP','A = M','M = D','@SP','M = M+1']

    LATT = {'local':'@LCL','argument':'@ARG','this':'@THIS','that':'@THAT'}

    SPT = {'static':'@'+fileName+'.'+n, 'pointer':'@'+str(3+int(n)),
       'temp':'@'+str(5+int(n))}
    
    if segment in LATT:
        return [LATT[segment],'D = M','@'+n,'A = A+D','D = M']+endCode

    if segment in SPT:
        return [SPT[segment],'D = M']+endCode

    if segment == 'constant':
        return ['@'+n,'D = A']+endCode


"""
This function receives string representations of the segment, index, and filename
and returns the assembly code representing the virtual machine command 'pop segment n'.
The filename is used to provide a unique label in the case the static segment is
provided.
"""
def popAssembly(segment,n,fileName):

    endCode1 = ['@SP','A = M-1','D = M']
    endCode2 = ['M = D','@SP','M = M-1']

    LATT = {'local':'@LCL','argument':'@ARG','this':'@THIS','that':'@THAT'}

    if segment in LATT:
        return [LATT[segment],'D = M','@'+n,'D = D+A','@R13','M = D'] + endCode1 + ['@R13','A = M'] + endCode2

    SPT = {'static':'@'+fileName+'.'+n, 'pointer':'@'+str(3+int(n)),
       'temp':'@'+str(5+int(n))}

    if segment in SPT:
        return endCode1 + [SPT[segment]] + endCode2


"""
This function receives a .vm file name as a string and returns, as a list,
all the equivalent assembly commands.
"""
def assembleVMFile(fullFileName):

# Open the file, clean out comments,
# and load resulting lines into a list vmLines.
    vmFile = open(fullFileName, 'r')
    vmLines = []
    for line in vmFile:
        line = line.strip()
        comIndex = line.find('//')
        if comIndex > -1:
            line = line[:comIndex]
        if len(line) > 0:
            vmLines.append(line.split())
    vmFile.close()

# Keep track of file name, and keep a count of inequalities.
# Both of these are used in constructing unique labels.
    fileName = fullFileName[:-3]
    ineqCount = 0

# Process each vmLine, checking for appropriate syntax, 
# and add to list to be returned.
    assemblyLines = []

    for line in vmLines:
        if len(line) == 1:
            if line[0] in ['eq','gt','lt']:
                assemblyLines += ineqAssembly(line[0],fileName+str(ineqCount))
                ineqCount += 1
            elif line[0] in ['neg','not','add','sub','and','or']:
                assemblyLines += mathAssembly(line[0])
            else:
                print('Unknown operation: ',line[0])

        pushSegments = ['local','argument','this','that','static','pointer','temp','constant']
        popSegments = ['local','argument','this','that','static','pointer','temp']
        
        if len(line) == 3:        
            if line[0] == 'push':
                if line[1] not in pushSegments:
                    print('Unrecognized push segment:',line[0],'*'+line[1]+'*',line[2])
                elif not line[2].isdigit():
                    print('Unrecognized push index:',line[0],line[1],'*'+line[2]+'*')
                else:
                    assemblyLines += pushAssembly(line[1],line[2],fileName)

            if line[0] == 'pop':
                if line[1] not in popSegments:
                    print('Unrecognized pop segment:',line[0],'*'+line[1]+'*',line[2])
                elif not line[2].isdigit():
                    print('Unrecognized pop index:',line[0],line[1],'*'+line[2]+'*')
                else:
                    assemblyLines += popAssembly(line[1],line[2],fileName)

    return assemblyLines


def main():
    FullVMFileName = sys.argv[1]

    assemblyFile = open(FullVMFileName[:-3]+'.asm','w')

    for line in assembleVMFile(FullVMFileName):
        assemblyFile.write(line+'\n')

    assemblyFile.close()


if __name__ == '__main__':
    main()








    
