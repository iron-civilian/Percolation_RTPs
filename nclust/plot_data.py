import numpy as np
import matplotlib.pyplot as plt
import sys



if __name__=='__main__':
    L_arr=[16,24,32,48]#24,32,48,64]#,32,48,64]
    for L in L_arr:
        omega_arr=np.array([.003,.0044,.0058,.0072,.0086,.01,.0114,.0128,.0142,.0156,.017,.0184,.0198,.0212,.0226,.0240,.0254,.0268,.0282,.0296])#np.arange(0.003,0.3,0.0014)
        m_arr=[]
        m2_arr=[]
        m4_arr=[]

        for omega in omega_arr:
            data=np.loadtxt(f'dataL{L}w{omega}.txt')
            m_arr.append(data[0])
            m2_arr.append(data[1])
            m4_arr.append(data[2])
           
        m_arr=np.array(m_arr)
        m2_arr=np.array(m2_arr)
        m4_arr=np.array(m4_arr)
        chi=(m2_arr-m_arr**2)*L**2

        bc=1-m4_arr/(3*m2_arr**2)
        plt.plot(omega_arr,m_arr,label=f'{L}')
        #plt.scatter(np.log(omega_c-omega_arr),np.log(m_arr),label=f'L={L}',marker='s',color='red')
        #plt.plot(np.log(omega_c-omega_arr),f(np.log(omega_c-omega_arr),beta,c),color='black')
        #plt.plot(omega_arr,bc,label=f'L={L}')
        #np.savetxt(f'bc_L={L}.txt',bc)
        #plt.plot((omega_c-omega_arr)*L**(1/nu),bc,label=f'L={L}')
        #plt.plot((omega_c-omega_arr)*L**(1/nu),m_arr*L**(beta/nu),label=f'L={L}')
        #plt.plot((omega_c-omega_arr)*L**(1/nu),chi*L**(-gamma/nu),label=f'L={L}')
    plt.legend()
    #plt.ylim(.642,.648)
    #plt.xlim(.021,0.0225)
    #plt.xlabel(r'$(\omega_c-\omega)L^\frac{1}{\nu}$',size='large')
    #plt.ylabel(r'$\chi L^\frac{-\gamma}{\nu}$',size='large')
    #plt.title(r'$\omega_c=0.022,\beta=0.09, \nu=0.85, \gamma=1.52$')
    #plt.savefig('chi_collapse.png')
    plt.show()

