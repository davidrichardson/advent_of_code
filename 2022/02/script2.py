import sys

# A = rock,B = paper,C = sicssors
# X = lose,Y = draw,Z = win

choice_lookup = {
    'A':{"X":"C", "Y":"A", "Z":"B"},
    'B':{"X":"A", "Y":"B", "Z":"C"},
    'C':{"X":"B", "Y":"C", "Z":"A"},
}
choice_bonus = {'A':1,'B':2,'C':3}
round_score = {"X":0,"Y":3,"Z":6}

total = 0

for line in sys.stdin:
    opp = line[0]
    outcome = line[2]
    
    mine = choice_lookup[opp][outcome] 

    r = round_score[outcome]
    c = choice_bonus[mine]
    total += (r+c)
    print(f"{opp} {outcome} {mine} {r} {c} {r+c} {total}")

print(total)