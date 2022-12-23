from collections import defaultdict
from itertools import count

def bounds(grid):
    xlim = (0,0)
    ylim = (0,0)
    for x,y in grid:
        xlim = ( min(xlim[0],x), max(xlim[1],x))
        ylim = ( min(ylim[0],y), max(ylim[1],y))
    return (xlim,ylim)

def print_grid(grid):
    (xlim,ylim) = bounds(grid)
    for y in range(ylim[0],ylim[1]+1):
        row = [ grid[(x,y)] if (x,y) in grid else '.' for x in range(xlim[0],xlim[1]+1)]
        print("".join(row))


def read_input():
    grid = {}
    
    for y,row in enumerate(open(0).read().splitlines()):
            for x,c in enumerate(row):
                if c == '#':
                    grid[(x,y)] = c

    return grid

def nface(pos,clear_spots):
    (x,y),(nw,n,ne,_,_,_,_,_) = pos,clear_spots
    if nw and n and ne:
        return True,(x,y-1)
    else:
        return False,(x,y)

def wface(pos,clear_spots):
    (x,y),(nw,_,_,w,_,sw,_,_) = pos,clear_spots
    if nw and w and sw:
        return True,(x-1,y)
    else:
        return False,(x,y)

def eface(pos,clear_spots):
    (x,y),(_,_,ne,_,e,_,_,se) = pos,clear_spots
    if ne and e and se:
        return True,(x+1,y)
    else:
        return False,(x,y)

def sface(pos,clear_spots):
    (x,y),(_,_,_,_,_,sw,s,se) = pos,clear_spots
    if sw and s and se:
        return True,(x,y+1)
    else:
        return False,(x,y)


consideration = [
    nface,
    sface,
    wface,
    eface
]

def round(grid,t):
    proposal = defaultdict(lambda: [])
    start_idx = t%4
    no_move_planned = set()

    for (x,y) in grid.keys():
        around = [  (x-1,y-1),(x,y-1),(x+1,y-1),
                    (x-1,y),            (x+1,y),
                    (x-1,y+1),(x,y+1),(x+1,y+1)]
        
        #clear spots
        #(nw,n,ne,w,e,sw,s,se) 
        clear_spots = [(x,y) not in grid for x,y in around]
    
        nx,ny = x,y

        if not all(clear_spots):
            for i in range(4):
                idx = (start_idx+i)%4
                (changed,npos) = consideration[idx]((x,y),clear_spots)
            
                if changed:
                    nx,ny = npos
                    break

        if (nx,ny) == (x,y):
            no_move_planned.add((x,y))
        else:
            proposal[nx,ny].append((x,y))
        

    grid = {}

    move_count = 0

    for (x,y),prev in proposal.items():
        if len(prev) == 1:
            grid[x,y] = '#'
            move_count += 1
        else:
            for x,y in prev:
                grid[x,y] = '#'
    
    for (x,y) in no_move_planned:
        grid[x,y] = '#'
    
    return grid,move_count



initial_grid = read_input()


p1_grid = initial_grid
for t in range(10):
    p1_grid,_ = round(p1_grid,t)


(xlim,ylim) = bounds(p1_grid)
area = (1+ xlim[1] - xlim[0]) * (1+ylim[1] - ylim[0]) 
print(f"p1: {area - len(p1_grid)}")

p2_grid = initial_grid
for r in count():
    p2_grid,move_count = round(p2_grid,r)
    if move_count==0:
        print(f"p2: {r+1}")
        break