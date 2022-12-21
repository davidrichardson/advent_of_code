from dataclasses import dataclass
HUMAN = 'humn'

@dataclass
class StaticMon():
    val: int
    def getVal(self): return self.val
    def rep(self): return str(self.val)
    def rev(self,c): return c
    def is_const(self): return isinstance(self.val, int)

@dataclass
class CalcMon():
    a: any
    b: any
    op: str

    def _calc(self,a,b):
        match self.op:
            case '+': x=a+b
            case '-': x=a-b
            case '*': x=a*b
            case '/': x=a/b
        return x

    def getVal(self):
        return self._calc(self.a.getVal(),self.b.getVal())
    
    def rep(self):
        if (self.is_const()):
            return str(self.getVal())
        else:
            return f"({self.a.rep()} {self.op} {self.b.rep()})"    

    def is_const(self): 
        return self.a.is_const() and self.b.is_const()

    def rev(self,c):
        if self.b.is_const():
            b = self.b.getVal()
            match self.op:
                case "+": # a+b=c
                    a = c-b  
                case "-": # a-b=c
                    a = c+b
                case "*": # a*b=c
                    a = c/b
                case "/": # a/b=c
                    a = c*b   
            return self.a.rev(a)
        if self.a.is_const():
            a = self.a.getVal()
            match self.op:
                case "+": # a+b=c
                    b = c - a
                case "-": # a-b=c
                    b = -1*(c - a)
                case "*": # a*b=c
                    b = c / a
                case "/": # a/b=c
                    b =  a / c         
            return self.b.rev(b)	
            
			
        

def monkeys():
    lookup = {}
    tofix = []

    for l in open(0).read().splitlines():
        toks = l.split(' ')
        id = toks[0].removesuffix(":")
        if len(toks)==2:
            lookup[id] = StaticMon(int(toks[1]))
        else:
            lookup[id] = CalcMon(toks[1],toks[3],toks[2])
            tofix.append(lookup[id])

    for m in tofix:
        m.a = lookup[m.a]
        m.b = lookup[m.b]

    return lookup

lookup =monkeys()
root = lookup['root']
print(f"part 1: {root.getVal()}")

human = lookup['humn']
human.val = 'x'
x = root.a.rev(root.b.getVal())
human.val= x
print(f"part 2: {human.val}")
