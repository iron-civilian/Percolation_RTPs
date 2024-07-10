import numpy as np
import matplotlib.pyplot as plt

if __name__=='__main__':
    L_arr=[16,24,32,48,64]
    for L in L_arr:
        omega_arr=np.arange(0.001,0.1,0.005)
        m_arr=[]
        m2_arr=[]
        m4_arr=[]

        for omega in omega_arr:
            data=np.loadtxt(f'data_0.08_{omega:.3f}_{L}.txt',max_rows=3)
            m_arr.append(data[0][-1])
            m2_arr.append(data[1][-1])
            m4_arr.append(data[2][-1])
           
        m_arr=np.array(m_arr)/L**2
        m2_arr=np.array(m2_arr)/L**4
        m4_arr=np.array(m4_arr)/L**8

        bc=1-m4_arr/(3*m2_arr**2)
        plt.plot(omega_arr,bc,label=f'L={L}')
    plt.legend()
    plt.show()

