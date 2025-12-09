import sys
from itertools import combinations
from typing import TypeAlias
from dataclasses import dataclass

Point: TypeAlias = tuple[int, int]

@dataclass
class Rectangle:
    min_x: int
    max_x: int
    min_y: int
    max_y: int

    @classmethod
    def fromPoints(cls, a: Point, b: Point) -> 'Rectangle':
        min_x = min(a[0], b[0])
        max_x = max(a[0], b[0])
        min_y = min(a[1], b[1])
        max_y = max(a[1], b[1])

        return cls(min_x, max_x, min_y, max_y)

@dataclass
class Line:
    min_x: int
    max_x: int
    min_y: int
    max_y: int


    @classmethod
    def fromPoints(cls, a: Point, b: Point) -> 'Line':
        min_x = min(a[0], b[0])
        max_x = max(a[0], b[0])
        min_y = min(a[1], b[1])
        max_y = max(a[1], b[1])

        return cls(min_x, max_x, min_y, max_y)

def area(a: Point,b: Point) -> int:
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)


def parse_input() -> list[Point]:
    return [tuple(map(int, line.rstrip().split(','))) for line in sys.stdin.readlines()]

def intersects(rect: Rectangle, line: Line) -> bool:
    
    if rect.max_x <= line.min_x or rect.min_x >= line.max_x:
        return False
    if rect.max_y <= line.min_y or rect.min_y >= line.max_y:
        return False
    
    return True

def display(coords,lines):
    data = {}
    max_x, max_y = 0,0
    min_x, min_y = float('inf'), float('inf')

    for x,y in coords:
        max_x = max(max_x, x)
        max_y = max(max_y, y)
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        data[(x,y)] = '#'
    
        
    for y in range(min_y-1, max_y+2):
        row = ''
        for x in range (min_x-1, max_x+2):
            if (x,y) in coords:
                row += '#'
            elif any(line.min_x <= x <= line.max_x and line.min_y <= y <= line.max_y for line in lines):
                row += '*'
            else:
                row += '.'
        print(row)


coords = parse_input()

a = max(area(a,b) for a,b in combinations(coords, 2))
print('a)',a)


lines = [Line.fromPoints(coords[i-1],coords[i]) for i in range(1,len(coords))]
lines.append(Line.fromPoints(coords[-1],coords[0]))

#display(coords,lines)

max_valid_area = 0

for a,b in combinations(coords, 2):
    rect_area = area(a,b)
    if rect_area <= max_valid_area:
        #no point, it can't be better than what we have
        continue

    rect = Rectangle.fromPoints(a,b)

    if any(intersects(rect, line) for line in lines):
        #intersects a line, not valid
        continue
    
    max_valid_area = rect_area

print('b)',max_valid_area)