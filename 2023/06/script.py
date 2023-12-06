import sys
import re
from functools import reduce
from math import sqrt

pattern = re.compile("\d+")

def read():
    return [line for line in sys.stdin]

def possibilities(time: int, distance: int) -> int:
    a = time - sqrt(time**2 - 4*distance)
    return int(2 * (time//2 - a//2) - (1 - time%2))

def part_one(lines):
    times = [int(m.group()) for m in pattern.finditer(lines[0])]
    distances = [int(m.group()) for m in pattern.finditer(lines[1])]

    valids =[possibilities(time,distances[idx])for idx,time in enumerate(times)]
            
    return reduce(lambda x, y: x*y, valids)

def part_two(lines):
    time = int(''.join([m.group() for m in pattern.finditer(lines[0])])) 
    distance = int(''.join([m.group() for m in pattern.finditer(lines[1])])) 

    return possibilities(time,distance)
    
lines = read()

print(part_one(lines),part_two(lines))