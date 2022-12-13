

def comp(l,r):
    l_list = isinstance(l,list)
    r_list = isinstance(r,list)
    if (l_list and r_list):
        return comp_lists(l,r)
    elif (not l_list and not r_list):
        return comp_ints(l,r)
    else:
        l = l if l_list else [l]
        r = r if r_list else [r]
        return comp_lists(l,r)


def comp_ints(l,r):
    if l<r: return -1    
    if l>r: return 1
    if l==r: return 0


def comp_lists(l,r):
    for idx in range(min(len(l),len(r))):
        c = comp(l[idx],r[idx])
        if c != 0:
            return c
    d = len(l) - len(r)
    if d < 0: return -1
    if d > 0: return 1
    if d == 0: return 0


sum = 0

packets = []

for idx,chunk in enumerate(open(0).read().split("\n\n")):
    (left,right) = [eval(packet) for packet in chunk.split("\n")]
    o = comp(left,right)
    if o == -1:
        sum += idx+1
    packets.append(left)
    packets.append(right)
        
print(f"part 1: {sum}")

divider_packets = [ [[2]],[[6]] ] 
for dp in divider_packets: packets.append(dp)

from functools import cmp_to_key

packets.sort(key=cmp_to_key(comp))

m = 1
for dp in divider_packets:
    m *= (1 + packets.index(dp))

print(f"part 2: {m}")