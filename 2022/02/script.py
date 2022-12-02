import sys

w = 6
d = 3
l = 0
#A|X = rock
#B|Y = paper
#C|Z = sicssors

round_outcome = {
    'A':{"X":d, "Y":w, "Z":l},
    'B':{"X":l, "Y":d, "Z":w},
    'C':{"X":w, "Y":l, "Z":d},
}

choice_bonus = {"X":1,"Y":2,"Z":3}

total = 0

for line in sys.stdin:
    opp = line[0]
    mine = line[2]
    r = round_outcome[opp][mine]
    c = choice_bonus[mine]
    total += (r+c)
    print(f"{opp} {mine} {r} {c} {r+c} {total}")

print(total)