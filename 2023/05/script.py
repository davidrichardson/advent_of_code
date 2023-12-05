import sys
import re

number_pattern = re.compile("\d+")

seeds = None
buffers = []

for line in sys.stdin:

    if seeds is None:
        seeds = [int (m.group()) for m in number_pattern.finditer(line)]       
        next_buffer = {s:s for s in seeds}
        buffers.append(next_buffer)
    elif line == '\n':
        '''blank line'''        
    elif ':' in line:
        next_buffer = {v:v for v in buffers[-1].values()}
        buffers.append(next_buffer)
    else:
        dest,src,length = [int(m) for m in number_pattern.findall(line)]

        for k in buffers[-1]:
            if k >= src and k < src+length:
                diff = k - src
                buffers[-1][k] = dest+diff
    
        #print(buffers[-1])

lowest_loc = min(buffers[-1].values())  


for s in seeds:
    steps = [s]
    for b in buffers:
        steps.append( b[steps[-1]] )
    print(steps)

print(lowest_loc)