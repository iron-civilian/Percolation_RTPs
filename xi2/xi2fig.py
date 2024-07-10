import numpy as  np
import matplotlib.pyplot as plt

Larr=[64,72]
cdict={0.15:"red",0.235:"cornflowerblue",0.029:"green",0.0275:"purple",0.02:"orange"}
mdict={64:"s",72:"o"}

parr=np.sort([0.02,0.15,0.235,0.029,0.0275])
for p in parr:
    for L in Larr:
        try:
            data=np.loadtxt(f"2data_L{L}_p{p}.txt")
        except:
            continue
        y=1-data[:,4]/data[:,3]**2/3
        data=np.loadtxt(f"xi2L{L}p{p}.txt")
        x=(data[:,3]**.5)/L
        plt.scatter(x,y,label=f"L={L},p={p}",marker=mdict[L],color=cdict[p])#,edgecolor='black')


data1=np.loadtxt("ddata_L32.txt")
y=1-data1[:,4]/data1[:,3]**2/3
data2=np.loadtxt("xxi2L32.txt")
x=data2[:,2]**.5/32/1#.0015

plt.plot(x,y,lw=4,linestyle='dashed',label=r"$Z_2P$",c='black')

#data1=np.loadtxt("ddata_L48.txt")
#y=1-data1[:,4]/data1[:,3]**2/3
#data2=np.loadtxt("xxi2L48.txt")
#x=data2[:,2]**.5/48/1.00

#plt.scatter(x,y,label="CLG",c='blue')

'''
data1=np.loadtxt("ddata_L48.txt")
y=1-data1[:,4]/data1[:,3]**2/3
data2=np.loadtxt("xxi2L48.txt")
x=data2[:,2]**.5/48

plt.scatter(x,y,label="CLG",c='black')
'''

plt.xlim(.268,.288)
plt.ylim(.475,.675)
plt.legend(fontsize=13.5)
plt.yticks([.475,.525,.575,.625,.675],fontsize=15)
plt.xticks([.27,.275,.28,.285,.29],fontsize=15)
plt.xlabel((r'$\xi_2/L$'),size=25)
plt.ylabel((r'$U_4$'),size=25)
plt.tight_layout()
plt.savefig("xi2.png")
#plt.show()
