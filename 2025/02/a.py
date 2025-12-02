import sys
from itertools import product

ranges = []

for line in sys.stdin:
    line = line.rstrip()
    chunks = line.split(',')
    for chunk in chunks:
        (a,b) = map(int,chunk.split('-'))
        ranges.append((a,b))

max_val = ranges[-1][1]
max_length = len(str(max_val))
max_repeat_length = max_length // 2

chars = list(map(str,range(0,10)))

sum_a = 0
sum_b = 0
seen_cache = set()

for l in range(1, max_repeat_length+1):

    max_reps = max_length // l

    for repeat_unit in product(chars,repeat=l):
        if repeat_unit[0] != '0':
            repeat_unit = ''.join(repeat_unit)

            for reps in range(2, max_reps+1):
                num = int(repeat_unit * reps)

                found = False
                
                for r in ranges:
                    if num >= r[0] and num <= r[1]:
                        found = True
                
                if found:
                    if reps == 2:
                        sum_a += num
                    if num not in seen_cache:
                        seen_cache.add(num)
                        sum_b += num


print('a)',sum_a)
print('b)',sum_b)
