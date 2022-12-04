import sys
import collections

group_sets = [0,0,0]
total = 0

for idx,line in enumerate(sys.stdin):
    pos = idx%3
    group_sets[pos] = set()
    for c in line.rstrip():
        group_sets[pos].add(c)
    
    if pos == 2:
        common_item = group_sets[0].intersection(group_sets[1]).intersection(group_sets[2]).pop()
        item_ord = ord(common_item)
    
        priority_adjustment = 38 if (item_ord <97) else 96

        item_priority = item_ord - priority_adjustment
        print(f"{common_item} {item_priority}")
        total += item_priority

print(total)
