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


grid = defaultdict(lambda:'.')

max_height = 0
wind_step = 0

for rock_step in range(2022):
    falling = True
    coords = [ (x+2,y+max_height+3) for x,y in rock_for_step(rock_step)]

    while falling:
        coords = blow(coords,grid,wind_step)
        wind_step += 1
        (coords,falling) = fall(coords,grid)
       
    for x,y in coords:
        grid[(x,y)] = '#'
        max_height = max(y+1,max_height)
    
    

    


if max_height < 100:
    print_grid(grid,max_height+1)
print(max_height)