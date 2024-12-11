import sys
from dataclasses import dataclass

@dataclass
class File():
    id: int
    size: int
    @property
    def rep(self) -> str:
        return str(self.id)

@dataclass
class Gap():
    size: int

    @property
    def rep(self):
        return '.'
disk = []

def parse_input():
    line = next(sys.stdin).rstrip()

    id = 0
    for idx,size in enumerate(line):
        size = int(size)
        if idx % 2 == 1:
            disk.append( Gap(size) )
        else:
            disk.append( File(id,size))
            id += 1

def print_disk():
    line = ''.join([element.rep * element.size for element in disk])
    print(line)

parse_input()
print_disk()

while disk:
    ele = disk.pop()
    if isinstance(ele,File):
        for idx,e in enumerate(disk):
            if isinstance(e,Gap) and ele.size <= e.size:
                print(e)
                
    print_disk()