import sys
from collections import defaultdict
from itertools import chain
N = 0,-1#top of map, low y
S = 0,1 #bottom of map, high y
E = 1,0 #right of map, high x
W = -1,0#left of map, low x

pipe_ref = {
    '|': (N,S),
    '-': (E,W),
    'L': (N,E),
    'J': (N,W),
    '7': (S,W),
    'F': (S,E)
}
def parse() -> tuple[dict[tuple[int,int],tuple[tuple[int,int],tuple[int,int]]],tuple[int,int]]:
    layout = defaultdict(lambda: '.')
    start = None
    for idy,line in enumerate(sys.stdin):
        for idx,c in enumerate(line.rstrip()):
            if c != '.':
                layout[(idx,idy)] = c
            if c == 'S':
                start = (idx,idy)
    return layout,start

def move(curr: tuple[int,int], mov: tuple[int,int]) -> tuple[int,int]:
    return curr[0]+mov[0],curr[1]+mov[1]

def next_step(layout,steps):
    pos = steps[-1]
    pipe = layout[pos]
    possible_moves = pipe_ref[pipe]
    possible_pos = (move(pos,s) for s in possible_moves)
    next_pos = next( (p for p in possible_pos if p != steps[-2] ) )
    steps.append(next_pos)

def part_one(layout,start):
    possible_start_steps = []

    #start pipe type is unclear
    for d in (N,S,E,W):
        pos = move(start,d)
        pipe_at_pos = layout[pos]
        rd = tuple([x * -1 for x in d])
        if pipe_at_pos != '.' and rd in pipe_ref[pipe_at_pos]:
            possible_start_steps.append(move(start,d))

    steps = 1
    fwd_steps = [start,possible_start_steps[0]]
    rev_steps = [start,possible_start_steps[1]]

    while fwd_steps[-1] != rev_steps[-1]:
        steps = steps+1
        next_step(layout,fwd_steps)
        next_step(layout,rev_steps)
    return steps,fwd_steps,rev_steps

layout,start = parse()

steps,fwd_steps,rev_steps = part_one(layout,start)
print("part 1",steps)

max_x,max_y = 0,0
new_layout = defaultdict(lambda: '.')
for p in chain(fwd_steps,rev_steps):
    new_layout[p] = layout[p]
    max_x = max(max_x,p[0])
    max_y = max(max_y,p[1])

simple_layout = []
for y in range(0,max_y+1):
    simple_layout.append( [new_layout[(x,y)] for x in range(0,max_x+1)] )

for l in simple_layout: print(''.join(l))