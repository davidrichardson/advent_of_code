import re
from collections import Counter

def min_max(items):
    return [min(items),max(items)]

def bounds(grid):
    xlim = min_max([x for x,_ in grid.keys()])
    ylim = min_max([y for _,y in grid.keys()])
    return (xlim,ylim)

def print_grid(grid):
    if len(grid) == 0: return "<empty>"
    (xlim,ylim) = bounds(grid)
    for y in range(ylim[0],ylim[1]+1):
        row = [ grid[(x,y)] if (x,y) in grid else '.' for x in range(xlim[0],xlim[1]+1)]
        print("".join(row))

def sensor_point(grid,x,y):
    grid[(x,y)] = 'S'

def beacon_point(grid,x,y):
    grid[(x,y)] = 'B'

def scanned_point(grid,x,y):
    grid[(x,y)] = '#'

def read_input():
    return [list(map(int,re.findall(r"-?\d+",l))) for l in open(0).read().splitlines()]
        
def phase_1():
    rows_of_interest = { r:{} for r in [10,2000000] }

    for sx,sy,bx,by in read_input():
        

        manhatten_distance = abs(sx - bx) + abs ( sy - by)

        for y,row in rows_of_interest.items():
            if y == sy: sensor_point(row,sx,sy)
            if y == by: beacon_point(row,bx,by)

            if y >= sy - manhatten_distance and y <= sy+manhatten_distance:
                dy = abs(sy - y)
                dx = abs(dy - manhatten_distance)                 
                
                for x in range(sx - dx, sx + dx+1):
                    if (x,y) not in row:
                        scanned_point(row,x,y)

    if (rows_of_interest[2000000]=={}):
        grid = {}
        for row in rows_of_interest.values():
            for (x,y),c in row.items():
                grid[(x,y)] = c
        print_grid(grid)

    for y,row in rows_of_interest.items():
        counter = Counter(row.values())
        count = counter['#']+counter['S']
        print(f"{y} {count}")
                

phase_1()

