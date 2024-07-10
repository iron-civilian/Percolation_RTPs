import numpy as np
import sys


L=int(sys.argv[1])
omega=float(sys.argv[2])

if __name__=='__main__':
    fname=f'data_0.08_{omega}_{L}.txt'
    data=np.loadtxt(fname,max_rows=3)
    k=0
    N_ensemble=0
    r_line=0
    with open(fname,'r') as file:
        for line in file:
            r_line=line
    i=r_line.find("x")
    j=r_line.find(" ")

    k=int(r_line[:i])
    N_ensemble=int(r_line[i+1:j])

    print(f"k={k}, Nens={N_ensemble}")




