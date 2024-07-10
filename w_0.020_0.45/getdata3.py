import numpy as np
import sys

L=int(sys.argv[1])
w=float(sys.argv[2])

if __name__=='__main__':
    p_arr=np.arange(.01,.31,.0415)#[0.003,0.0044,0.0058,0.0072,0.0086,0.01,0.0114,0.0128,0.0142,0.0156,0.0170,0.0184,0.0198,0.0212,0.0226,0.0240,0.0254,0.0268,0.0282,0.0296]
    p1_arr=np.arange(.5*(.01+.0515),.3,.0415)#[0.003,0.0044,0.0058,0.0072,0.0086,0.01,0.0114,0.0128,0.0142,0.0156,0.0170,0.0184,0.0198,0.0212,0.0226,0.0240,0.0254,0.0268,0.0282,0.0296]
    p_arr=np.append(p_arr,p1_arr)
    p_arr=np.append(p_arr,np.array([.02,.04]))
    p_arr=np.sort(p_arr)
    with open(f"2data_L{L}.txt","w") as fi:
        for p in p_arr:
            fname=f"data_{p}_{w}_{L}.txt" 
            data=np.loadtxt(fname,max_rows=3)
            m=np.mean(data[0][-100:])
            m2=np.mean(data[1][-100:])
            m4=np.mean(data[2][-100:])
            fi.write(f"{p} {w} {m} {m2} {m4}\n")
