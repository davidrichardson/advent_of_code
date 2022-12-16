from dataclasses import dataclass
from functools import cache
from collections import defaultdict 
from itertools import product


ROOT = None

@dataclass
class Valve():
    id: str
    flow: int
    edges: list[str]

    def __repr__(self):
        return f"Valve(id:{self.id} flow:{self.flow} edges:{','.join(self.edges)})"

    def __eq__(self,other):
        return self.id == other.id
    def __hash__(self):
        return self.id.__hash__()

def load_valves():
    lookup = {}
    for l in open(0).read().splitlines():
        tokens = l.split(" ")
        id = tokens[1]
        flow = int(tokens[4].removeprefix("rate=").removesuffix(";"))
        edges = [id.removesuffix(",") for id in tokens[9:]]
        lookup[id] = Valve(id,flow,edges)
    
    for v in lookup.values():
        v.edges = [lookup[e] for e in v.edges]
    return lookup


def make_distances(valves_by_id):
    dists = defaultdict(lambda: 100000)
    for v in valves_by_id.values():
        for e in v.edges:
            dists[(v.id,e.id)] = 1

    for k,i,j in product(valves_by_id.keys(),valves_by_id.keys(),valves_by_id.keys()):
        dists[(i,j)] = min(dists[(i,j)], dists[(i,k)] + dists[(k,j)])

    return dists

@cache
def maxflow(loc,valves_opened = frozenset(),time_left=30,elephant_available=False):
    mf = 0
    
    new_locs = [new_loc for new_loc in valves_by_id.values() if new_loc.id not in valves_opened and distances[(loc.id,new_loc.id)]<time_left]

    for new_loc in new_locs:
        cost = 1 + distances[(loc.id,new_loc.id)]
        flow_increase = new_loc.flow * (time_left - cost)
        new_opened = valves_opened.union( [new_loc.id])
        mf = max(mf, flow_increase + maxflow(new_loc,new_opened,time_left-cost,elephant_available))
    
    if elephant_available and len(new_locs)==0:
        mf = max(mf, maxflow(ROOT,valves_opened,26,False))

    return mf




valves_by_id = load_valves()
distances = make_distances(valves_by_id)
never_open = frozenset([key for key,valve in valves_by_id.items() if valve.flow == 0])
ROOT = valves_by_id["AA"]

def part_one():
    mf = maxflow(ROOT,never_open)
    print(f"1: {mf}")

def part_two():
    mf = maxflow(ROOT,never_open,26,True)
    print(f"2: {mf}")

part_one()
part_two()
