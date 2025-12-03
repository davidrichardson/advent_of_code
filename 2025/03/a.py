import sys

a_total = 0

for line in sys.stdin.readlines():
    line = line.rstrip()
    lmax = -1
    rmax = -1

    for i,v in enumerate(line):
        v = int(v)

        is_last_in_line = i == len(line) - 1


        if v > lmax and not is_last_in_line:
            lmax = v
            rmax = -1
        elif v > rmax:
            rmax = v
        
    j = (lmax*10)+rmax
    print(j)
    a_total += j

print('a)',a_total)