from collections import Counter
import sys

for l in sys.stdin.readlines():
    c = Counter(l)
    print('a)', c.get('(', 0)  - c.get(')', 0) )

    pos = 0
    for i,c in enumerate(l.rstrip()):
        if c == '(':
            pos += 1
        elif c == ')':
            pos -= 1
        if pos < 0:
            print('b)', i+1)
            break