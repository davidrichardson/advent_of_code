import sys


def levels_diffs(levels: list[int]) -> list[int]:
    diffs = []

    for i in range(0,len(levels)-1):
        diff = levels[i+1] - levels[i]
        diffs.append(diff)

    return diffs

def is_safe(diffs: list[int]) -> bool:
    all_increasing = all(d > 0 for d in diffs)
    all_decreasing = all(d < 0 for d in diffs)
    all_in_range   = all(abs(d) <= 3 for d in diffs)

    safe = all_in_range and (all_increasing or all_decreasing)
    return safe

p1_counter = 0
p2_counter = 0

for l,line in enumerate(sys.stdin):
    line = line.rstrip()

    levels = [int(x) for x in  line.split(' ')]
    diffs = levels_diffs(levels)
    
   # print(l,'x',levels,is_safe(diffs))

    if is_safe(diffs):
        p1_counter += 1
        p2_counter +=1
    else:
        i = 0
        found_safe = False
        
        while i < len(levels) and not found_safe:
            spliced_levels = levels.copy()
            popped = spliced_levels.pop(i)
            spliced_diffs = levels_diffs(spliced_levels)
            found_safe = is_safe(spliced_diffs)
#            print(l,i,[popped],spliced_levels,found_safe)
            i += 1
        
        if found_safe:
            p2_counter += 1

print('part 1', p1_counter)
print('part 2', p2_counter)