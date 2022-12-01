import sys

current_total = 0
elves = []

for line in sys.stdin:
    line = line.rstrip()

    if line == "":
        elves.append(current_total)
        current_total = 0
    else:
        current_total =+ int(line)

elves.append(current_total)
elves.sort(reverse=True)

print(f"max: {elves[0]}")
print(f"total for top 3: {sum(elves[0:3])}")
