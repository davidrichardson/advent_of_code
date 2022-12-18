
def read_coords():
    return  [ (int(x),int(y),int(z)) for x,y,z in [l.split(",") for l in open(0).read().splitlines()]]

grid = set(read_coords())

def contact_points(pos):
    (x,y,z) = pos
    return  set([(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z),(x,y,z+1),(x,y,z-1)])
    
def part_one():
    count = 0
    for pos in grid:
        count +=  sum([1 for npos in contact_points(pos) if npos not in grid])
    print(count)

def faces_lava(pos):
    return any(npos in grid for npos in contact_points(pos))

def contact_point_faces_lava(pos):
    return any(faces_lava(npos) for npos in contact_points(pos))

def accessible(seen,border):
    if len(border)==0: return seen

    new_border = set()
    for pos in border:
        for npos in contact_points(pos) - seen - grid:
            if faces_lava(npos) or contact_point_faces_lava(npos):
                new_border.add(npos)
                
    return accessible(seen.union(border),new_border)

def count_touches_lava(pos):
    return sum(1 for npos in contact_points(pos) if npos in grid)

def part_two():
    (sx,sy,sz) = min(grid)
    exterior_start = (sx-1,sy,sz)
    exterior = accessible(set(),set([exterior_start]))
    out = sum(count_touches_lava(pos) for pos in exterior)
    print(out)

part_one()
part_two()