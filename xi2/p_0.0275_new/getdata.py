import numpy as np
import sys

L=int(sys.argv[1])
Nens=int(sys.argv[2])

w_arr=[]

with open('a.x','r') as fl:
    for line in fl:
        w=float(line.split()[4])
        w_arr.append(w)

with open(f'xi2L{L}p0.0275.txt','w') as fl:
    for w in w_arr:
        c_arr=np.loadtxt(f"data_0.0275_{w}_{L}.txt",max_rows=L)
        gm=0
        rsq_gm=0
        for i in range(L//2+1):
            c_arr[i]=(c_arr[i]/(4*Nens*L**2) - .5**2)
            gm+=c_arr[i]
            rsq_gm+=i*i*c_arr[i]
        xi2=rsq_gm/gm
        fl.write(f"{L} 0.0275 {w} {xi2}\n")



