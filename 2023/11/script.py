import sys
from itertools import combinations
from collections import defaultdict
 
def parse() -> tuple[list[int,int],set[int],set[int]]:
    galaxies = []
    gal_xs = set()
    gal_ys = set()

    for idy,line in enumerate(sys.stdin):
        for idx,c in enumerate(line.rstrip()):
            if c == '#':
                galaxies.append((idx,idy))
                gal_xs.add(idx)
                gal_ys.add(idy)
    
    return galaxies,gal_xs,gal_ys

def build_dist_lookup(gals_in_dim,ef):
    dim_min = min(gals_in_dim)
    dim_max = max(gals_in_dim)

    dist_lookup = defaultdict(lambda: 1)

    for d in range(dim_min,dim_max+1):
        if d not in gals_in_dim:
            dist_lookup[d] = ef

    return dist_lookup

def ordered(a,b):
    if (a > b): return b,a
    else: return a,b 

def dim_dist(a,b,dist_lookup):
    l,h = ordered(a,b)
    distances = (dist_lookup[i] for i in range(l,h))
    return sum(distances)

def distance_sum(ef,galaxies,gal_xs,gal_ys):
    xdl = build_dist_lookup(gal_xs,ef)
    ydl = build_dist_lookup(gal_ys,ef)

    def pair_distance(a,b): 
        x_dist = dim_dist(a[0],b[0],xdl)
        y_dist = dim_dist(a[1],b[1],ydl)
        return x_dist + y_dist

    return sum(pair_distance(a,b) for a,b in combinations(galaxies,2))

galaxies,gal_xs,gal_ys = parse()

p1 = distance_sum(2,galaxies,gal_xs,gal_ys)
p2 = distance_sum(1_000_000,galaxies,gal_xs,gal_ys)

print(p1,p2)