import numpy as np
import sys

L=int(sys.argv[1])
p=float(sys.argv[2])

if __name__=='__main__':
    w_arr=np.arange(0.01,.0285,.0023)
    w_arr2=np.arange(.5*(.01+.0123),.0285,.0023)
    w_arr=np.append(w_arr,w_arr2)
    w_arr=np.sort(w_arr)
    with open(f"2data_L{L}.txt","w") as fi:
        for w in w_arr:
            fname=f"data_{p}_{w}_{L}.txt" 
            data=np.loadtxt(fname,max_rows=3)
            m=np.mean(data[0][-240:])
            m2=np.mean(data[1][-240:])
            m4=np.mean(data[2][-240:])
            fi.write(f"{p} {w} {m} {m2} {m4}\n")

