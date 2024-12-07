import sys
from collections import deque
import re

def parse(line: str) -> tuple[str,tuple[int]]:
    layout,numbers = line.rstrip().split(' ')
    contigs = tuple(int(x) for x in numbers.split(','))
    return layout,contigs

def possibilities(layout: str):
    dq = deque([layout])
    
    while dq:
        l = dq.popleft()
        f = l.find('?')
        if f >= 0:
            dq.append(l.replace('?','.',1))
            dq.append(l.replace('?','#',1))
        else:
            yield l

def validator(contigs):
    pattern_mid = '\.+'.join(['#'*c for c in contigs])
    pattern = '^\.*'+pattern_mid+'\.*$'
    regex = re.compile(pattern)
    
    return lambda l: bool(regex.search(l))

  
    
    
def p1(layout: str,contigs: tuple[int]):
    is_valid = validator(contigs)
    return sum(1 for p in possibilities(layout) if is_valid(p))
        
lines = [line for line in sys.stdin]

p1_total = 0
for line in lines:
    layout,contigs = parse(line)
    p1_count = p1(layout,contigs)
    p1_total += p1_count

print(p1_total)
