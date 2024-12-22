import sys
from dataclasses import dataclass

disk = []

@dataclass
class File:
    id: int
    size: int
    trailing_space: int

def print_disk():
    if len(disk) > 100:
        return
    
    buffer = []

    for f in disk:
        buffer.append( str(f.id) * f.size)
        buffer.append( '.' * f.trailing_space)

    print(''.join(buffer))

def parse_input():
    line = next(sys.stdin).rstrip()
    id = 0
    for idx,size in enumerate(line):
        size = int(size)
        if idx % 2 == 1:
            disk[-1].trailing_space = size
        else:
            f = File(id,size,0)
            disk.append(f)
            id += 1

def checksum():
    total = 0
    pos = 0
    for f in disk:
        for _ in range(f.size):
            total += (pos * f.id)
            pos += 1

        pos += f.trailing_space

    return total 

parse_input()
work_list = list(reversed(disk))

def move_one(candidate):
    c_idx = disk.index(candidate)
    #print(f'Candidate {candidate.id} is at {c_idx}, size {candidate.size}')
    for idx in range(0,c_idx):
        t = disk[idx]
        if t.trailing_space >= candidate.size:
            #print(f'It fits after {t.id}')
            
            if c_idx > 0:
                before_candidate = disk[c_idx-1]
                before_candidate.trailing_space += (candidate.size + candidate.trailing_space)
                #print(f'{before_candidate.id} now has {before_candidate.trailing_space} trailing space')

            candidate.trailing_space = t.trailing_space - candidate.size
            t.trailing_space = 0
            disk.pop(c_idx)
            disk.insert(idx+1,candidate)            
            return True
    return False
            
print_disk()

for candidate in work_list:
    if move_one(candidate):
        print_disk()

print(checksum())
