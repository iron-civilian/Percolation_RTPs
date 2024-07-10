import numpy as np
import matplotlib.pyplot as plt

if __name__=='__main__':
    L_arr=[24,32]#,48]
    p=0.08
    omega_arr=np.array([0.003,0.0044,0.0058,0.0072,0.0086,0.01,0.0114,0.0128,0.0142,0.0156,0.0170,0.0184,0.0198,0.0212,0.0226,0.0240,0.0254,0.0268,0.0282,0.0296])
    for L in L_arr:
        m_arr=[]
        m2_arr=[]
        m4_arr=[]
        for omega in omega_arr:
            fname=f'L={L},omega={omega},p={p}.txt'
            data=np.loadtxt(fname,max_rows=3)
            m_arr.append(data[0])
            m2_arr.append(data[1])
            m4_arr.append(data[2])
        m_arr=np.array(m_arr)/(L**2)
        m2_arr=np.array(m2_arr)/(L**4)
        m4_arr=np.array(m4_arr)/L**8
        bc=1-m4_arr/m2_arr**2/3


        plt.plot(omega_arr,bc,label=f'L={L}')
    plt.legend()
    plt.show()

