import numpy as np
import sys

L=int(sys.argv[1])
w=float(sys.argv[2])

if __name__=='__main__':
    p_arr=np.arange(0.5*(.025+0.05),0.25,0.025)#[0.003,0.0044,0.001008,0.0072,0.0086,0.01,0.0114,0.0128,0.0142,0.011006,0.0170,0.0184,0.0198,0.0212,0.0226,0.0240,0.021004,0.0268,0.0282,0.0296]
    with open(f"44data_L{L}.txt","w") as fi:
        for p in p_arr:
            fname=f"data_{p}_{w}_{L}.txt" 
            data=np.loadtxt(fname,max_rows=3)
            m=np.mean(data[0][-100:])
            m2=np.mean(data[1][-100:])
            m4=np.mean(data[2][-100:])
            fi.write(f"{p} {w} {m} {m2} {m4}\n")

