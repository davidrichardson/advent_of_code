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

def connected_pos(p: Position) -> list[Position]:
    return ( (p[0]+1, p[1]), (p[0]-1, p[1]), (p[0], p[1]+1), (p[0], p[1]-1) )

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

def number_of_sides(field: set[Position]) -> int:
    sides = set()

    for pos in field:
        for d,candidate in enumerate(connected_pos(pos)):
            if candidate not in field:
                if pos[0] == candidate[0]:
                    x = pos[0]
                else:
                    x = pos[1]
                sides.add((d,x))                 

    return len(sides)

grid = parse_input()

p1_total_price = 0
p2_total_price = 0

while grid:
    seed_pos,crop = grid.popitem()

    field = find_a_field(seed_pos,crop,grid)
    area = area_of_field(field)
    perimeter = perimeter_of_field(field)
    sides = number_of_sides(field)

    print(f'p1: Field {crop} has area {area} and perimiter {perimeter}. {area} * {perimeter} = {area*perimeter}')
    print(f'p2: Field {crop} has area {area} and sides {sides}. {area} * {sides} = {area*sides}')

    p1_total_price += (area * perimeter)
    p2_total_price += (area * sides)

print('p1',p1_total_price)
print('p2',p2_total_price)
