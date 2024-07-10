import numpy as np
data=np.loadtxt('data.txt',delimiter=',')
data=sorted(data,key=lambda x:x[0])
np.savetxt('data.txt',data)
