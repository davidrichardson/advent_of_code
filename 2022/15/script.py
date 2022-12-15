import re
from dataclasses import dataclass

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
    accumulator = [ranges[0]]
    #relies on sorted ranges
    def reducer(acc,rg):
        head = acc[-1]
        if rg[0]<=head[1]+1:
            head[1] = max(head[1],rg[1])
        else:
            acc.append(rg)

    for r in ranges[1:]: reducer(accumulator,r)

    return accumulator


def phase_1(input):
    sensors = [to_sensor(sx,sy,bx,by) for sx,sy,bx,by in input]
    out = {}
    for y in [10,2000000]:
        rs = relevant_sensors(y,sensors)
        
        ranges = sorted([s.sense_xrange_at_y(y) for s in rs],key=lambda r:r[0])    
        ranges = merge_ranges(ranges)
        c = sum([r[1]-r[0] for r in ranges])
        out[y] = c
    return out


def phase_2(input):
    sensors = [to_sensor(sx,sy,bx,by) for sx,sy,bx,by in input]
    
    limit = 4000000 # should complete within this, but may as well use it

    for y in range(limit+1): 
        rs = relevant_sensors(y,sensors)
        
        sensor_ranges_in_row = sorted([s.sense_xrange_at_y(y) for s in rs],key=lambda r:r[0])    
        deduped_ranges = merge_ranges(sensor_ranges_in_row)
 
        if len(deduped_ranges)>1:
            #report the gap
            x = deduped_ranges[0][1]+1
            return [(x,y), (x*4000000)+y]
        
input = read_input()
print(phase_1(input))
print(phase_2(input))

