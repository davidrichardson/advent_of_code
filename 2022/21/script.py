from dataclasses import dataclass
from operator import add, sub, mul, truediv
HUMAN = 'humn'

@dataclass
class StaticMon():
    id: str
    val: int
    def getVal(self): return self.val
    def rep(self): return str(self.val)
    def rev(self,c):  
        self.val = c
        return c
    def is_const(self): return isinstance(self.val, int)
        

@dataclass
class CalcMon():
    id: str
    a: any
    b: any
    func: any
    revfunc: any
    op: str

    def getVal(self):
        return self.func(self.a.getVal(),self.b.getVal())
    
    def rep(self):
        if (self.is_const()):
            return str(self.getVal())
        else:
            return f"({self.a.rep()} {self.op} {self.b.rep()})"    

    def is_const(self): 
        return self.a.is_const() and self.b.is_const()

    def rev(self,c):
        (m,n) = (self.a,self.b)


        if n.is_const():
            (m,n) = (self.b,self.a)

        o = self.revfunc(c,m.getVal())
        
        x = n.rev(o)
        
        return x 
        

def monkeys():
    lookup = {}
    tofix = []

    for l in open(0).read().splitlines():
        toks = l.split(' ')
        id = toks[0].removesuffix(":")
        if len(toks)==2:
            lookup[id] = StaticMon(id,int(toks[1]))
        else:
            a = toks[1]
            b = toks[3]
            
            match toks[2]:
                case '+':
                    f = add
                    r = sub 
                case '-':
                    f = sub
                    r = add
                case '*': 
                    f = mul
                    r = truediv
                case '/':
                    f = truediv
                    r = mul
            lookup[id] = CalcMon(id,a,b,f,r,toks[2])
            tofix.append(lookup[id])

    for m in tofix:
        m.a = lookup[m.a]
        m.b = lookup[m.b]
    return lookup


lookup =monkeys()
root = lookup['root']
print(f"part 1: {root.getVal()}")

human = lookup['humn']
human.val = HUMAN
x = root.a.rev(root.b.getVal())
print(f"part 2: {human.val}")
print(root.a.getVal())
print(root.b.getVal())