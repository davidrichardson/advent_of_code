import sys
import collections

def parse_layout(input:str):
    lines = input.splitlines()

    stacks = []
    for x in range((len(lines[0])+1)//4): stacks.append([])

    for l in lines:
        for idx, s in enumerate(stacks):
            crate = l[(idx * 4) + 1]
            if crate.isalpha(): 
                s.insert(0,crate)

    return stacks


def parse_move_line(ml:str):
    tokens = ml.split(" ")
    return (int(tokens[1]),int(tokens[3])-1,int(tokens[5])-1)


def read_top(stacks):
    return "".join( map(lambda s: s[-1], stacks) )


def move_9000(stacks,quant,src,targ):
    crates = stacks[src][quant * -1:]
    del stacks[src][quant * -1:]
    stacks[targ].extend(reversed(crates))


def move_9001(stacks,quant,src,targ):
    crates = stacks[src][quant * -1:]
    del stacks[src][quant * -1:]
    stacks[targ].extend(crates)


(layout_input,moves_input) = sys.stdin.read().split("\n\n")

stacks = parse_layout(layout_input)

for ml in moves_input.splitlines():
    (q,s,t) = parse_move_line(ml)
    move_9001(stacks,q,s,t)

print(read_top(stacks))
