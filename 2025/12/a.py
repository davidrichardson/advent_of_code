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

impossible = 0
trivial = 0
maybe = 0

for r in regions:

    total_req = sum(m * shapes[i].filled_count() for i,m in enumerate(r.present_req))

    total_niners = sum(r.present_req)
    x9 = r.x_len // 3
    y9 = r.y_len // 3
    niner_space = x9 * y9

    if total_req > r.area():
        impossible += 1
    elif niner_space >= total_niners:
        trivial += 1
    else:
        maybe += 1

if maybe == 0:
    print("a)",trivial)
else:
    print(f"a is quite difficult, there are {trivial} with trivial solutions, {maybe} that would require more work")
        
            







shapes,regions = parse_input()