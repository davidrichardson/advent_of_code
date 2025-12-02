import sys

pos = 50
a_counter = 0
b_counter = 0

for line in sys.stdin:
    instr = line.rstrip()

    rotdir = instr[0].upper()
    mov = int(instr[1:])

    b_counter += mov // 100
    '''Every 100 cancels out, only consider the remainder'''
    mov = mov % 100

    '''Change pos based on the rotation instruction'''
    if rotdir == 'L':
        pos -= mov
        if pos < 0:
            pos += 100 
            b_counter += 1       
    elif rotdir == 'R':
        pos += mov
        if pos >= 100:
            pos -= 100
            b_counter += 1
    
    if pos == 0:
        a_counter += 1
    
    print(instr,rotdir,mov,pos,a_counter,b_counter)


print("a) ",a_counter)
print("b) ",b_counter)