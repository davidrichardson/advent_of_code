import sys

w = 6
d = 3
l = 0
#A = rock
#B = paper
#C = sicssors
#X = lose
#Y = draw
#Z = win

opt = {
    'A':{"X":"C", "Y":"A", "Z":"B"},
    'B':{"X":"A", "Y":"B", "Z":"C"},
    'C':{"X":"B", "Y":"C", "Z":"A"},
}

choice = {'A':1,'B':2,'C':3}
round_score = {"X":l,"Y":d,"Z":w}

total = 0

for line in sys.stdin:
    opp = line[0]
    outcome = line[2]
    
    mine = opt[opp][outcome] 

    r = round_score[outcome]
    c = choice[mine]
    total += (r+c)
    print(f"{opp} {mine} {r} {c} {r+c} {total}")

print(total)