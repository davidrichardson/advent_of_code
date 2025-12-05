import sys

def parse_input(lines):
    ranges = []
    ids = []
    ranges_done = False
    for line in lines:
        line = line.rstrip()
        if line == '':
            ranges_done = True
            continue
        if not ranges_done:
            a, b = line.split('-')
            ranges.append((int(a), int(b)))
        else:
            ids.append(int(line))
    return ranges, ids

def merge_ranges(ranges):
    merged_ranges = []

    for r in ranges:
        if not merged_ranges:
            merged_ranges.append( r )
        else:
            if r[0] <= merged_ranges[-1][1] + 1:
                merged_ranges[-1] = ( merged_ranges[-1][0], max(merged_ranges[-1][1], r[1]) )
            else:
                merged_ranges.append( r )
    return merged_ranges

def count_fresh_ids(ranges, ids):
    ranges_limit = len(ranges)
    ridx = 0
    fresh_count = 0

    for id in ids:
        spoiled = False
        fresh = False
        while not spoiled and not fresh and ridx < ranges_limit:        
            if id >= ranges[ridx][0] and id <= ranges[ridx][1]:
                fresh = True
                fresh_count += 1
            elif id < ranges[ridx][0]:
                spoiled = True
            elif id > ranges[ridx][1]:
                ridx += 1
    return fresh_count

ranges, ids = parse_input(sys.stdin.readlines())

ranges.sort()
ids.sort()

ranges = merge_ranges(ranges)

b_answer = sum(b-a+1 for a,b in ranges)
a_answer = count_fresh_ids(ranges, ids)


print('a)',a_answer)
print('b)',b_answer)
  