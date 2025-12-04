from collections import defaultdict
import sys

def read_input():
    data = defaultdict(int)
    max_x = 0
    max_y = 0
    for y,line in enumerate(sys.stdin):
        line = line.rstrip()
        for x,p in enumerate(line):
            if p == '@':
                data[(x,y)] = 1
        max_y = y
        max_x = x
    return data,max_x,max_y

def print_grid(data,max_x,max_y):
    for y in range(max_y+1):
        line = ''.join([str(data[(x,y)]) for x in range(max_x+1)])
        print(line)

def find_removable(data,max_x,max_y):
    pos = []
    keys = list(data.keys())
    for x,y in keys:
        if data[(x,y)] == 0:
            continue
        surrounds = (
            (x-1,y-1),
            (x,y-1),
            (x+1,y-1),
            (x-1,y),
            (x+1,y),
            (x-1,y+1),
            (x,y+1),
            (x+1,y+1)
        )
        c = sum(data[(a,b)] for a,b in surrounds)
        if c < 4:
            pos.append((x,y))
    return pos

data,max_x,max_y = read_input()

removable = find_removable(data,max_x,max_y)
print('a)',len(removable))
b_count = len(removable)


while removable:
    for x,y in removable:
        data[(x,y)] = 0
    removable = find_removable(data,max_x,max_y)
    b_count += len(removable)


print_grid(data,max_x,max_y)
print('b)',b_count)        


