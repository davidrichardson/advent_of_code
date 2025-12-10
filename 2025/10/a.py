import sys
from typing import TypeAlias
from dataclasses import dataclass
from itertools import count
import numpy as np
from scipy.optimize import linprog

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
    
    def initial_state_a(self):
        return [False] * len(self.lights)
    
    def buttons_joltage(self):
        joltage_buttons = []
        for b in self.buttons:
            jb = [0] * len(self.lights)
            for x in b:
                jb[x] = 1
            joltage_buttons.append(jb)
        return joltage_buttons


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
    state = [machine.initial_state_a()]

    state_seen = set()
    for c in count(1):
        new_state = set()

        for s in state:
            for b in machine.buttons:
                l = list(s)
                
                for p in b:
                    l[p] = not l[p]

                if machine.match_a(l):
                    return c

                l = tuple(l)

                if l not in state_seen:
                    new_state.add(l)
                    state_seen.add(l)

        state = new_state

def part_b_min_press(machine: Machine) -> int:
    optimizer_c = [1] * len(machine.buttons)

    joltage_buttons = machine.buttons_joltage()

    return linprog(c=optimizer_c, A_eq=np.array(joltage_buttons).T, b_eq=machine.joltage, integrality=optimizer_c).fun

machines = parse_input()

a = sum(part_a_min_press(m) for m in machines)
print('a)',a)

b = int(sum(part_b_min_press(m) for m in machines))
print('b)',b)