import sys
import re


lines = list(sys.stdin.readlines())

def part_a(lines):
    nice_count = 0

    for l in lines:
        vowels = 0
        has_double = False
        has_bad = False

        for i in range(len(l)-1):
            if l[i] in 'aeiou':
                vowels += 1
            pair = (l[i] , l[i+1]) 
            if pair[0] == pair[1]:
                has_double = True
            
            if pair in [('a','b'),('c','d'),('p','q'),('x','y')]:
                has_bad = True
                break        

        if not has_bad and vowels >=3 and has_double:
            nice_count += 1

    return nice_count

def part_b(lines):
    nice_count = 0

    pair_re = re.compile('(..).*\\1')
    repeat_re = re.compile('(.).\\1')

    return sum(1 for l in lines if pair_re.search(l) and repeat_re.search(l))


print('a)', part_a(lines))
print('b)', part_b(lines))