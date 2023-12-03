import sys
import re

def parse_and_pad():
    schematic = []
    line_length = None

    for line in sys.stdin:
        line = line.rstrip()
        line = '.'+line+'.'
        if line_length is None:
            line_length = len(line)
            schematic.append( '.'*line_length)
        schematic.append(line)
    schematic.append( '.'*line_length)
    return schematic

schematic = schematic = parse_and_pad()
part_numbers = []
gears = {}

digit_pattern = re.compile("\d+")

for idy,line in enumerate(schematic):

    y_start = idy-1
    y_end = idy+1

    for m in digit_pattern.finditer(line):
        x_start = m.start()-1
        x_end =  m.start()+len(m.group())

        part_number = int(m.group())        


        coords = ((y,x) for x in range(x_start,x_end+1) for y in range(y_start,y_end+1))
        
        matched = False
        for y,x in coords:
            c = schematic[y][x]

            if not(c.isnumeric() or c == '.'):
               matched = True

            if c == '*':
                if (y,x) not in gears:
                    gears[(y,x)] = []
                gears[(y,x)].append(part_number) 

        if matched:
            part_numbers.append(part_number)


gear_sum = sum([g[0] * g[1] for g in gears.values() if len(g) == 2])
part_number_sum = sum(part_numbers)


print(part_number_sum,gear_sum)
