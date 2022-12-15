import re
from dataclasses import dataclass
from collections import Counter
from functools import reduce
def read_input():
    return [list(map(int,re.findall(r"-?\d+",l))) for l in open(0).read().splitlines()]
        
                
@dataclass
class Sensor():
    x: int
    y: int
    radius: int
    min_y: int
    max_y: int

    def senses_row(self,y):
        return y >= self.min_y and y <= self.max_y

    def sense_xrange_at_y(self,y):
        dy = abs(self.y - y)
        dx = abs(dy - self.radius)                 
        return [self.x - dx, self.x+dx]

    def __repr__(self):
        return f"Sensor: ({self.x},{self.y}) r:{self.radius} y:{self.min_y}<->{self.max_y})"

def to_sensor(sx,sy,bx,by):
    r = abs(sx - bx) + abs ( sy - by)
    return Sensor(sx,sy,r,sy-r,sy+r)

def relevant_sensors(y,sensors):
    return [s for s in sensors if s.senses_row(y)]    

def merge_ranges(ranges):
    if (len(ranges)<2): return ranges

    accumulator = [ranges[0]]
    #relies on sorted ranges
    def reducer(rg):
        head = accumulator[-1]
        if rg[0]<=head[1]+1:
            head[1] = max(head[1],rg[1])
        else:
            accumulator.append(rg)

    for r in ranges[1:]: reducer(r)

    return accumulator


def phase_1():
    sensors = []

    sensors = [to_sensor(sx,sy,bx,by) for sx,sy,bx,by in read_input()]
 
    for y in [10,2000000]:
        rs = relevant_sensors(y,sensors)
        
        ranges = sorted([s.sense_xrange_at_y(y) for s in rs],key=lambda r:r[0])    
        ranges = merge_ranges(ranges)
        c = sum(map(lambda r: r[1]-r[0],ranges))
        print(f"{y} {c}")


def phase_2():
    sensors = []

    sensors = [to_sensor(sx,sy,bx,by) for sx,sy,bx,by in read_input()]
    
    limit = 4000000 # should complete within this, but may as well use it

    for y in range(limit+1): 
        rs = relevant_sensors(y,sensors)
        
        sensor_ranges_in_row = sorted([s.sense_xrange_at_y(y) for s in rs],key=lambda r:r[0])    
        deduped_ranges = merge_ranges(sensor_ranges_in_row)
 
        if len(deduped_ranges)>1:
            #report the gap
            x = deduped_ranges[0][1]+1
            print((x*4000000)+y)
            return (x,y)
        

print(phase_2())

