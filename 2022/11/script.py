import sys
from dataclasses import dataclass,field
from typing import Callable

part_1 = True
logging = False

def log(txt_call):
    if(logging):
        print(txt_call())

@dataclass
class Monkey:
    id: int = -1
    items: list[int] = field(default_factory=lambda: [])
    test_divi: int = -1
    test_true_target: int = -1
    test_false_target: int = -1
    inspect_count: int = 0

    opc: Callable[[int],int] = lambda x: x

    def __repr__(self) -> str:
        return "\n".join([
            f"Monkey {self.id}:",
            f"\tItems: {self.items}",
            f"\tOperation: {self.opc}",
            f"\tTest: divisible by {self.test_divi}",
            f"\t\tIf true: throw to monkey {self.test_true_target}",
            f"\t\tIf false: throw to monkey {self.test_false_target}",
        ])

    def catch(self,item):
        self.items.append(item)

    def inspect_item(self,item,monkey,bored_fn):
        self.inspect_count += 1
        log(lambda: f"  Monkey inspects an item with a worry level of {item}")
        new_worry_level = self._do_op(item)
        log(lambda: f"     Worry level goes from {item} to {new_worry_level}")

        bored_now = bored_fn(new_worry_level)
        log(lambda: f"     Bored now. Worry level divided by 3 to {bored_now}")            
        
        is_divi = self._do_test(bored_now)
        log(lambda: f"     Current worry level dividible by {self.test_divi}: {is_divi}")
        target = self.test_true_target if is_divi else self.test_false_target
        log(lambda: f"     Item with worry level {bored_now} is thrown to monkey {target}")
        monkeys[target].catch(bored_now)

    def _do_op(self,old):
        return self.opc(old)

    def _do_test(self,wl):
        return (wl % self.test_divi) == 0

    def take_turn(self,monkeys,bored_fn):
        log(lambda: f"Monkey {self.id}:")
        for i in self.items:
            self.inspect_item(i,monkeys,bored_fn)
        self.items = []


def parse():
    monkeys = []
    m = None
    for line in sys.stdin.read().splitlines():
        if line.startswith("Monkey"):
            m = Monkey(id=len(monkeys))
            monkeys.append(m)
        elif line.startswith("  Starting items"):
            m.items = list(map(int,line.removeprefix("  Starting items: ").split(", ")))
        elif line.startswith("  Operation"):
            (_,op,b) = line.removeprefix("  Operation: new = ").split(" ")
            
            if (b=='old' and op =='*'):
                f = lambda x: x*x
            else:
                b = int(b)
                match op:
                    case '*': f = lambda x: x*b
                    case '+': f = lambda x: x+b
                    case '-': f = lambda x: x-b
                    case _: raise Exception(line)
            m.opc = f
        elif line.startswith("  Test"):
            m.test_divi = int(line.removeprefix("  Test: divisible by "))
        elif line.startswith("    If true"):
            m.test_true_target = int(line.split(" ")[-1])
        elif line.startswith("    If false"):
            m.test_false_target = int(line.split(" ")[-1])
        
    return monkeys

logging = False
part_1 = False
rounds = 10000

monkeys = parse()

for m in monkeys: log(lambda: str(m))

if (part_1):
    bored_fn = lambda x: x//3
else:
    mod = 1
    for m in monkeys:
        mod *= m.test_divi
    bored_fn = lambda x: x % mod

for round_idx in range(rounds):
    for m in monkeys:
        m.take_turn(monkeys,bored_fn)

for m in monkeys:
    print(f"Monkey {m.id}: {m.inspect_count}")

ics = sorted([m.inspect_count for m in monkeys],reverse=True)
print(ics[0]*ics[1])