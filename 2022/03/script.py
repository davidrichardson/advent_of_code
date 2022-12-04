import sys
import collections

total = 0

for line in sys.stdin:
    line = line.rstrip()
    halfway = len(line)//2

    compA = set()
    compB = set()

    for idx,item in enumerate(line):
        comp = compA if idx < halfway else compB
        comp.add(item)

    common_item = compA.intersection(compB).pop()

    item_ord = ord(common_item)
    
    priority_adjustment = 38 if (item_ord <97) else 96

    item_priority = item_ord - priority_adjustment
    print(f"{common_item} {item_priority}")
    total += item_priority

print(total)
