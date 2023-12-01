import sys

match_1 = {str(x):x for x in range(1,10)}

def match(line:str,matches: dict[str,int],lengths: list[int]):
    for i in range(0,len(line)):
        for l in lengths:
            ss = line[i:i+l]
            if ss in matches:
                return matches[ss]


def part_1(line: str):
    lengths = [1]
    f = match(line,match_1,lengths)
    l = match(line[::-1],match_1,lengths)
    print(f,line,l)
    return combine(f,l)

        
    
def combine(f,l):
    return int(f"{f}{l}")

total_1 = 0
total_2 = 0

for line in sys.stdin:
    line = line.rstrip()
    total_1 = total_1 + part_1(line)

print(total_1,total_2)