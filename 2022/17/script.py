from collections import defaultdict


hline = [(0,0),(1,0),(2,0),(3,0)]
cross = [(0,1),(1,1),(2,1),(1,0),(1,2)]
corner = [(0,0),(1,0),(2,0),(2,1),(2,2)]
vline = [(0,0),(0,1),(0,2),(0,3)]
square = [(0,0),(1,0),(0,1),(1,1)]

rocks = [hline,cross,corner,vline,square]

winds = open(0).read()

def rock_for_step(step): return rocks[step % 5]

def wind_for_step(ws): return 1 if winds[ws % len(winds)]=='>' else -1
    
def print_grid(grid,max_height):
    for y in reversed(range(max_height)):
        row = [ grid[(x,y)] for x in range(0,7)]
        print("".join(['|']+row+['|']))
    print("+-------+")

def move_ok(x,y,grid):
    return x >= 0 and x < 7 and grid[(x,y)] == '.' and y >= 0

def blow(coords,grid,ws):
    wx = wind_for_step(ws)
    new_coords = [(x+wx,y) for x,y in coords if move_ok(x+wx,y,grid)]
    
    if len(new_coords) == len(coords):
        return new_coords
    else: 
        return coords

def fall(coords,grid):
    new_coords = [(x,y-1) for x,y in coords if move_ok(x,y-1,grid)]
    
    if len(new_coords) == len(coords):
        coords = new_coords
        falling = True
    else:
        falling = False
    return (coords,falling)

def trim(grid,maxh):
    for x,y in [(x,y) for x,y in grid.keys() if y < maxh-100]:
        del grid[(x,y)]

grid = defaultdict(lambda:'.')

max_height = 0
wind_step = 0

cycle_tracker=defaultdict(lambda: list())

cyclecheck = [None]*(len(winds)*2)

rock_step = 0

limit = 1000000000000

divisor = None
target_step = None
diff = None
initial_height = None

for rock_step in range(limit):
    falling = True
    coords = [ (x+2,y+max_height+3) for x,y in rock_for_step(rock_step)]
    ws_at_start = wind_step
    h_at_start = max_height

    while falling:
        coords = blow(coords,grid,wind_step)
        wind_step += 1
        (coords,falling) = fall(coords,grid)
       
    for x,y in coords:
        grid[(x,y)] = '#'
        max_height = max(y+1,max_height)

    if (rock_step == 2021):
        print(f"1: {max_height}")

    trim(grid,max_height)
    
    if rock_step == target_step:
        m = max_height - (initial_height + ((rock_step // divisor)-1)*diff)
        h = initial_height-1 + ((limit//divisor)-1) * diff + m
        print(f"2: {h}")
        break

    if divisor is None:

        if (rock_step>0):
            cycle_tracker[rock_step] = [(max_height,max_height)]
        
        for i in [i for i in cycle_tracker if rock_step % i == 0]:
            tracker = cycle_tracker[i]
            diff = max_height - tracker[-1][0]
            tracker.append( (max_height, diff))
            
            if len(tracker) > 3 and len(set([d for _,d in tracker[-4:]]))==1:
                divisor = i
                initial_height = tracker[0][0]
                target_step = rock_step + (limit % divisor)
                break
            elif len(tracker) > 3 and tracker[-1][1] != tracker[-2][1]:
                del cycle_tracker[i]
    

if max_height < 100:
    print_grid(grid,max_height+1)
