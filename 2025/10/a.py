import sys
from typing import TypeAlias
from dataclasses import dataclass
from itertools import count


Lights: TypeAlias = list[int]
Button: TypeAlias = list[int]
Joltage: TypeAlias = list[int]

@dataclass
class Machine:
    lights: Lights
    buttons: list[Button]
    joltage: Joltage

    def match_a(self,state: list[int]) -> bool:
        return all( self.lights[i] == state[i] for i in range(len(self.lights))) 
    
    def match_b(self,state: list[int]) -> bool:
        return all( self.joltage[i] == state[i] for i in range(len(self.joltage)))

    def still_under_joltage(self,state: list[int]) -> bool:
        return all( self.joltage[i] >= state[i] for i in range(len(self.joltage)) ) 

    def initial_state(self): 
        return [0] * len(self.lights)

def parse_input() -> list[Machine]:
    def light_mapper(c): 
        if c == '#':
            return 1
        else:
            return 0

    def button_mapper(chunk):
        return [int(c) for c in chunk[1:-1].split(',')]

    def line_to_machine(l):
        chunks = l.rstrip().split(' ')

        lights = [light_mapper(c) for c in chunks[0][1:-1]]
        buttons = [button_mapper(chunk) for chunk in chunks[1:-1]]
        joltage = button_mapper(chunks[-1])

        return Machine(lights,buttons,joltage)

    return [line_to_machine(l) for l in sys.stdin.readlines()]

def part_a_min_press(machine: Machine) -> int:
    state = [machine.initial_state()]

    state_seen = set()
    for c in count(1):
        new_state = set()

        for s in state:
            for b in machine.buttons:
                l = list(s)
                for p in b:
                    l[p] += 1
                    l[p] = l[p] % 2
                if machine.match_a(l):
                    return c
                l = tuple(l)
                if l not in state_seen:
                    new_state.add(l)
                    state_seen.add(l)

        state = new_state

    return -1

def part_b_min_press(machine: Machine) -> int:
    state = [machine.joltage]

    already_seen = set()
    
    for c in count(1):
        new_state = set()

        if c % 3 == 0:
            print(c,len(state))

        for s in state:
            for b in machine.buttons:
                j = list(s)
                under = False
                for p in b:
                    j[p] -= 1
                    if j[p] < 0:
                        under = True

                if not under and all(x == 0 for x in j):
                    return c
                j = tuple(j)
                if not under and j not in already_seen:
                    new_state.add(j)
                    already_seen.add(j)
                
        state = new_state

    return -1



machines = parse_input()

a = sum(part_a_min_press(m) for m in machines)
print('a)',a)

b = sum(part_b_min_press(m) for m in machines)
print('b)',b)