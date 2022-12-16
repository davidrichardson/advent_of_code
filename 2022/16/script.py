from dataclasses import dataclass

@dataclass
class Valve():
    id: str
    flow: int
    edges: list[str]

    def __repr__(self):
        return f"Valve(id:{self.id} flow:{self.flow} edges:{','.join(self.edges)})"

def load_valves():
    lookup = {}
    for l in open(0).read().splitlines():
        tokens = l.split(" ")
        id = tokens[1]
        flow = int(tokens[4].removeprefix("rate=").removesuffix(";"))
        edges = [id.removesuffix(",") for id in tokens[9:]]
        lookup[id] = Valve(id,flow,edges)

    return lookup

valves_by_id = load_valves()
print(valves_by_id)