import sys

b_total = 0

for line in sys.stdin.readlines():
    line = line.rstrip()
    dmax = [-1] * 12
    for i,v in enumerate(line):
        v = int(v)

        digits_available_after = len(line) - i - 1
        used = False
        
        for j,c in enumerate(dmax):
            digits_needed = len(dmax) - j - 1
            # don't evaluate if there isn't enough line left to fill remaining digits
            if not used and v > c and digits_available_after >= digits_needed: 
                dmax[j] = v
                used = True
            elif used:
                #if you change a digit, reset dmax for all after it
                dmax[j] = -1
        
    j = int(''.join(map(str,dmax)))
    print(line,j)
    
    b_total += j

print('b)',b_total)