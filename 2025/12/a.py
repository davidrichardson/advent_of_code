import sys
from dataclasses import dataclass
from typing import TypeAlias
Point: TypeAlias = tuple[int, int]


@dataclass
class Shape:
    index: int
    filled: set[Point]
    
    def filled_count(self):
        return len(self.filled)

@dataclass
class Region:
    x_len: int
    y_len: int
    present_req: tuple[int]
    def area(self):
        return self.x_len * self.y_len

def parse_input():
    shapes = []
    regions = []

    s = None

    for line in sys.stdin.readlines():
        line = line.rstrip()

        if 'x' in line:
            chunks = line.split(' ')
            (x_len,y_len) = (int(d) for d in chunks[0][:-1].split('x'))
            present_req = tuple([int(d) for d in chunks[1:]])
            regions.append( Region(x_len,y_len,present_req))
        elif ':' in line:
            shapes.append( Shape(int(line[:-1]), set()) )
            s = 0
        elif not line:
            s = None
        else:
            for i,c in enumerate(line):
                if c == '#':
                    shapes[-1].filled.add( (i,s) )
            s += 1    
        
    return shapes,regions

shapes,regions = parse_input()
for s in shapes:
    print(s)

for r in regions:
    print(r)

    total_req = sum(m * shapes[i].filled_count() for i,m in enumerate(r.present_req))
    print(total_req,r.area())
            







shapes,regions = parse_input()