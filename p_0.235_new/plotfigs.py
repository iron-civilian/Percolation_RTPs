import numpy as np
import matplotlib.pyplot as plt


n=1.2
wc=.0199
bn=.14
gn=1.72
m=[1]*150
m[64]='o'
m[72]='^'
m[108]='s'
m[128]='p'
ed=[1]*150
ed[64]='blue'
ed[72]='red'
ed[108]='green'
ed[128]='purple'
fig=plt.figure(figsize=(5.5,5))
ax_main=fig.add_axes([.24, .165, .745,.81])



left, bottom, width, height = 0.68, 0.345, 0.28, 0.28
ax_small = fig.add_axes([left, bottom, width, height])

for L in [64,72,108,128]:
    data=np.loadtxt(f"2data_L{L}.txt")
    w=data[:,1]
    bc=1-data[:,4]/data[:,3]**2/3
    phi=data[:,2]
    chi=data[:,3]-phi**2
    ax_main.scatter((wc-w)*L**n,bc,label=f'L={L}',s=80,edgecolors=ed[L],facecolors='None',lw=1,marker=m[L])
    #plt.plot(w,bc,color=ed[L],label=f'L={L}',lw=.85)
    ax_small.plot((wc-w),bc,label=f'L={L}',color=ed[L])#,marker=m[L],markeredgecolor=ed[L],markerfacecolor='None')



### bc ###
ax_small.set_xlabel(r'$\epsilon$',size=18)
ax_small.set_ylabel(r'$U_4$',size=18)
ax_small.set_xticks([0,.01],[0,.01],size=18)
ax_small.set_yticks([.45,.55,.65],[0.45,.55,.65],size=18)

ax_main.legend(loc=(.0,.68),fontsize=14,frameon=False)
plt.subplots_adjust(left=0.25, right=0.9, top=0.9, bottom=0.15)

ax_main.set_xlim(-2,4)
ax_main.set_ylim(.45,.75)
ax_main.set_xlabel(r'$\epsilon L^{\frac{1}{\nu}}$',size=25)
#plt.xlabel('w',size='x-large')
ax_main.set_ylabel(r'$U_4$',size=25)
ax_main.set_xticks([-2,0,2,4],[-2,0,2,4],fontsize=20)
ax_main.set_yticks([.45,.6,.75],[.45,.6,.75],fontsize=20)
##########


'''
### phi ###
ax_small.set_xlabel(r'$\epsilon$',size=18)
ax_small.set_ylabel(r'$\phi$',size=18)
ax_small.set_xticks([0,.012],[0,.012],size=18)
ax_small.set_yticks([.1,.3,.5],[0.2,.6,1],size=18)

ax_main.legend(loc=(.62,.01),fontsize=14,frameon=False)
plt.subplots_adjust(left=0.25, right=0.9, top=0.9, bottom=0.15)

ax_main.set_xlim(-1,1)
ax_main.set_ylim(0,1.5)
ax_main.set_xlabel(r'$\epsilon L^{\frac{1}{\nu}}$',size=25)
#plt.xlabel('w',size='x-large')
ax_main.set_ylabel(r'$\phi L^{\frac{\beta}{\nu}}$',size=25)
ax_main.set_xticks([-1,-.5,0,.5,1],[-1,-.5,0,.5,1],fontsize=20)
ax_main.set_yticks([0,.75,1.5],[0,.75,1.5],fontsize=20)
##########
'''


'''
### chi ###
ax_small.set_xlabel(r'$\epsilon$',size=18)
ax_small.set_ylabel(r'$\chi$',size=18)
ax_small.set_xticks([0,.012],[0,.012],size=18)
ax_small.set_yticks([0,25,50],[0,25,50],size=18)

ax_main.legend(loc=(.5,.65),fontsize=14,frameon=False)
plt.subplots_adjust(left=0.25, right=0.9, top=0.9, bottom=0.15)

ax_main.set_xlim(-.5,4)
ax_main.set_ylim(0,.015)
ax_main.set_xlabel(r'$\epsilon L^{\frac{1}{\nu}}$',size=25)
#plt.xlabel('w',size='x-large')
ax_main.set_ylabel(r'$\chi L^{-\frac{\gamma}{\nu}}$',size=25)
ax_main.set_xticks([0,2,4],[0,2,4],fontsize=20)
ax_main.set_yticks([0,.004,.008,.012],[0,.04,.08,.12],fontsize=20)
##########
'''


#plt.tight_layout(pad=.2)
plt.show()

'''
plt.subplots_adjust(left=0.25, right=0.9, top=0.9, bottom=0.15)
data=np.loadtxt("fdata_L128.txt")
w=data[:,1]
wc=.02
phi=data[:,2]/128**2
er=(data[:,3]-data[:,2]**2)/128**4
#plt.scatter((wc-w),phi,c='red',marker='s')
ax_main.errorbar((wc-w), phi, yerr=er**.5,c='red', fmt='s',capsize=5, label='data_L=128_p=0.235')
ax_main.set_xscale('log')
ax_main.set_yscale('log')
ax_main.set_ylim(.1,1)
ax_main.set_xlim(.0003,)
x=np.linspace(0.00001,1,100)
ax_main.plot(x,.6575*x**(.1166667),c='black',label='.65758*x**(.1167)')
ax_main.legend()
ax_main.set_xlabel(r'$\epsilon$ ($10^{-3}$)',size=25)
ax_main.set_ylabel(f'$\phi$',size=25)
ax_main.set_xticks([5e-4,1e-3,2e-3],[r'$0.5$',r'$1$',r'$2$'],fontsize=20)
ax_main.set_yticks([.1,.5,1],[.1,.5,1],fontsize=20)
ax_main.yaxis.set_minor_formatter(plt.NullFormatter())
ax_main.xaxis.set_minor_formatter(plt.NullFormatter())
ax_main.legend(fontsize=14,frameon=False)
#plt.savefig('directfit_p=0.235.png')

plt.show()
'''
