import sys
import os
from pathlib import Path

for d in sys.argv[1:]:
    d = int(d)
    d_dir = f'2022/{d:02}'

    os.mkdir(d_dir)

    for f in ["input.txt","test_input.txt","script.py"]:
        Path(f"{d_dir}/{f}").touch()
    


