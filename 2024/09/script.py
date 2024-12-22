import sys
from dataclasses import dataclass

GAP = '.'
disk = []

def parse_input():
    line = next(sys.stdin).rstrip()
    id = 0
    for idx,size in enumerate(line):
        size = int(size)
        if idx % 2 == 1:
            disk.extend( [GAP]*size )
        else:
            disk.extend( [id]*size )
            id += 1

def print_disk(lpos=None,rpos=None):
    if len(disk) > 100:
        return
    
    if lpos is not None or rpos is not None:
        blah = [' ']*len(disk)
        if lpos is not None:        
            blah[lpos] = 'L'
        if rpos is not None:
            blah[rpos] = 'R'
        print(''.join([str(e) for e in blah]))    

    line = ''.join([str(e) for e in disk])
    print(line)

def find_next_gap(lpos):
    for i in range(lpos,len(disk)):
        if disk[i] == GAP:
            return i
    return None

def find_last_content(rpos):
    for i in range(rpos,-1,-1):
        if disk[i] != GAP:
            return i
    return None

def checksum():
    return sum((i*v for i,v in enumerate(disk) if v != GAP))

parse_input()
print_disk()

rpos = find_last_content(len(disk)-1)
lpos = find_next_gap(0)

while lpos is not None and rpos is not None:
    disk[lpos] = disk[rpos]
    disk[rpos] = GAP
    rpos = find_last_content(rpos)
    lpos = find_next_gap(lpos)
    if lpos >= rpos:
        break

print('p1',checksum())


