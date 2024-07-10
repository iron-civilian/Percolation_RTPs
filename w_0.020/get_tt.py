import numpy as np
import sys

N=int(sys.argv[1])

tt=1
for i in range(N):
    print(f"{i+1} {tt}")
    tt=int(tt*1.01+1)

