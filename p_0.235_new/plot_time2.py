import numpy as np
import matplotlib.pyplot as plt
import sys

L=int(sys.argv[1])
p=float(sys.argv[2])
#omega=float(sys.argv[2])
if __name__=='__main__':
    omegalist=np.loadtxt("2data_L128.txt")[:,1][::2]
    for omega in omegalist:
        fname=f'data_{p}_{omega}_{L}.txt'
        data=np.loadtxt(fname,max_rows=3)
        m_arr=2*data[0]/L**2
        tt_arr=[1]
        for i in range(999):
            tt_arr.append(int(tt_arr[-1]*1.01+1))
        tt_arr=np.array(tt_arr)
        plt.plot(tt_arr,m_arr,label=r'$\omega={omega:.4f}$'.format(omega=omega))
        plt.xscale('log')
        #plt.yscale('log')
    plt.legend(fontsize=13)
    plt.ylim(0,1)
    plt.xlim(1,10**6)
    plt.xticks(size=20)
    plt.yticks([.2,.4,.6,.8,1.0],size=20)
    plt.ylabel(r"$\phi$",size=25)
    plt.xlabel("t",size=25)
    plt.tight_layout()
    plt.savefig(f"../finalfigs/ssp{p}.png")
    #plt.show()
	


