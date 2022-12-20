import re
import multiprocessing as mp 
from collections import defaultdict
from functools import cache

(ORE,CLAY,OBSIDIAN,GEODE) = (0,1,2,3)

def read_input():
    pattern = r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."
    blueprints={}
    for l in open(0).read().splitlines():
        (b_id,or_cost,cl_cost,ob_o_cost,ob_c_cost,g_or_cost,g_ob_cost) = [int(x) for x in re.search(pattern,l).groups()]
        blueprints[b_id] = ( 
            (or_cost,0,0,0),
            (cl_cost,0,0,0),
            (ob_o_cost,ob_c_cost,0,0),
            (g_or_cost,0,g_ob_cost,0)
        )            
        
    return blueprints

def subcost(r,c):
    return tuple([r[i] - c[i] for i in range(4)])

def add_bot(bots,nb):
    return tuple([b+1 if i==nb else b for i,b in enumerate(bots) ])

def mine(t,resources,bots): return tuple([resources[i] + (bot*t) for i,bot in enumerate(bots)])


def max_res_utilisation(blueprint,res):
    return max([p[res] for p in blueprint])

def time_to_buildable(cost,resources,bots):
    after_paying = subcost(resources,cost)
    worst_time = 0

    for i,v in enumerate(after_paying):
        if v<0:
            if bots[i] == 0: return None
            worst_time = max(worst_time,((v*-1)//bots[i])+1)

    return worst_time


BEST = defaultdict(lambda:0)

def maxgeodes(blueprint,tl,resources,bots, buildorder=[], seen=set()):

    if (tl == 0):
        if BEST[blueprint]<resources[GEODE]:
            print((resources[GEODE],buildorder))
        BEST[blueprint] = max(BEST[blueprint],resources[GEODE])
        return (resources[GEODE],buildorder)


    if (BEST[blueprint]>=best_achievable_in_time(tl,resources,bots)):
        return 0,set()

    #what should we build next?
    mg = 0
    nbo = None

    for i in range(4):
        tb = time_to_buildable(blueprint[i],resources,bots)
        buildable  = tb is not None and tb < tl
        #enough_ore_bots = i != 0 or bots[1] < 3
        have_max_usable = i != GEODE and bots[i]>=max_res_utilisation(blueprint,i)

        
        if buildable and not have_max_usable:

            new_resources = subcost(mine(tb+1,resources,bots),blueprint[i])

            new_bots = add_bot(bots,i)
            new_build_order = buildorder + (([9])*tb) + [i]

            novel = (tl-tb-1,new_resources,new_bots) not in seen

            if novel:
                (nmg,bo) = maxgeodes(blueprint,tl-tb-1,new_resources,new_bots,new_build_order,seen)
                if nmg>mg:
                    mg = nmg
                    nbo = bo
    seen.add((tl,resources,bots))    

    return (mg,nbo)


def best_achievable_in_time(t,resources,bots,i=GEODE):
    now = resources[i]
    from_current_bots = t*bots[i]
    only_new_geode_bots = sum(z for z in range(t+1))
    return now + from_current_bots + only_new_geode_bots


blueprints = read_input()

def p1(tup):
    (bid,b) = tup
    resources = (0,0,0,0)
    bots = (1,0,0,0)
    g,bo = maxgeodes(b,24,resources,bots)
    
    print([bid,g,bo])
    
    return bid,g

def p2(b):
    resources = (0,0,0,0)
    bots = (1,0,0,0)
    g,bo = maxgeodes(b,32,resources,bots)
    print([b,g,bo])
    return g



if True:
    tasks = list(blueprints.items())
    
    results = [p1(t) for  t in tasks]
    print(results)
    print(sum([k*v for k,v in results]))
else:
    tasks = list(blueprints.values())[0:3]
    results = [p2(t) for t in tasks]
    x = 1
    for y in results: x *= y
    print(results)
    print(y)


