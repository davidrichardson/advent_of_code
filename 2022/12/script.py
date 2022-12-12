import sys

steps_taken = 0
current_pos = set()

e_pos = (-1,-1)
height_grid = []

part1 = False

for y,line in enumerate(sys.stdin.read().splitlines()):
    height_grid.append([])
    for x,c in enumerate(line):
        if c=='E':
            e_pos = (y,x)
            c='z'
        if c=='S':
            if (part1):  current_pos.add((y,x))
            c='a'
        if c=='a' and not part1:
            current_pos.add((y,x))
        height_grid[-1].append(ord(c) - ord('a'))

steps_seen = {p:-1 for p in current_pos}

def possible_moves(y,x):
    ch = height_grid[y][x]
    a = [(py,x) for py in [y-1,y+1]] + [(y,px) for px in [x-1,x+1]]
    b = [(y,x) for y,x in a if y>-1 and x>-1 and y < len(height_grid) and x < len(height_grid[0])]
    c = [(y,x) for y,x in b if (height_grid[y][x] - ch) < 2]
    d = [(y,x) for y,x in c if (y,x) not in steps_seen]
    return set(d)


while len(current_pos)>0:
    next_steps = set()
    
    for y,x in current_pos:
        next_steps.update(possible_moves(y,x))

    current_pos = next_steps - steps_seen.keys()
    for p in current_pos: steps_seen[p] = steps_taken
    steps_taken += 1
    
    if e_pos in current_pos:
        break

print(steps_taken)