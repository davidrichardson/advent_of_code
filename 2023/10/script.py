import sys
from collections import defaultdict,deque


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

def read():
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip())
    return lines

def parse(lines: list[str]) -> tuple[dict[tuple[int,int],tuple[tuple[int,int],tuple[int,int]]],tuple[int,int]]:
    layout = defaultdict(lambda: '.')
    start = None
    for idy,line in enumerate(lines):
        for idx,c in enumerate(line):
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
    possible_start_moves = []

    #start pipe type is unclear
    for d in (N,S,E,W):
        pos = move(start,d)
        pipe_at_pos = layout[pos]
        rd = tuple([x * -1 for x in d])
        if pipe_at_pos != '.' and rd in pipe_ref[pipe_at_pos]:
            possible_start_moves.append(d)
            possible_start_steps.append(move(start,d))
    for k,v in pipe_ref.items():
        if all(d in v for d in possible_start_moves):
            layout[start] = k

    steps = 1
    fwd_steps = [start,possible_start_steps[0]]
    rev_steps = [start,possible_start_steps[1]]

    while fwd_steps[-1] != rev_steps[-1]:
        steps = steps+1
        next_step(layout,fwd_steps)
        next_step(layout,rev_steps)
    return steps,fwd_steps,rev_steps

def part_two(steps,layout):
    x_s, y_s = set(),set()
    steps=set(steps)
    for p in steps:
        x_s.add(p[0])
        y_s.add(p[1])
    max_x = max(x_s)
    max_y = max(y_s)

    area = 0

    for y in range(max_y+1):
        norths = 0
        for x in range(max_x+1):
            con = layout[(x,y)]

            if (x,y) in steps:
                pipe_directions = pipe_ref[con]
                if N in pipe_directions:
                    norths += 1
                continue

            if norths % 2 != 0:
                area = area + 1
    
    return area


def display_loop(layout,fwd_steps,rev_steps):
    x_s, y_s = set(),set()
    max_x,max_y = 0,0
    new_layout = defaultdict(lambda: ' ')
    steps = fwd_steps + list(reversed(rev_steps))

    for p in steps:
        new_layout[p] = layout[p]
        x_s.add(p[0])
        y_s.add(p[1])

    min_x,max_x = min(x_s),max(x_s)
    min_y,max_y = min(y_s),max(y_s)

    simple_layout = []
    for y in range(min_y,max_y+1):
        simple_layout.append( [new_layout[(x,y)] for x in range(min_x,max_x+1)] )

    tr = str.maketrans("-|F7LJ.", "─│┌┐└┘ ")

    for l in simple_layout: print(''.join(l).translate(tr))



lines = read()
layout,start = parse(lines)

num_steps,fwd_steps,rev_steps = part_one(layout,start)
area = part_two(fwd_steps+rev_steps,layout)
display_loop(layout,fwd_steps,rev_steps)

print("part 1",num_steps)
print("part 2",area)


    

