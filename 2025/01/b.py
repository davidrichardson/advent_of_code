import sys

pos = 50
a_counter = 0
b_counter = 0

for line in sys.stdin:
    instr = line.rstrip()

    rotdir = instr[0].upper()
    mov = int(instr[1:])

    for _ in range(0,mov):
        if rotdir == 'L':
            pos -= 1
            if pos == -1:
                pos = 99       
        elif rotdir == 'R':
            pos += 1
            if pos == 100:
                pos = 0
        if pos == 0:
            b_counter += 1
    if pos == 0:
        a_counter += 1

print("a) ",a_counter)
print("b) ",b_counter)