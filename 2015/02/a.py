import sys

a = 0
b = 0
for l in sys.stdin.readlines():
    l,w,h = sorted([int(x) for x in l.rstrip().split('x')])
    sides = [l*w,w*h,h*l]
    
    bow = l*w*h
    perim = 2*(l+w)
    a += min(sides) + (2 * sum(sides))
    b += bow+perim


print('a)', a)
print('b)', b)