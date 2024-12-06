import sys
import re


mul_matcher = 'mul\((\d+),(\d+)\)'
dont_matcher = "don't\(\)"
do_matcher = "do\(\)"

p = re.compile('|'.join([mul_matcher,do_matcher,dont_matcher]))


p1_total = 0
p2_total = 0
mul_enabled = True

for line in sys.stdin:

    for match in p.finditer(line):
        instr = match.group(0)[:3]

        if instr == 'mul':
            a = int(match.group(1))
            b = int(match.group(2))
            x = a*b
            p1_total += x 
            
            if mul_enabled:
                p2_total += x
        elif instr == 'don':
            mul_enabled = False
        elif instr == 'do(':
            mul_enabled = True
        

print('part 1',p1_total)
print('part 2',p2_total)