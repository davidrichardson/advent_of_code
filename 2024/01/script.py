import sys
import re

loc_lists = ([],[])

for line in sys.stdin:
    line = line.rstrip()

    vals = re.split('\s+',line)
    for i,v in enumerate(vals):
        loc_lists[i].append(int(v))

s_loc_lists = [None,None]

for i,ll in enumerate(loc_lists):
    s_loc_lists[i] = sorted(ll)    

s = 0

for i,a in enumerate(s_loc_lists[0]):
    b = s_loc_lists[1][i]
    s += abs(a - b)


print('part 1',s)    
    
from collections import Counter, defaultdict

r_counts = defaultdict(lambda: 0,Counter(loc_lists[1]))

ss = sum(v * r_counts[v] for v in loc_lists[0])

print('part 2',ss)