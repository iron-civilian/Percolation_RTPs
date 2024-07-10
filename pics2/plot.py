import numpy as np
import matplotlib.pyplot as plt
import sys

p=float(sys.argv[1])
w=float(sys.argv[2])
u=int(sys.argv[3])

data=np.loadtxt(f"dataL128T{u}p{p}w{w}.txt")
data=data.reshape((256,256))
plt.imshow(data,cmap='Greys')
plt.xticks([])
plt.yticks([])
plt.tight_layout()
#plt.title(f'p={p},w={w},T=1e{u}',size='x-large')
plt.savefig(f'p{p}w{w}u{u}.png')

