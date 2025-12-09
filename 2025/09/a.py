import sys
from itertools import combinations

def parse_input():
    return [tuple(map(int, line.rstrip().split(','))) for line in sys.stdin.readlines()]

def area(a,b):
    return (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)


coords = parse_input()

a = max(area(a,b) for a,b in combinations(coords, 2))
print('a)',a)
    