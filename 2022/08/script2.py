import sys

def distance(h,trees):
    visi = [idx for idx,z in enumerate(trees) if z>=h]
    return len(trees) if len(visi)==0 else visi[0]+1 

grid = []
ss = 0

for line in sys.stdin.read().splitlines():
    grid.append(line)

for y in range(1,len(grid)-1):
    for x in range(1,len(grid[y])-1):
        h = grid[y][x]
        l = distance(h,list(reversed(grid[y][0:x])))
        r = distance(h,grid[y][x+1:])
        t = distance(h,list(reversed([z[x] for z in grid[0:y]])))
        b = distance(h,[z[x] for z in grid[y+1:]])

        ss = max(ss,l*r*t*b)
        
print(ss)