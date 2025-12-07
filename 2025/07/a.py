import sys
from collections import defaultdict

def parse_line(line):
    return { x:c for x,c in enumerate(l.strip()) if c != '.' }

splits_used = defaultdict(int)
last_row = None

for y,l in enumerate(sys.stdin.readlines()):
    row = parse_line(l)
    if not last_row:
        #start only
        last_row = {pos:1 for pos in row.keys()}
        continue
    
    this_row = defaultdict(int)
    for pos,count in last_row.items():
        if pos in row:
            this_row[pos-1] += count
            this_row[pos+1] += count
            splits_used[(pos,y)] += 1
        else:
            this_row[pos] += count
    last_row = this_row

print('a)',len(splits_used))
print('b)',sum(last_row.values()))
        


