import sys
from dataclasses import dataclass


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

def _blink(engraving,blinks):
    next_blink = blinks+1
    new_engravings = next_engravings(engraving)
    return [Stone(e,next_blink) for e in new_engravings]

@dataclass
class Stone:
    engraving: str
    blinks: int

    def blink(self) -> list:
        return _blink(self.engraving,self.blinks)


def parse_input():
    line = sys.stdin.readline().rstrip()
    stones = [Stone(chunk,0) for chunk in line.split(' ')]
    return stones


def stones_at_blink_point(blink_limit: int,stones) -> int: 
    stone_counter = 0

    while stones:
        stone = stones.pop()

        if stone.blinks == blink_limit:
            stone_counter += 1
        else:
            next_stones = stone.blink()
            stones.extend(next_stones)
    return stone_counter

stones = parse_input()
print('p1',stones_at_blink_point(25,stones.copy()))
print('p2',stones_at_blink_point(75,stones.copy()))