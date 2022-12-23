from collections import defaultdict
from dataclasses import dataclass
from itertools import groupby

@dataclass
class Node():
    x: int
    y: int
    wall: bool = False
    up: any = None
    down: any = None
    left: any = None
    right: any = None

    def pos(self): return (self.x,self.y)
    def zpos(self): return (self.x-1,self.y-1)

    def walk(self,dir,steps):
        if (steps == 0):
            return self

        match dir:
            case '^': nxt=self.up
            case 'v': nxt=self.down
            case '<': nxt=self.left
            case '>': nxt=self.right

        if nxt.wall:
            return self
        
        return nxt.walk(dir,steps-1)


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


def str_to_nodes(map_str):
    
    first_node = None
    curr_row = None
    prev_row = None
    nodes = []

    for y,row in enumerate(map_str.splitlines()):
        curr_row = []

        for x,c in enumerate(row):
            if c == ' ': continue

            node = Node(x+1,y+1,c=='#')

            if first_node is None: first_node = node

            curr_row.append(node)
            nodes.append(node)
            if prev_row is not None:
                node_above = [n for n in prev_row if n.x == node.x]
                for na in node_above:
                    node.up = na
                    na.down = node

            # horizontal wrapping
            if len(curr_row) > 1:
                node.left = curr_row[-2]
                curr_row[-2].right = node
        
        curr_row[0].left = curr_row[-1]
        curr_row[-1].right = curr_row[0]

        prev_row = curr_row
        
    #now we have most of a grid, but don't wrap on the verticals
    vwrap_needed = [((node.x,node.y),node) for node in nodes if node.up is None or node.down is None]
    
    for _,g in groupby(sorted(vwrap_needed),lambda t: t[0][0]):
        (top,bottom)= g
        top[1].up = bottom[1]
        bottom[1].down = top[1]

    return first_node


def str_to_grid(map_str):
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
    return input.split("\n\n")

def do_walk(current_node,instructions,grid):
    dirs = ['>','v','<','^']
    dir_idx = 0

    for instr in instructions:
        grid[current_node.zpos()] = dirs[dir_idx] 
        if instr in ['L','R']:
            change = 1 if instr == 'R' else -1
            dir_idx += change
            dir_idx = dir_idx%len(dirs)
        else:
            current_node = current_node.walk(dirs[dir_idx],instr)

    return current_node,dir_idx

def part_one(map_str,instructions_str):
    first_node = str_to_nodes(map_str)
    instructions = str_to_instructions(instructions_str)
    grid = str_to_grid(map_str)

    p1_end,p1_dir_idx = do_walk(first_node,instructions,grid) 

    grid[p1_end.zpos()] = '*'

    password = ((p1_end.y)* 1000) + ((p1_end.x)*4) + p1_dir_idx
    print_grid(grid)

    print(f"p1: {p1_end.pos()} {password}")


map_str,instructions_str = read_input()
part_one(map_str,instructions_str)

