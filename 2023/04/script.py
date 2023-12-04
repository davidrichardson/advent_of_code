import sys
import re
from collections import defaultdict, Counter


def line_count(line: str) -> int:
    idx = line.find(':')
    
    
    
    numbers_pattern = re.compile('\d+')
    counter = Counter((m.group() for m in numbers_pattern.finditer(line[idx:])))
    count = sum(1 for c in counter.values() if c > 1)
    return count

    
def score_count(count: int) -> int:
    return 2**(count - 1)


total_score = 0
total_count = 0
counter = defaultdict(lambda: 1)

for idx,line in enumerate(sys.stdin):
    count = line_count(line)

    total_count = total_count + counter[idx]

    if count > 0:
        score = score_count(count)
        total_score = total_score + score

        for incr in range(1,count+1):
            i = idx + incr
            counter[i] = counter[i] + counter[idx]

print(total_score,total_count)        
