import numpy as np
import sys

rho=float(sys.argv[2])
L=int(sys.argv[1])

N_sites=L*L
N=int(N_sites*rho)
a=N//4

state_arr=np.ones(N_sites)*-1
state_arr[:a]=0
state_arr[a:2*a]=1
state_arr[2*a:3*a]=2
state_arr[3*a:4*a]=3

np.random.shuffle(state_arr)
np.savetxt(f"state_arr_{L}.txt",state_arr)
