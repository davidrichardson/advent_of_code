import sys


grid = []

for line in sys.stdin:
    grid.append(line.rstrip())


line_length = len(grid[0])
line_count = len(grid)
#y,x diffs
east = [ (0,1),(0,2),(0,3) ] 
west = [ (0,-1),(0,-2),(0,-3) ]
south = [ (1,0),(2,0),(3,0) ]
north = [ (-1,0),(-2,0),(-3,0)]
ne = [ (-1,1),(-2,2),(-3,3)]
nw = [ (-1,-1),(-2,-2),(-3,-3)]
se = [ (1,1),(2,2),(3,3)]
sw = [ (1,-1),(2,-2),(3,-3)]


def get_one_letter(start_y,start_x,dy,dx):
    y = start_y + dy
    x = start_x + dx
    if y < 0 or x < 0 or y >= line_count or x >= line_length:
        return '.'
    else:
        return grid[y][x]

def word(start_y,start_x,lookup):
    letters = [get_one_letter(start_y,start_x,dy,dx) for dy,dx in lookup]
    return ''.join(letters)

def xmas_words(start_y,start_x,patterns):
    for p in patterns:
        yield word(start_y,start_x,p)
         
def words_starting_at_coords(coords,patterns):
    for start_y,start_x in coords:
        for w in xmas_words(start_y,start_x,patterns):
            yield w

p1_patterns = [east,west,north,south,ne,nw,se,sw]
coords_of_x = ((y,x) for x in range(line_length) for y in range(line_count) if grid[y][x] == 'X')
p1_count = sum(1 for w in words_starting_at_coords(coords_of_x,p1_patterns) if w == 'MAS')
    
print(p1_count)

p2_patterns = [[(-1,-1),(-1,1),(1,-1),(1,1)]]

targets = set(['MSMS','MMSS','SMSM','SSMM'])
coords_of_a = ((y,x) for x in range(line_length) for y in range(line_count) if grid[y][x] == 'A')
p2_count = sum(1 for w in words_starting_at_coords(coords_of_a,p2_patterns) if w in targets)
print(p2_count)
