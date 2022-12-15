sand_src = (500,0)

def read_input():
    draw_instructions = []
    for l in open(0).read().splitlines():
        line_instruction = []
        draw_instructions.append(line_instruction)
        for p in l.split(" -> "):
            (x,y) = list(map(int,p.split(",")))
            line_instruction.append( (x,y) )
        
    return draw_instructions      
    
def print_grid(g):
    for r in g:
        print("".join(r))

def draw_lines(draw_instructions):
    grid = {}
    for line_instruction in draw_instructions:
        draw_line(grid,line_instruction)
    return grid

def rock_point(grid,x,y):
    grid[(x,y)] = '#'

def sand_point(grid,x,y):
    grid[(x,y)] = 'o'

def sand_source(grid):
    grid[sand_src] = '+'

def draw_line(grid,line_instruction):
    (lp_x,lp_y) = line_instruction[0]
    rock_point(grid,lp_x,lp_y)
    for tp_x,tp_y in line_instruction[1:]:
        if (tp_x==lp_x):
            #vertical line
            for y in range(min(lp_y,tp_y),max(lp_y,tp_y)):
                rock_point(grid,lp_x,y+1)
        if(tp_y==lp_y):
            #horizontal line
            for x in range(min(lp_x,tp_x),max(lp_x,tp_x)):
                rock_point(grid,x+1,lp_y)
        rock_point(grid,tp_x,tp_y)
        lp_x = tp_x
        lp_y = tp_y


def min_max(items):
    return [min(items),max(items)]

def bounds(grid):
    xlim = min_max([x for x,_ in grid.keys()])
    ylim = min_max([y for _,y in grid.keys()])
    return (xlim,ylim)

def print_grid(grid):
    (xlim,ylim) = bounds(grid)
    for y in range(ylim[0],ylim[1]+1):
        row = [ grid[(x,y)] if (x,y) in grid else '.' for x in range(xlim[0],xlim[1]+1)]
        print("".join(row))

draw_instructions =  read_input()
grid = draw_lines(draw_instructions)

def phase_one(grid):
    step = 0
    (_,ylim) = bounds(grid) 

    fellout = False
    while not fellout:
        (x,y) = sand_src
        settled = False

        while not fellout and not settled:
            while (x,y+1) not in grid and y<ylim[1]:
                y += 1
        
            if (x,y+1) in grid:
                #diagonal left
                if (x-1,y+1) not in grid:
                    x -= 1
                    y += 1
                #diagonal right    
                elif (x+1,y+1) not in grid:
                    x += 1
                    y += 1
                else:
                    sand_point(grid,x,y)
                    step += 1
                    settled = True
            else:
                fellout = True
    return step

def phase_two(grid):
    step = 0
    
    (x_lim,y_lim) = bounds(grid)
    # I could try to model the infinite floor properly, or I could just hack this in:
    draw_line(grid,[ (x_lim[0]-y_lim[1],y_lim[1]+2),(x_lim[1]+y_lim[1],y_lim[1]+2) ])

    while sand_src not in grid:
        (x,y) = sand_src
        settled = False

        while sand_src not in grid and not settled:
            while (x,y+1) not in grid:
                y += 1
        
            if (x,y+1) in grid:
                #diagonal left
                if (x-1,y+1) not in grid:
                    x -= 1
                    y += 1
                #diagonal right    
                elif (x+1,y+1) not in grid:
                    x += 1
                    y += 1
                else:
                    sand_point(grid,x,y)
                    step += 1
                    settled = True
                
    return step   


step = phase_two(grid)

sand_source(grid)
#print_grid(grid)
print(step)



