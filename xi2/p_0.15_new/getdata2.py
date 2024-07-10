import numpy as np
import sys

L=int(sys.argv[1])
p=float(sys.argv[2])

w_arr=[]

with open('a2.x','r') as fl:
    for line in fl:
        w=float(line.split()[4])
        w_arr.append(w)


if __name__=='__main__':
    #w_arr=[.018,.0182,.0184,.0186,.0188,.019,.0192,.0194,.0196,.0198,.02]
    with open(f"2data_L{L}.txt","w") as fi:
        for w in w_arr:
            fname=f"fdata_{p}_{w}_{L}.txt" 
            data=np.loadtxt(fname,max_rows=3)
            m=np.mean(data[0][-100:])
            m2=np.mean(data[1][-100:])
            m4=np.mean(data[2][-100:])
            fi.write(f"{p} {w} {m} {m2} {m4}\n")

