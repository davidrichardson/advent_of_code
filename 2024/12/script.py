import sys
Position = tuple[int,int] #x,y
Crop = str # single char

def parse_input() -> dict[Position,Crop]:
    grid: dict[Position,Crop] = {}
    for y,line in enumerate(sys.stdin):
        for x,crop in enumerate(line.rstrip()):
            position: Position = (x,y)
            grid[position] = crop
    return grid

def east(p: Position) -> Position: return (p[0]+1, p[1])
def west(p: Position) -> Position: return (p[0]-1, p[1])
def north(p: Position) -> Position: return (p[0], p[1]-1)
def south(p: Position) -> Position: return (p[0], p[1]+1)

def ne(p: Position) -> Position: return (p[0]+1, p[1]-1)
def se(p: Position) -> Position: return (p[0]+1, p[1]+1)
def nw(p: Position) -> Position: return (p[0]-1, p[1]-1)
def sw(p: Position) -> Position: return (p[0]-1, p[1]+1)

def connected_pos(p: Position) -> list[Position]:
    return ( east(p), west(p), south(p), north(p) )

def corner_nonsense(p: Position):
    return [
        (p,north(p),east(p),ne(p)),
        (p,north(p),west(p),nw(p)),
        (p,south(p),east(p),se(p)),
        (p,south(p),west(p),sw(p))
    ]

def cornering(grid,p: Position):
    c = lambda x: grid.get(x)
    return [list(map(c,t)) for t in corner_nonsense(p)] 

def find_a_field(pos,crop,grid) -> set[Position]:
    field = set([pos])
    for candidate in connected_pos(pos):
        if candidate in grid and grid[candidate] == crop:
            del grid[candidate]
            connected_elements = find_a_field(candidate,crop,grid)
            field.update(connected_elements)
    return field

def area_of_field(field: set[Position]) -> int:
    return len(field)

def perimeter_of_field(field: set[Position]) -> int:
    perimiter = 0
    for pos in field:
        exposed = sum(1 for candidate in connected_pos(pos) if candidate not in field)
        perimiter += exposed
    return perimiter

def number_of_corners(grid,field: set[Position]) -> int:
    corners = 0
    
    for pos in field:
        for (target,side1,side2,corner) in cornering(grid,pos):
            if ((target != side1 and target != side2) or
               (side1 == target and side2 == target and corner != target)):
                corners +=1
      
    
    return corners

ref_grid = parse_input()
grid  = ref_grid.copy()
p1_total_price = 0
p2_total_price = 0

while grid:
    seed_pos,crop = grid.popitem()

    field = find_a_field(seed_pos,crop,grid)
    area = area_of_field(field)
    perimeter = perimeter_of_field(field)
    sides = number_of_corners(ref_grid,field)

    print(f'p1: Field {crop} has area {area} and perimiter {perimeter}. {area} * {perimeter} = {area*perimeter}')
    print(f'p2: Field {crop} has area {area} and sides {sides}. {area} * {sides} = {area*sides}')

    p1_total_price += (area * perimeter)
    p2_total_price += (area * sides)

print('p1',p1_total_price)
print('p2',p2_total_price)

