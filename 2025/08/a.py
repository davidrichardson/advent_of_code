import sys
from itertools import combinations
from math import sqrt, dist
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

def circuits_to_connect(jboxes: list[JBox]) -> int:
    if len(jboxes) < 1000:
        return 10
    else:
        return 1000


def answer_problems(jboxes: list[JBox], distances: list[Distance]) -> tuple:
    jbox_to_circuit: dict[JBox,Circuit] = {}
    circuits: set[Circuit]= set()

    for jbox in jboxes:
        c: Circuit= set()
        c.add(jbox)
        c = frozenset(c)
        jbox_to_circuit[jbox] = c
        circuits.add(c)    

    distances_to_use_for_a = circuits_to_connect(jboxes)
    a,b = None,None

    while len(circuits) > 1 and distances:
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

        distances_to_use_for_a -= 1
        if not distances_to_use_for_a:
            sorted_circuits = sorted(circuits,key=lambda a: len(a),reverse=True)
            a = reduce(mul, (len(c) for c in sorted_circuits[:3]), 1)
    
    b = jbox1[0] * jbox2[0] 

    return a,b


jboxes: list[JBox] = parse_input()
distances: list[Distance] = sorted([(dist(jbox1, jbox2),jbox1,jbox2) for jbox1, jbox2 in combinations(jboxes, 2)],reverse=True)

a,b = answer_problems(jboxes, distances)

print('a)',a)
print('b)',b)

