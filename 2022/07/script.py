import sys
from dataclasses import dataclass
import collections
from typing import List

@dataclass
class File:
    name: str
    size: int

@dataclass
class Dir:
    name: str
    dirs: dict[str,any]
    files: list[File]
    parent: any = None
    _s: int = None 

    def size(self):
        if self._s is None:
            fs = sum(map(lambda f: f.size, self.files)) 
            ds = sum(map(lambda d: d.size(), self.dirs.values()))
            self._s = fs+ds
        return self._s
    

    def all_dirs(self):
        children = list(self.dirs.values())
        descendent_lists = [c.all_dirs() for c in children]
        descendents = [item for sublist in descendent_lists for item in sublist]
        
        return children+descendents

    
def ls(cwd: Dir,cmd_output: list[str]):
    for o in cmd_output:
        toks = o.split(" ")
        if toks[0] == "dir":
            cwd.dirs[toks[1]] = Dir(toks[1],{},[],cwd)
        else:
            cwd.files.append(File(toks[1],int(toks[0]))) 

root = Dir("/",{},[])
cwd = None

cmds_and_output = sys.stdin.read().split("$ ")

for c_and_o in cmds_and_output[1:]:
    c_and_o = c_and_o.splitlines()
    
    cmd = c_and_o[0].split(" ")

    match cmd[0]:
        case "cd":
            if (cmd[1] == "/"): cwd = root
            elif (cmd[1] == ".."): cwd = cwd.parent
            else: cwd = cwd.dirs[cmd[1]]
        case "ls":
            ls(cwd,c_and_o[1:])

total_under_limit = 0
for d in root.all_dirs():

    size = d.size()
    if (size <= 100000):
        total_under_limit += d.size()

print(f"Part 1 total: {total_under_limit}")

total_space = 70000000
space_required = 30000000
current_free = total_space - root.size()
minimum_to_free = space_required - current_free

dirs = sorted([d for d in root.all_dirs() if d.size() >= minimum_to_free],key=lambda d: d.size())

print(f"part 2: {dirs[0].name} {dirs[0].size()}")
