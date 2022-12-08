import sys
from dataclasses import dataclass,field

#dirs
(l,t,r,b) = [0,1,2,3]

@dataclass
class Tree:
    height: int
    max_height: list[int] = field(default_factory=lambda: [-1]*4)

    def max_for_dir(self,dir):
        return max(self.height,self.max_height[dir])

    def dirs_visible(self):
        return [mh<self.height for mh in self.max_height]

    def is_visible(self):
        return any(self.dirs_visible())
        
    def update_from_adjacent(self,at,dir):
            self.max_height[dir] = at.max_for_dir(dir)


    def __repr__(self):
        return f"(h:{self.height} mh:{str(self.max_height)}]"


grid = []


#build the grid from left to right, top to bottom
for y,line in enumerate(sys.stdin):
    row = []
    grid.append(row)

    for x,h in enumerate(line.rstrip()):
        tree = Tree(int(h))
        row.append(tree)

        if y > 0: tree.update_from_adjacent(grid[y-1][x],t)           
        
        if x > 0: tree.update_from_adjacent(grid[y][x-1],l)           
        

total_visible = 0

max_y = len(grid)-1
max_x = len(grid[0])-1

best_ss = 0

for y,row in reversed(list(enumerate(grid))):
    for x,tree in reversed(list(enumerate(row))):
        if y < max_y:
            tree.update_from_adjacent(grid[y+1][x],b)

        if x < max_x:
            tree.update_from_adjacent(grid[y][x+1],r)

        if tree.is_visible():
            total_visible += 1
        

print(f"total visible: {total_visible}")