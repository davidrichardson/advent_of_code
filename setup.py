import sys
import os
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('year')

args = parser.parse_args()

for d in range(1,26):
    d = int(d)
    d_dir = Path(f'{args.year}/{d:02}')

    if not d_dir.exists():
        os.mkdir(d_dir)

    for f in ["input.txt","test_input.txt","script.py"]:
        fp = d_dir / f
        if not fp.exists():
            fp.touch()
    


