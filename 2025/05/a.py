import sys

ranges = []
ids = []
ranges_done = False
for line in sys.stdin.readlines():
    line = line.rstrip()
    if line == '':
        ranges_done = True
        continue
    if not ranges_done:
        a,b = line.split('-')
        ranges.append( (int(a),int(b)) )
    else:
        ids.append(int(line))

ranges.sort()
ids.sort()

ranges_limit = len(ranges)
ridx = 0
fresh_ids = []

for id in ids:
    spoiled = False
    fresh = False
    while not spoiled and not fresh and ridx < ranges_limit:        
        if id >= ranges[ridx][0] and id <= ranges[ridx][1]:
            fresh = True
        elif id < ranges[ridx][0]:
            spoiled = True
        elif id > ranges[ridx][1]:
            ridx += 1

    if fresh:
        fresh_ids.append(id)

print('a)',len(fresh_ids))

merged_ranges = []

for i in range(len(ranges)):
    if i == 0:
        merged_ranges.append( ranges[i] )
    else:
        if ranges[i][0] <= merged_ranges[-1][1] + 1:
            merged_ranges[-1] = ( merged_ranges[-1][0], max(merged_ranges[-1][1], ranges[i][1]) )
        else:
            merged_ranges.append( ranges[i] )

b = sum(b-a+1 for a,b in merged_ranges)

print('b)', b)
  