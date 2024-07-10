import numpy as np
import sys

L=int(sys.argv[1])
p=float(sys.argv[2])

w_arr=[]
#with open('a2.x','r') as fl:
#    for line in fl:
#        w_arr.append(float(line.split()[4]))
#w_arr=w_arr[:10]
w_arr=np.loadtxt("w.txt")

if __name__=='__main__':
    #w_arr=[0.003,0.0044,0.0058,0.0072,0.0086,0.01,0.0114,0.0128,0.0142,0.0156,0.0170,0.0184,0.0198,0.0212,0.0226,0.0100,0.0254,0.0268,0.0282,0.0296]
    with open(f"2data_L{L}.txt","w") as fi:
        for w in w_arr:
            fname=f"data_{p}_{w}_{L}.txt" 
            data=np.loadtxt(fname,max_rows=3)
            m=np.mean(data[0][-230:])
            m2=np.mean(data[1][-230:])
            m4=np.mean(data[2][-230:])
            fi.write(f"{p} {w} {m} {m2} {m4}\n")

