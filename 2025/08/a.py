import sys
from itertools import combinations
from math import sqrt
from operator import mul
from functools import reduce
from typing import TypeAlias

JBox: TypeAlias = tuple[int, int, int]
Circuit: TypeAlias = set[JBox]
Distance: TypeAlias = tuple[float, JBox, JBox]

def parse_input() -> list[JBox]:
    jboxes = []
    for line in sys.stdin.readlines():
        x,y,z = line.rstrip().split(',')
        jboxes.append( (int(x),int(y),int(z)) )
    return jboxes

def distance(jbox1: JBox, jbox2: JBox) -> Distance:
    return (sqrt(sum(abs(a - b)**2 for a, b in zip(jbox1, jbox2))), jbox1, jbox2)

def circuits_to_connect(jboxes: list[JBox]) -> int:
    if len(jboxes) < 1000:
        return 10
    else:
        return 1000

def part_a(jboxes: list[JBox],distances: list[Distance]) -> int:
    jbox_to_circuit: dict[JBox,Circuit] = {}
    
    for jbox in jboxes:
        c: Circuit= set()
        c.add(jbox)
        jbox_to_circuit[jbox] = { jbox:c }
    
    for dist,jbox1,jbox2 in distances[:circuits_to_connect(jboxes)]:
        c1 = jbox_to_circuit[jbox1] 
        c2 = jbox_to_circuit[jbox2]

        if c1 is not c2:
            for b in c2:
                jbox_to_circuit[b] = c1
            c1.update(c2)
    
    circuits = set()
    for c in jbox_to_circuit.values():
        circuits.add( frozenset(c) )

    circuits = sorted(circuits,key=lambda a: len(a),reverse=True)

    return reduce(mul, (len(c) for c in circuits[:3]), 1)

def part_b(jboxes: list[JBox],distances: list[Distance]) -> int:
    jbox_to_circuit: dict[JBox,Circuit] = {}
    circuits: set[Circuit]= set()

    for jbox in jboxes:
        c: Circuit= set()
        c.add(jbox)
        c = frozenset(c)
        jbox_to_circuit[jbox] = c
        circuits.add(c)    

    while len(circuits) > 1:
        (_,jbox1,jbox2) = distances.pop()
        
        c1 = jbox_to_circuit[jbox1] 
        c2 = jbox_to_circuit[jbox2]

        if c1 is not c2:
            c3 = frozenset().union(c1,c2)
            for jb in c3:
                jbox_to_circuit[jb] = c3
            
            circuits.remove(c1) 
            circuits.remove(c2)
            circuits.add(c3)
    
    return jbox1[0] * jbox2[0] 

jboxes: list[JBox] = parse_input()
distances = sorted([distance(jbox1, jbox2) for jbox1, jbox2 in combinations(jboxes, 2)])
rev_distances = list(reversed(distances))

print('a)',part_a(jboxes,distances))
print('b)',part_b(jboxes,rev_distances))
