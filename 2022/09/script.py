import sys


def display_grid(knots,visited):
    (min_x, min_y, max_x, max_y) = (0,0,0,0)

    for x,y in knots+list(visited):
        min_x = min(min_x,x)
        max_x = max(max_x,x)
        min_y = min(min_y,y)
        max_y = max(max_y,y)
    
    max_x = max(max_x,6)
    max_y = max(max_y,5)

    grid = []
    
    for idx in range(min_y,max_y+1):
        grid.append( ['.'] * (1+(max_x - min_x)) )

    def write(x,y,c):
        grid[y-min_y][x-min_x] = c 
    
    for x,y in visited: write(x,y,'#')
    write(0,0,'s')
    for idx,knot in enumerate(knots):
        (x,y) = knot
        write(x,y, 'H' if idx == 0 else str(idx))
    
    for r in reversed(grid): print(''.join(r))

def move_head(h,dir):
    (x,y) = h
    
    match dir:
        case 'U': y += 1
        case 'D': y -= 1
        case 'L': x -= 1
        case 'R': x += 1
        case _:
            raise Exception(f"unexpected instruction in: {line}")
    
    return (x,y)


def move_knot(h,k):
    (hx,hy) = h
    (kx,ky) = k
    (dx,dy) = (hx - kx,hy - ky)

    out_of_contact = abs(dx)>1 or abs(dy)>1

    if (out_of_contact):
        if (hx != kx and hy != ky):
            # not in same row or col, make a diagonal move
            if dx > 0 : kx += 1
            else: kx -= 1

            if dy > 0 : ky +=1
            else: ky -= 1
        else:
            if (dx > 1):
                kx += 1
            if (dx < -1):
                kx -= 1
            if (dy > 1):
                ky +=1
            if (dy < -1):
                ky -=1
    
    return (kx,ky)

# head of knot = idx 0, tail = idx - 1
knot_count = 10 # part 1 = 2, part 2 = 10
knots = [(0,0)] * knot_count
visited = set()
    
for line in sys.stdin.read().splitlines():
    (dir,steps) = line.split(" ")

    for i in range(int(steps)):
        knots[0] = move_head(knots[0],dir)

        for i in range(len(knots) - 1):
            knots[i+1] = move_knot(knots[i],knots[i+1])    
            
        visited.add(knots[-1])


display_grid(knots,visited)
print(len(visited))
