import sys
from collections import defaultdict, Counter
from itertools import cycle
from dataclasses import dataclass

OBSTRUCTION = '#'
DIRECTIONS = ['>','v','<','^']
VISITED = 'X'

@dataclass
class LabMap():
    lab_map: dict[tuple[int,int],str]
    dir_iter: list[str]
    dir: str = '^'
    pos: tuple[int,int] = (0,0)
    max_x: int = 0
    max_y: int = 0
    

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
        self.lab_map[self.pos] = VISITED
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


    def count_up(self):
        return Counter(self.lab_map.values())

    def init(self,lines):
        for y,line in enumerate(lines):
            self.max_y = y
            for x,c in enumerate(line.rstrip()):
                self.max_x = x
                if c == OBSTRUCTION:
                    self.lab_map[(y,x)] = OBSTRUCTION
                elif c == '^':
                    self.pos = (y,x)
                    self.dir = c

lab_map = LabMap(defaultdict(lambda: '.'),cycle(DIRECTIONS))
lab_map.init(sys.stdin)

while lab_map.on_map():
    lab_map.tick()

print('p1',lab_map.count_up()[VISITED])




