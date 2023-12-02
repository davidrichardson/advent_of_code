import sys
from functools import reduce

green_limit = 13
blue_limit = 14
red_limit = 12

limits = {'green': green_limit,'blue': blue_limit,'red': red_limit}


def parse_rev(rev: str):
    reveal = {}
    
    for e in rev.split(','):
        v,k = e.strip().split(' ')
        reveal[k] = int(v)

    return reveal

def parse_line(line: str) -> tuple[int,list[dict[str,int]]]:
    id,revs = line.split(':')

    _,id = id.split(' ')
    reveals = [parse_rev(x) for x in revs.split(";")]

    return (int(id),reveals)

def in_limits(reveal: dict[str,int]) -> bool:
    return all( [reveal.get(c,0) <= limits[c] for c in limits.keys()] )

def max_per_colour(reveals: list[dict[str,int]]) -> dict[str,int]:
    maxc = {c:0 for c in limits.keys()}
    
    for r in reveals:
        for k,v in r.items():
            if v > maxc[k]:
                maxc[k] = v

    return maxc

def power(maxc: dict[str,int]) -> int:
    return reduce(lambda x, y: x*y, maxc.values())

part_1_total = 0
part_2_sum = 0

for line in sys.stdin:
    id,reveals = parse_line(line)

    if all([in_limits(r) for r in reveals]):
        part_1_total = part_1_total + id

    p = power(max_per_colour(reveals))
    part_2_sum = part_2_sum + p

print(part_1_total,part_2_sum)