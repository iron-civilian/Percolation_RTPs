import numpy as np
import matplotlib.pyplot as plt
import sys

L=int(sys.argv[1])
omega=float(sys.argv[2])
Nt=int(sys.argv[3])

if __name__=='__main__':
    fname=f'data_0.08_{omega}_{L}.txt'
    data=np.loadtxt(fname,max_rows=3)
	
    m_arr=2*data[0]/L**2
    tt_arr=[1]
    for i in range(Nt-1):
        tt_arr.append(int(tt_arr[-1]*1.01+1))
    tt_arr=np.array(tt_arr)
    plt.xlim((1,tt_arr[-1]))
    plt.plot(tt_arr,m_arr)
    plt.xscale('log')
    plt.ylabel(r'$\phi$',size=20)
    plt.xlabel('# MC steps',size=20)
    plt.yticks(size=15)
    plt.xticks(size=15)
    plt.title(r'$L$={L},$p$=0.08,$\omega$={omega}'.format(L=L,omega=omega),size=20)
    plt.tight_layout()
    plt.show()
	


