from dataclasses import dataclass
from functools import cache

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
        v.edges = frozenset([lookup[e] for e in v.edges])

    return lookup

@cache
def maxflow(loc,valves_opened,time_left=30):
    if time_left <= 0:
        return 0

    mf = 0
    if loc.id not in valves_opened:
        #valve at this loc has not been opened, can open it+move or just move
        val = (time_left - 1) * loc.flow
        new_opened = valves_opened + loc.id
        for adjacent in loc.edges:
            if val > 0:
                mf = max(mf, val+maxflow(adjacent,new_opened,time_left-2))
            mf = max(mf, maxflow(adjacent, valves_opened, time_left - 1))
    else:
        # just passing through
        for adjacent in loc.edges:
            mf = max(mf,maxflow(adjacent, valves_opened, time_left - 1))
    return mf

def part_one(valves_by_id):
    mf = maxflow(valves_by_id["AA"],"")
    print(mf)

valves_by_id = load_valves()
part_one(valves_by_id)
