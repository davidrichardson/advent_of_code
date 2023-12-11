import sys
from itertools import combinations
from collections import defaultdict

def parse():
    galaxies = []
    x_gal_index = set()
    y_gal_index = set()

    for idy,line in enumerate(sys.stdin):
        for idx,c in enumerate(line.rstrip()):
            if c == '#':
                galaxies.append((idx,idy))
                x_gal_index.add(idx)
                y_gal_index.add(idy)
    
    return galaxies,x_gal_index,y_gal_index

def build_dist_lookup(dim_gal_indexes,expansion_factor):
    dim_min = min(dim_gal_indexes)
    dim_max = max(dim_gal_indexes)

    dist_lookup = defaultdict(lambda: 1)

    for d in range(dim_min,dim_max+1):
        if d not in dim_gal_indexes:
            dist_lookup[d] = expansion_factor

    return dist_lookup

def ordered(a,b):
    if (a > b): return b,a
    else: return a,b 

def dim_distance(a,b,dist_lookup):
    l,h = ordered(a,b)
    return sum((dist_lookup[i] for i in range(l,h)))

def distance_sum(expansion_factor,galaxies,x_gal_index,y_gal_index):
    x_dist_lookup = build_dist_lookup(x_gal_index,expansion_factor)
    y_dist_lookup = build_dist_lookup(y_gal_index,expansion_factor)

    total = 0
    for a,b in combinations(galaxies,2):
        x_dist = dim_distance(a[0],b[0],x_dist_lookup)
        y_dist = dim_distance(a[1],b[1],y_dist_lookup)

        total = total + x_dist + y_dist

    return total

galaxies,x_gal_index,y_gal_index = parse()

p1 = distance_sum(2,galaxies,x_gal_index,y_gal_index)
p2 = distance_sum(1_000_000,galaxies,x_gal_index,y_gal_index)

print(p1,p2)