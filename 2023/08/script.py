import sys
import re
from itertools import cycle
from math import lcm

def parse():
    lines = [line.rstrip() for line in sys.stdin]
    
    instructions = lines[0]

    layout = {}
    pattern = re.compile("\w+")
    for l in lines[2:]:
        n,l,r = pattern.findall(l)
        layout[n] = {'L':l,'R':r}
    
    return instructions,layout

def part_one(instructions,layout):
    node = 'AAA'
    steps = 0

    for d in cycle(instructions):
        node = layout[node][d]
        steps = steps+1
        if node == 'ZZZ':
            break
    
    return steps

def part_two(instructions,layout):
    nodes = [l for l in layout.keys() if l.endswith('A')]
    hit_z = [-1] * len(nodes)
    
    for c,d in enumerate(cycle(instructions)):
        nodes = [layout[n][d] for n in nodes]
        
        for idx,s in enumerate(hit_z):
            if s < 0 and nodes[idx].endswith("Z"):
                hit_z[idx] = c+1

        if all(s > 0 for s in hit_z):
            break
    
    return lcm(*hit_z)

instructions,layout = parse()

print(part_one(instructions,layout),part_two(instructions,layout))
