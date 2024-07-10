import numpy as np
import sys

L=int(sys.argv[1])
p=float(sys.argv[2])

if __name__=='__main__':
    w1_arr=np.arange(.005,.0251,.0025)
    w_arr=np.arange(.5*(.005+.0075),.0251,.0025)#[0.003,0.0044,0.0058,0.0072,0.0086,0.01,0.0114,0.0128,0.0142,0.0156,0.0170,0.0184,0.0198,0.0212,0.0226,0.0240,0.0254,0.0268,0.0282,0.0296]
    w_arr=np.append(w1_arr,w_arr)
    w_arr=np.sort(w_arr)
    with open(f"2data_L{L}.txt","w") as fi:
        for w in w_arr:
            fname=f"data_{p}_{w}_{L}.txt" 
            data=np.loadtxt(fname,max_rows=3)
            m=np.mean(data[0][-240:])
            m2=np.mean(data[1][-240:])
            m4=np.mean(data[2][-240:])
            fi.write(f"{p} {w} {m} {m2} {m4}\n")
