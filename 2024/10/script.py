import sys
from itertools import chain
from functools import cache
topo_map = {}
trailheads = []

def parse_input():
    lines = sys.stdin.readlines()
    for y, line in enumerate(lines):
        for x, height in enumerate(line.rstrip()):
            pos = (x,y)
            height = int(height)
            topo_map[pos] = height
            if height == 0:
                trailheads.append(pos)


def reachable_max_height_positions(x,y,h) -> set[tuple[int,int]]:
    if h == 9:
        return set([(x,y)])
    
    next_pos = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]    
    next_h = h+1

    gen = (reachable_max_height_positions(p[0],p[1],next_h) for p in next_pos if p in topo_map and topo_map[p] == next_h)

    return set(chain.from_iterable(gen))


def paths_to_max_height(x,y,h) -> list[list[tuple[int,int]]]:
    if h == 9:
        path_seed = [(x,y)]
        return path_seed    

    next_pos = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]    
    next_h = h+1

    next_steps = [p for p in next_pos if p in topo_map and topo_map[p] == next_h]

    my_routes = []

    for ns in next_steps:
        paths = paths_to_max_height(ns[0],ns[1],next_h)
        for path in paths:
            new_path = [(x,y)]
            new_path.extend(path)
            my_routes.append(new_path)
            
    return my_routes

    

parse_input()

p1_score = sum((len(reachable_max_height_positions(x,y,0)) for x,y in trailheads))
print('p1',p1_score)

p2_score = sum((len(paths_to_max_height(x,y,0)) for x,y in trailheads))
print('p2',p2_score)