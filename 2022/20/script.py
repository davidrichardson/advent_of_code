def mix(items, times = 1):
    new = []
    for i, v in enumerate(items):
        new.append((v, i))
    for _ in range(times):
        for i, v in enumerate(items):
            swap(new, (v, i))
    return list(map(lambda x:x[0], new))


def swap(items, e):
    i = items.index(e)
    val, _ = items.pop(i)
    ni = (i+val)%len(items)
    if ni == 0:
        items.append(e)
        return
    items.insert(ni, e)    

def output(mixed):
    o_pos = mixed.index(0)
    total = 0
    for x in range(1,4):
        coord = (o_pos+(x*1000))%len(mixed)
        total += mixed[coord]
    print(total)

input = [int(l) for l in open(0).read().splitlines()]

def p1():
    mixed = mix(input)  
    output(mixed)

def p2():
    key = 811589153
    decrypted_input = list(map(lambda x: x*key,input))
    mixed = mix(decrypted_input, 10)
    output(mixed)


p1()
p2()


