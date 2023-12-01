import sys

match_1 = {str(x):x for x in range(1,10)}
lengths_1 = [1]

digits = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
digits_r = {k[::-1]:v for k,v in digits.items()}

match_2 = match_1 | digits
match_2r = match_1 | digits_r
lengths_2 = [1,3,4,5]


def match(line:str,matches: dict[str,int],lengths: list[int]):
    for i in range(0,len(line)):
        for l in lengths:
            ss = line[i:i+l]
            if ss in matches:
                return matches[ss]
    return 0


def part_1(line: str):
    f = match(line,match_1,lengths_1)
    l = match(line[::-1],match_1,lengths_1)
    return combine(f,l)

def part_2(line: str):
    f = match(line,match_2,lengths_2)
    l = match(line[::-1],match_2r,lengths_2)
    return combine(f,l)
        
    
def combine(f,l):
    return int(f"{f}{l}")

total_1 = 0
total_2 = 0

for line in sys.stdin:
    line = line.rstrip()
    total_1 = total_1 + part_1(line)
    total_2 = total_2 + part_2(line)

print(total_1,total_2)