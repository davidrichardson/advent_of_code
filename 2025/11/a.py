import sys
from functools import cache

def parse_input():
    data = {}
    for line in sys.stdin.readlines():
        eles = line.rstrip().split(' ')
        key = eles[0][:-1]
        data[key] = eles[1:]
        
    return data

connections = parse_input()

@cache            
def count_paths_to_target(node,target):
    if node == target:
        return 1
        
    return sum(count_paths_to_target(n,target) for n in connections.get(node,[]) if (n in connections or n == target))


print('a)',count_paths_to_target('you','out'))

x = count_paths_to_target('svr','fft')
y = count_paths_to_target('fft','dac')
z = count_paths_to_target('dac','out')

print('b)',x*y*z)