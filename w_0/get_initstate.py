import numpy as np
import sys

L=int(sys.argv[1])

data=np.ones(L*L)*-1
n=L*L//8

data[:n]=0
data[n:2*n]=1
data[2*n:3*n]=2
data[3*n:4*n]=3


np.random.shuffle(data)

np.savetxt(f'state_arr_{L}.txt',data)



