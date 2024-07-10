import numpy as  np
import matplotlib.pyplot as plt

Larr=[64,72]

for L in Larr:
    data=np.loadtxt(f"2data_L{L}_p0.029.txt")
    y=1-data[:,4]/data[:,3]**2/3
    data=np.loadtxt(f"xi2L{L}p0.029.txt")
    x=(data[:,3]**.5)/L
    plt.scatter(x,y,label=f"L={L}")
plt.legend()
plt.show()
