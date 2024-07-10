import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import colors
import matplotlib.colors as mcolors

parr=[.235,.08,.02]
warr=[.012,.022,.032]

colors = [(0, 'white'),  # Value 0 is white
          (0.5, 'black'),  # Value 1 is black
          (1, 'red')]  # Value 2 is red

# Create the colormap
cmap = LinearSegmentedColormap.from_list('custom_cmap', colors)


fig,axs=plt.subplots(3,3,figsize=(10,10))

for i in range(3):
    for j in range(3):
        p=parr[i]
        w=warr[j]
        data=np.loadtxt(f"2dataL128T7p{p}w{w}.txt")
        data=data.reshape((256,256))
        #axs[i][j].set_title(f"p={p},w={w}",size='xx-large')
        axs[i][j].imshow(data,cmap=cmap)
        axs[i][j].set_xticks([])
        axs[i][j].set_yticks([])
        axs[i][j].set_aspect('auto')

fig.add_subplot(111, frameon=False)

plt.tick_params(labelcolor='black', top=False, bottom=False, left=False, right=False)
plt.xlabel(r'$\omega$', labelpad=0,size=50)
plt.ylabel('p', labelpad=0,size=50)
plt.annotate('', xy=(0, 3), xytext=(0,-.15), arrowprops=dict(facecolor='black', arrowstyle='<->',linewidth=7))
plt.annotate('', xy=(3,0), xytext=(-.15, 0), arrowprops=dict(facecolor='black', arrowstyle='<->',linewidth=7))

# Add lines along with the axis
#plt.axhline(-10, color='black', lw=1)
#plt.axvline(-25, color='black', lw=1)

# Set axis ticks for the global figure
plt.xticks([.475,1.475,2.475,3],['0.012','0.022','0.032',''],color='black',fontsize=35)
plt.yticks([.475,1.475,2.475,3],['0.02','0.08','0.235',''],color='black',fontsize=35)

fig.subplots_adjust(hspace=0.02, wspace=0.02)
plt.tight_layout()
#plt.savefig('finalcollage.png')
#plt.show()
plt.savefig("tempcol.png")
