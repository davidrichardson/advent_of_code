import hashlib
import sys
from itertools import count

key = sys.stdin.read().strip()

def hashy(key,value):
    return hashlib.md5(f"{key}{value}".encode('utf-8')).hexdigest()

found_a = False

for i in count(1):
    h = hashy(key,i)
    if not found_a and h.startswith('00000'):
        print('a)',i)
        found_a = True
    if h.startswith('000000'):
        print('b)',i)
        break


