import sys
from collections import defaultdict

def next_engravings(engraving: str) -> list[str]:
    #rule 1 - if the engrtaving is 0, add 1
    if engraving == '0':
        return ['1']

    #rule 2 - if the number of digits is even, split into two
    engraving_length = len(engraving) 
    if engraving_length % 2 == 0:
        mid_point = engraving_length // 2
        return [str(int(e)) for e in (engraving[:mid_point],engraving[mid_point:])]
        
    #rule 3 - otherwise, multiply by 2024
    v = int(engraving) * 2024
    return [str(v)]

def parse_input():
    line = sys.stdin.readline().rstrip()
    stones = {chunk:1 for chunk in line.split(' ')}
    return stones

def update(stones: dict[str,int]):
    new_stones = defaultdict(lambda: 0)
    for engraving,count in stones.items():
        for new_engraving in next_engravings(engraving):
            new_stones[new_engraving] += count
    return new_stones

stones = parse_input()

for _ in range(1000):
    stones = update(stones)

print(sum(stones.values()))