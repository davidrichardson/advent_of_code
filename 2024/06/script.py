import sys
from collections import defaultdict
from itertools import cycle
from dataclasses import dataclass

OBSTRUCTION = '#'
DIRECTIONS = ['>','v','<','^']
VISITED = 'X'

@dataclass
class LabMap():
    lab_map: dict[tuple[int,int],str]
    dir_iter: list[str]
    visited: dict[tuple[int,int],set[str]]
    dir: str = '^'
    pos: tuple[int,int] = (0,0)
    max_x: int = 0
    max_y: int = 0
    in_loop: bool = False

    @classmethod
    def create(cls,lines: list[str]):
        lm = LabMap(
            lab_map=defaultdict(lambda: '.'),
            dir_iter=cycle(DIRECTIONS),
            visited=defaultdict(lambda: set())
        )
        lm._init(lines)
        return lm

    def print_map(self):
        lm = self.lab_map.copy()
        lm[self.pos] = self.dir

        for y in range(self.max_y+1):
            line = []
            for x in range(self.max_x+1):
                line.append(lm[(y,x)])
            print(''.join(line))

    def on_map(self):
        return self.pos[0] >= 0 and self.pos[0] <= self.max_y and self.pos[1] >= 0 and self.pos[1] <= self.max_x

    def tick(self):
        if self.dir in self.visited[self.pos]:
            self.in_loop = True

        self.visited[self.pos].add(self.dir)
        (next_y,next_x) = self.pos
        
        match self.dir:
            case '^':
                next_y -= 1
            case '>':
                next_x += 1
            case 'v':
                next_y += 1
            case '<':
                next_x -= 1
            case _:
                print(f'Dir: {dir} ???')
                exit()
        next_pos = (next_y,next_x)
    
        if self.lab_map[next_pos] == OBSTRUCTION:
            self.dir = next(self.dir_iter)
        else:
            self.pos = next_pos


    def count_visited(self):
        return len(self.visited.keys())

    def _init(self,lines):
        for y,line in enumerate(lines):
            self.max_y = y
            for x,c in enumerate(line.rstrip()):
                self.max_x = x
                if c == OBSTRUCTION:
                    self.lab_map[(y,x)] = OBSTRUCTION
                elif c == '^':
                    self.pos = (y,x)
                    self.dir = c

input = sys.stdin.readlines()
lab_map = LabMap.create(input)

while lab_map.on_map() and not lab_map.in_loop:
    lab_map.tick()

print('p1',lab_map.count_visited())

p2_counter = 0

for obstacle_point in lab_map.visited.keys():
    alt_lab_map = LabMap.create(input)
    alt_lab_map.lab_map[obstacle_point] = OBSTRUCTION
    
    while alt_lab_map.on_map() and not alt_lab_map.in_loop:
        alt_lab_map.tick()

    if alt_lab_map.in_loop:
        p2_counter += 1

print('p1',p2_counter)