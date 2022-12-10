import sys

x = 1
cycle = 1

report = {}

grid = [[" "] * 40 for i in range(6)]

def show_grid():
    for r in grid:
        print("".join(r))


def maybe_report(line):
    if cycle in [20, 60, 100, 140, 180, 220]:
        report[cycle] = x

    sprite = [x-1,x,x+1]
    if (cycle - 1) % 40 in sprite:
        row = (cycle-1) // 40
        col = (cycle-1)% 40
        grid[row][col] = '▓'

for line in sys.stdin.read().splitlines():
    cycle += 1
    maybe_report(line)
    
    match line[0:4]:
        case 'noop':
            ...
        case 'addx':
            x += int(line[5:])
            cycle += 1
            maybe_report(line)

        case _:
            raise Exception(line)


print(report)
print(f"{x} after {cycle} cycles")

ss = sum([k*v for k,v in report.items()])
print(ss)

show_grid()