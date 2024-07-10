import numpy as np
import sys
import matplotlib.pyplot as plt

L=int(sys.argv[1])
p=0.04
w=float(sys.argv[2])

def get_tt(N):
    tt=[1,]
    for i in range(N-1):
        tt.append(int(tt[-1]*1.01+1))
    return tt

if __name__=="__main__":
    data=np.loadtxt(f"data_{p}_{w}_{L}.txt",max_rows=3)[0]
    tt=np.array(get_tt(760))

    plt.plot(tt,data)
    plt.xscale('log')
    plt.show()

