import sys
from itertools import pairwise

def parse():
    for line in sys.stdin:
        yield [int(n) for n in line.rstrip().split(' ')]

diffs = lambda vals: [b - a for a,b in pairwise(vals)]

def predictions(nums):
    vals_list = [nums]
    
    while any(x != 0 for x in vals_list[-1]):
        vals_list.append(diffs(vals_list[-1]))

    for idx in reversed(range(0,len(vals_list)-1)):
        end_d = vals_list[idx+1][-1]
        end_r = vals_list[idx][-1]

        start_d = vals_list[idx+1][0]
        start_r = vals_list[idx][0]

        vals_list[idx].insert(0,start_r-start_d)
        vals_list[idx].append(end_r+end_d)

    return vals_list[0][-1],vals_list[0][0]

p1_total = 0
p2_total = 0

for l in parse():
    p1p,p2p = predictions(l)
    p1_total = p1_total + p1p
    p2_total = p2_total + p2p

print(p1_total,p2_total)