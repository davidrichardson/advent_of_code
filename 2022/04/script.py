import sys

def line_to_pair(l:str): return line.rstrip().split(",")

def pair_to_range(p:str): return list(map(int,p.split("-")))

def x_within_y(x,y):
    return (x[0]<=y[0] and x[1]>=y[1])

def x_overlaps_y(x,y):
    return (y[0] >= x[0] and y[0] <= x[1]) or (y[1] >= x[0] and y[1] <= x[1])

part_1_total = 0
part_2_total = 0

for line in sys.stdin:
    (a,b) = map(pair_to_range,line_to_pair(line))
    
    j = False
    k = False

    if x_within_y(a,b) or x_within_y(b,a):
        part_1_total += 1
        j = True

    if x_overlaps_y(a,b) or x_overlaps_y(b,a):
        part_2_total += 1
        k = True
    
    print(f"{a} {b} {j} {k}")


print(f"part 1: {part_1_total}")
print(f"part 2: {part_2_total}")
