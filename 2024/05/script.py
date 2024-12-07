import sys

order_rules: list[tuple[int,int]] = []

def parse_rule_line(line: str) -> tuple[int,int]:
    (a,b) = line.split('|')
    return (int(a),int(b))

def parse_print_line(line: str) -> list[int]:
    return [int(x) for x in line.split(',')]

def mid_point_value(print_order: list[int]) -> int:
    pos = int(len(print_order) / 2)
    return print_order[pos]

def to_print_order_lookup(print_order: list[int]) -> dict[int,int]:
    return {x:i for i,x in enumerate(print_order)}

def both_in(a:int,b:int,print_order_lookup: dict[int,int])-> bool:
    return a in print_order_lookup and b in print_order_lookup

def correct_order(a:int,b:int,print_order_lookup: dict[int,int])-> bool:
    return print_order_lookup[a] < print_order_lookup[b]

def rule_fails(a:int,b:int,print_order_lookup: dict[int,int])-> bool:
    return both_in(a,b,print_order_lookup) and not correct_order(a,b,print_order_lookup)

def failing_order_rules(print_order_lookup: dict[int,int]):
    return [(a,b) for a,b in order_rules if rule_fails(a,b,print_order_lookup)]

p1_counter = 0
p2_counter = 0

for line in sys.stdin:
    line = line.rstrip()

    if '|' in line:
        order_rules.append(parse_rule_line(line))
    elif line == '':
        continue
    else:
        print_order = parse_print_line(line)
        print_order_lookup = to_print_order_lookup(print_order)
        failing = failing_order_rules(print_order_lookup)

        if not failing:
            p1_counter += mid_point_value(print_order)
        else:
            while failing:
                a,b = failing[0]
                a_pos = print_order_lookup[a]
                b_pos = print_order_lookup[b]
                print_order_lookup[a] = b_pos
                print_order_lookup[b] = a_pos
                failing = failing_order_rules(print_order_lookup)

            for val,pos in print_order_lookup.items():
                print_order[pos] = val
            p2_counter += mid_point_value(print_order)
            

print(p1_counter,p2_counter)
