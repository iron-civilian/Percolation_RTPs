import numpy as np
import sys

p=float(sys.argv[1])
w=float(sys.argv[2])
u=int(sys.argv[3])

data=np.loadtxt(f"L128T{u}p{p}w{w}.txt")
data2=np.zeros_like(data)
L=len(data)

for i in range(L):
    if data[i]!=-1:
        data2[i]=1
np.savetxt(f"dataL128T{u}p{p}w{w}.txt",data2)

