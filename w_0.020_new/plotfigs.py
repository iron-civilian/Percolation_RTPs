import numpy as np
import matplotlib.pyplot as plt

pc=.235
n=1.1
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

plt.subplots_adjust(left=0.25, right=0.9, top=0.9, bottom=0.15)

for L in [64,72,108,128]:
    data=np.loadtxt(f"4finaldata_{L}.txt")
    p=data[:,0]
    phi=data[:,2]
    chi=(data[:,3]-data[:,2]**2)
    bc=1-data[:,4]/data[:,3]**2/3
    ax_main.plot(p,bc,label=f'L={L}',color=ed[L],lw=1.5)
    #plt.scatter((pc-p)*L**(n),bc,label=f'L={L}',s=25,marker=m[L],facecolors='none',edgecolors=ed[L],linewidth=.8)
ax_main.set_xlim(.01,.265)
ax_main.set_ylim(.5945,.668)
#plt.xlabel(r'$\Delta L^{\frac{1}{\nu}}$',size='x-large')
#plt.ylabel(r'$\phi L^{\frac{\beta}{\nu}}$',size='x-large')
#plt.xlabel("p",size='x-large')

ax_main.annotate('',xy=(.235, .626), xytext=(.235,.5942),arrowprops=dict(arrowstyle='-', connectionstyle='arc3',linestyle=(0, (5, 5)),linewidth=1.5, color='black'))
ax_main.text(.16, .62, '0.235', fontsize=20)

ax_main.annotate('',xytext=(.19,.619),xy=(.231,.595),arrowprops=dict(headlength=8,width=1, connectionstyle='arc3',linewidth=1, color='black'))

ax_main.annotate('',xy=(.0287, .6559), xytext=(.0287,.5942),arrowprops=dict(arrowstyle='-', connectionstyle='arc3',linestyle=(0, (5, 5)),linewidth=1.5, color='black'))
ax_main.text(.036, .62, '0.029', fontsize=20)

ax_main.annotate('',xytext=(.065,.619),xy=(.034,.596),arrowprops=dict(headlength=8,width=1,connectionstyle='arc3',linewidth=1, color='black'))

ax_main.set_xticks([.01, .13, .25])
ax_main.set_xticklabels([.01, .13, .25], fontsize=20)
ax_main.set_yticks([.61, .64, .667])
ax_main.set_yticklabels([.61, .64, .67], fontsize=20)

ax_main.set_xlabel('p',size=25)
ax_main.set_ylabel(r'$U_4$',size=25)

ax_main.legend(loc=(.25,.5),fontsize=14,frameon=False)
plt.show()
