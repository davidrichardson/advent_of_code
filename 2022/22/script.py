from collections import defaultdict

#R = +1 idx, L = -1 idx
dirs = ['>','v','<','^'] 

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
        row = [ grid[(x,y)] for x in range(xlim[0],xlim[1]+1)]
        print("".join(row))

def str_to_map(map_str):
    grid = defaultdict(lambda: ' ')
    for y,row in enumerate(map_str.splitlines()):
        for x,c in enumerate(row):
            if c != ' ':
                grid[(x,y)] = c
    return grid

def str_to_instructions(inst_str):
    buffer = []
    instr = []
    for chr in inst_str:
        if chr in ['R','L']:
            if buffer:
                instr.append(int(''.join(buffer)))
                buffer = []
            instr.append(chr)
        else:
            buffer.append(chr)
    if buffer:
        instr.append(int(''.join(buffer)))
    return instr    

def read_input():
    input = open(0).read()
    (map_str,inst_str)= input.split("\n\n")
    return str_to_map(map_str),str_to_instructions(inst_str)

def walk(steps,dir_sym,pos,grid,path_illustration):
    (x,y) = pos
        
    for s in range(steps):
        path_illustration[(x,y)] = dir_sym

        nx,ny = x,y
        match dir_sym:
            case '>': nx +=1
            case '<': nx -=1
            case 'v': ny +=1
            case '^': ny -=1

        match grid[(nx,ny)]:
            case '.': (x,y) = (nx,ny)
            case '#': break
            case ' ': 
                if dir_sym in ['^','v']: 
                    matcher = lambda a,_: nx == a
                else:
                    matcher = lambda _,b: ny == b

                same_plane = sorted([((a,b),c) for (a,b),c in grid.items() if matcher(a,b)])
                
                idx = 0 if dir_sym in ['>','v'] else -1
                ((nx,ny),c) = same_plane[idx]
                match c:
                    case '.': x,y = nx,ny
                    case '#': break

    return (x,y)
    



grid,instructions = read_input() 
path_illustration = grid.copy()

x = min([x for (x,y),c in grid.items() if y==0 and c =='.'])
y = 0

dir_idx = 0
dir_sym = dirs[dir_idx]


for instr in instructions:
    if instr in ['L','R']:
        change = 1 if instr == 'R' else -1
        dir_idx += change
        dir_idx = dir_idx%len(dirs)
        dir_sym = dirs[dir_idx]
    else:
        (x,y) = walk(instr,dir_sym,[x,y],grid,path_illustration)


print_grid(path_illustration)

password = ((y+1)* 1000) + ((x+1)*4) + dir_idx

print(password)



