import sys
from collections import defaultdict
from itertools import combinations
from math import dist
from typing import Generator


def parse_input():
    max_x,max_y = 0,0

    coords_per_signal: dict[str,list[tuple[int,int]]] = defaultdict(lambda: [])

    for y,line in enumerate(sys.stdin):
        line = line.rstrip()
        
        max_y = y
        max_x = len(line)-1

        for x,c in enumerate(line):
            if c == '.':
                ...
            else:
                pos = (y,x)
                coords_per_signal[c].append(pos)
        
    return coords_per_signal,max_y,max_x

def print_map(coords_per_signal,max_x,max_y,an_coords):
    grid = []
    for _ in range(max_y+1):
        grid.append(['.']*(max_x+1))

    for signal,coords in coords_per_signal.items():
        for y,x in coords:
            grid[y][x] = signal

    for y,x in an_coords:
        grid[y][x] = '#'

    for l in grid:
        print(''.join(l))

def diff(a,b):
    dy = a[0] - b[0]
    dx = a[1] - b[1]
    return dy,dx


def is_antinode_for_pair(p,a,b,signal):
    da = dist(p,a)
    db = dist(p,b)

    r = None
    if 0 not in [da,db]:
        r = da/db
    o = r in [2,0.5]  

    if o:
        print(f"{signal}: p:{p} a:{a} b:{b} {o}")

    return o  


def candidate_coords(antena_coords,max_y,max_x):
    for a,b in combinations(antena_coords,2):
        diff_y,diff_x = diff(a,b)

        candidates = set()    
        (y,x) = a
        while y <= max_y and x <= max_x and y >= 0 and x>= 0:
            candidates.add((y,x))
            y += diff_y
            x += diff_x
        (y,x) = a
        while y <= max_y and x <= max_x and y >= 0 and x>= 0:
            candidates.add((y,x))
            y -= diff_y
            x -= diff_x
        
        yield (candidates,a,b)




coords_per_signal,max_y,max_x = parse_input()
an_coords = set()
r_an_coords = set()
for signal,antenna_pos_list in coords_per_signal.items():
    for candidates,a,b in candidate_coords(antenna_pos_list,max_y,max_x):
        for c in candidates:
            if is_antinode_for_pair(c,a,b,signal):
                an_coords.add(c)
            r_an_coords.add(c)


print_map(coords_per_signal,max_x,max_y,r_an_coords)

print(len(an_coords),len(r_an_coords))

