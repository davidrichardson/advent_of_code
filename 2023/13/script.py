import sys

parse = lambda : (chunk.split("\n") for chunk in sys.stdin.read().split("\n\n"))

def l_r(txt,rp):
    left = txt[:rp]
    right = txt[rp:]
    ref_len = min(len(left),len(right))
    left = left[-1*ref_len:]
    right = right[0:ref_len][::-1]
    return left,right

def is_reflection(txt,rp):
        left,right = l_r(txt,rp)
        return left==right

def vertical_reflection(layout):
    v_len = len(layout)
    h_len = len(layout[0])
    
    possible = range(1,h_len)
    for y in range(0,v_len):
        possible = [x for x in possible if is_reflection(layout[y],x)]
    
    if possible:
        return possible[0]
    else:
        return False

def transpose(layout):
    tl = list(zip(*layout))
    return [''.join(l) for l in tl]

def p1(layout):
    v_reflection = vertical_reflection(layout)

    if v_reflection:
        return v_reflection
 
    transposed_layout = transpose(layout)

    h_reflection = vertical_reflection(transposed_layout)

    return 100*h_reflection

def smudged_refl(txt):
    for rp in range(1,len(txt)):
        left,right = l_r(txt,rp)
        
        if left != right:
            left = "".join(left)
            right = "".join(right)
            if sum(1 for i in range(len(left)) if left[i] != right[i]) == 1:
                return rp
    return False

def p2(layout):
    v_reflection = smudged_refl(layout)

    if v_reflection:
        return v_reflection*100
 
    transposed_layout = transpose(layout)
    h_reflection = smudged_refl(transposed_layout)
    
    return h_reflection

p1_total = 0 
p2_total = 0

for layout in parse():
    p1_total += p1(layout)
    p2_total += p2(layout)

print(p1_total,p2_total)    