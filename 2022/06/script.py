import sys

def find_signal(l:str,size:int):
    for i in range(0,len(l)-size):
        uniq_chars = set(l[i:i+size])
        if (len(uniq_chars)==size): return i+size
    return None


for line in sys.stdin:
    p = find_signal(line,4)
    m = find_signal(line,14)
    print(f"{p} {m}")