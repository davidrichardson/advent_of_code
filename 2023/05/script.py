import sys
import re

number_pattern = re.compile("\d+")

lines = [line.rstrip() for line in sys.stdin if line != '\n']
seeds = [int (m.group()) for m in number_pattern.finditer(lines[0])]
lines = lines[1:]

def parse_map(line):
    dest,src,length = [int(m) for m in number_pattern.findall(line)]
    return dest,src,length

def part_one(seeds,lines):
    buffers = [{v:v for v in seeds}]
    
    for line in lines:
        if ':' in line:
            buffers.append({v:v for v in buffers[-1].values()})
        else:
            dest,src,length = parse_map(line)
            for k in buffers[-1]:
                if k >= src and k < src+length:
                    diff = k - src
                    buffers[-1][k] = dest+diff

    lowest_loc = min(buffers[-1].values())  
    return lowest_loc


def part_two(seeds,lines):
    instr = []
            
    for line in lines:
        if ':' in line:
            instr.append([])
        else:
            dest,src,length = parse_map(line)
            src_start,src_end = src,src+length-1
            instr[-1].append((src_start,src_end,dest))


    seed_ranges = [(seeds[i],seeds[i]+seeds[i+1]-1) for i in range(0,len(seeds),2)]
    buffers = [[sr for sr in seed_ranges]]

    for block in instr:
        next_buffer = []
        
        block = sorted(block)
         
        for curr_start,curr_end in buffers[-1]:
             
            first_uncovered = curr_start

            for src_start,src_end,dest_start in block:
                if (curr_start <= src_end) and (src_start <= curr_end):
                        overlap_start = max(src_start,curr_start)
                        overlap_end = min(src_end,curr_end)

                        diff = dest_start - src_start

                        if first_uncovered < overlap_start:
                         #   print("not overlapped: ",(first_uncovered,overlap_start-1))
                            next_buffer.append((first_uncovered,overlap_start-1))

                      #  print("overlapped: ",(overlap_start,overlap_end),'->',(overlap_start+diff,overlap_end+diff),src_start,src_end,dest,diff)
                        next_buffer.append((overlap_start+diff,overlap_end+diff))                
                        
                        first_uncovered = overlap_end+1

            if first_uncovered <= curr_end:
#                print("not overlapped: ",(first_uncovered,curr_end))
                next_buffer.append((first_uncovered,curr_end))

        buffers.append(next_buffer)
                
    
    lowest_loc = min(v[0] for v in buffers[-1])

    return lowest_loc

print(part_one(seeds,lines),part_two(seeds,lines))