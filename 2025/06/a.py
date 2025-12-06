import sys
from functools import reduce
from operator import mul,add

def parse_line_a(line):
    eles = line.split()
    if eles[0] in ('+','*'):
        return eles
    else:
        return [int(e) for e in eles]

def parse_input_a(lines):
    return [parse_line_a(line.rstrip()) for line in lines]    

def problem_answer(z):
    if z[-1] == '+':
        op = add
        i = 0
    else:
        op = mul
        i = 1
    return reduce(op, z[:-1], i)

def problem_total_a(data):
    return sum(problem_answer(z) for z in zip(*data))

def problem_total_b(data):
    return sum(problem_answer(z) for z in data)

def parse_input_b(lines):
    data_b = []
    op = None
    acc = []
    for x in zip(*lines):
        if x[-1] in ('+','*'):
            op = x[-1]
        l = ''.join(x[:-1]).strip()
        if l:
            acc.append(int(l))
        else:
            acc.append(op)
            data_b.append(acc)
            acc = []

    acc.append(op)
    data_b.append(acc)
    return data_b

lines = list(sys.stdin.readlines())

data_a = parse_input_a(lines)
print('a)',problem_total_a(data_a))

data_b = parse_input_b(lines)
print('b)',problem_total_b(data_b))
