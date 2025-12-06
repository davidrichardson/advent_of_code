import sys

moves = {
    '^': (0,1),
    'v': (0,-1),
    '>': (1,0),
    '<': (-1,0)
}

def read_instructions():
    instr = []
    for l in sys.stdin.readlines():
        for i in l:
            if i in moves:
                instr.append(i)
    return instr

def move(instructions,tracker):
    pos = (0,0)
    tracker.add(pos)

    for instr in instructions:
        m = moves[instr]
        pos = (pos[0]+m[0], pos[1]+m[1])
        tracker.add(pos)

    return tracker

instructions = read_instructions()            

print('a)', len(move(instructions,set())))

santa_instructions = list(i for idx,i in enumerate(instructions) if idx % 2 == 0)
robo_instructions = list(i for idx,i in enumerate(instructions) if idx % 2 == 1)

tracker = move(santa_instructions,set())
tracker = move(robo_instructions,tracker)

print('b)', len(tracker))