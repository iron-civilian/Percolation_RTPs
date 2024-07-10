import numpy as np
import matplotlib.pyplot as plt

if __name__=='__main__':
    L_arr=[16,]
    L=24
    p=0.08
    m_arr=[]
    m2_arr=[]
    m4_arr=[]

    phi_arr=[]
    phi2_arr=[]
    phi4_arr=[]
    omega_arr=np.array([0.003,0.0044,0.0058,0.0072,0.0086,0.01,0.0114,0.0128,0.0142,0.0156,0.0170,0.0184,0.0198,0.0212,0.0226,0.0240,0.0254,0.0268,0.0282,0.0296])
    for omega in omega_arr:
        fname=f'L={L},omega={omega},p={p}.txt'
        data=np.loadtxt(fname,max_rows=3)
        m_arr.append(data[0])
        m2_arr.append(data[1])
        m4_arr.append(data[2])
        fname=f'data_{p}_{omega}_{L}.txt'
        data=np.loadtxt(fname,max_rows=3)
        phi_arr.append(data[0][-1])
        phi2_arr.append(data[1][-1])
        phi4_arr.append(data[2][-1])

    m_arr=np.array(m_arr)/L**2/100
    m2_arr=np.array(m2_arr)/L**4/100
    m4_arr=np.array(m4_arr)/L**8/100
    phi_arr=np.array(phi_arr)/L**2
    phi2_arr=np.array(phi2_arr)/L**4
    phi4_arr=np.array(phi4_arr)/L**8
    plt.scatter(omega_arr,m4_arr,color='red',label='t_avg 10^6')
    plt.plot(omega_arr,phi4_arr,color='black',label='Ens_avg 10^4')
    plt.legend()
    plt.show()

