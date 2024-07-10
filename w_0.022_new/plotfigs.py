import numpy as np
import matplotlib.pyplot as plt

ed=[1]*150
ed[72]='red'
ed[64]='blue'
ed[108]='green'
ed[128]='purple'


fig=plt.figure(figsize=(5.5,5))
ax_main=fig.add_axes([.24, .165, .745,.81])


plt.subplots_adjust(left=0.25, right=0.9, top=0.9, bottom=0.15)

for L in [64,72,108,128]:
    data=np.loadtxt(f"4finaldata_{L}.txt")
    p=data[:,0]
    bc=1-data[:,4]/data[:,3]**2/3
    ax_main.plot(p,bc,label=f'L={L}',lw=1.5,color=ed[L])
ax_main.legend(loc=(.25,.5),fontsize=14,frameon=False)
ax_main.set_xlim(.0125,.225)
ax_main.set_ylim(.6,.667)

ax_main.annotate('',xy=(.1919, .6343), xytext=(.1952,.5997),arrowprops=dict(arrowstyle='-', connectionstyle='arc3',linestyle=(0, (5, 5)),linewidth=1.5, color='black'))
ax_main.text(.14, .62, '0.191', fontsize=20)

ax_main.annotate('',xytext=(.1665,.619),xy=(.191,.6005),arrowprops=dict(headlength=8,width=1, connectionstyle='arc3',linewidth=1, color='black'))

ax_main.annotate('',xy=(.0404, .65442), xytext=(.039,.5997),arrowprops=dict(arrowstyle='-', connectionstyle='arc3',linestyle=(0, (5, 5)),linewidth=1.5, color='black'))
ax_main.text(.048, .62, '0.0414', fontsize=20)

ax_main.annotate('',xytext=(.076,.619),xy=(.042,.6005),arrowprops=dict(headlength=8,width=1, connectionstyle='arc3',linewidth=1, color='black'))

#ax_main.set_xticks([.0125,.125,.225],[.0125,.125,.2375],fontsize=15)
#ax_main.set_yticks([.61,.64,.667],[.61,.64,.67],fontsize=15)


ax_main.set_xticks([.03, .12, .21])
ax_main.set_xticklabels([.03, .12, .21], fontsize=20)
ax_main.set_yticks([.61, .64, .667])
ax_main.set_yticklabels([.61, .64, .67], fontsize=20)

ax_main.set_xlabel('p',size=25)
ax_main.set_ylabel(r'$U_4$',size=25)
plt.show()
