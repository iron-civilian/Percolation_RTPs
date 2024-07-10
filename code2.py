import numpy as np
import matplotlib.pyplot as plt
from numba import jit
import pickle
from scipy.optimize import curve_fit as cf
import sys
#%matplotlib notebook
import time
import matplotlib.colors as mcolors
import multiprocessing


MM=1500
L=int(sys.argv[1])
#T=float(sys.argv[2])
p=float(sys.argv[2])
omega=float(sys.argv[3])
J=float(sys.argv[4])
u=int(sys.argv[5])

N_ensemble=10**u





Lx=L
Ly=L
N_sites=Lx*Ly



'''
----------
convention
----------
-1 : No particle
0 : Particle along right
1 : Particle along down
2 : Particle along left
3 : Particle along up
'''

#start = time.time()


def nbr2D(L):
    nbrarr=np.zeros((N_sites,4),dtype=int)
    
    for i in range(N_sites):
        k1=i//Ly
        k2=i%Ly
        if 1<=k1<=Lx-2:
            nbrarr[i][3]=(k1-1)*Ly+k2 #up
            nbrarr[i][1]=(k1+1)*Ly+k2 #down
        else:
            a=(k1==0)
            nbrarr[i][3]=Ly*(Lx-2+a)+k2 #up
            nbrarr[i][1]=Ly*a+k2 #down
        if 1<=k2<=Ly-2:
            nbrarr[i][2]=i-1 #left
            nbrarr[i][0]=i+1 #right
        else:
            b=(k2==0)
            nbrarr[i][2]=(i-1+Ly*b)
            nbrarr[i][0]=(i+1-Ly*(1-b))
    return nbrarr
nbrarr=nbr2D(L)

@jit(nopython=True)
def is_nonzero(i):
    if i==-1:
        return 0
    return 1

@jit(nopython=True)
def delH(state_arr,i,k):
    delE=0
    nbr_i=state_arr[nbrarr[i][k]]
    for j in range(4):
       delE+=is_nonzero(state_arr[nbrarr[nbr_i][j]])-is_nonzero(state_arr[nbrarr[i][j]])
    return -J*(delE-1)

@jit(nopython=True)
def MC_update(state_arr):
    pos=np.random.randint(N_sites)
    if state_arr[pos]==-1:
        return None
    if np.random.random()<0.5:
        r=np.random.random()
        nbr=state_arr[pos]
        r1=p/(3*p+1)

        if r<r1:
            nbr=(nbr+1)%4
        elif r<2*r1:
            nbr=(nbr+2)%4
        elif r<3*r1:
            nbr=(nbr+3)%4
        if state_arr[nbrarr[pos][nbr]]!=-1:
            return None
        delE=delH(state_arr,pos,nbr)
        
        if delE<=0 or np.random.random()<np.exp(-delE):
            state_arr[nbrarr[pos][nbr]]=state_arr[pos]
            state_arr[pos]=-1

    else:
        r=np.random.random()
        Dir=state_arr[pos]
        r1=omega/(2*omega+1)
        if r<r1:
            Dir=(Dir+1)%4
        elif r<2*r1:
            Dir=(Dir+3)%4
        state_arr[pos]=Dir

@jit(nopython=True)
def random_initialize(state_arr):
    pos_arr=np.arange(0,N_sites)
    np.random.shuffle(pos_arr)
    for i in range(N_sites//2):
        state_arr[pos_arr[i]]=np.random.choice(np.array([0,1,2,3]))

@jit(nopython=True)
def df1(state_arr,pos,current_size,visited):
    if 0<=pos<N_sites and (pos not in visited) and state_arr[pos]!=-1:
        visited.append(pos)
        current_size+=1
        current_size=df1(state_arr,nbrarr[pos][0],current_size,visited)
        current_size=df1(state_arr,nbrarr[pos][1],current_size,visited)
        current_size=df1(state_arr,nbrarr[pos][2],current_size,visited)
        current_size=df1(state_arr,nbrarr[pos][3],current_size,visited)
    return current_size
        
@jit(nopython=True)
def get_largest_cluster(state_arr):
    visited=[-1,]
    
    largest_size=0
    current_size=0
    
    for i in range(N_sites):
        if (state_arr[i]!=-1) and (i not in visited):
            current_size=0
            current_size=df1(state_arr,i,current_size,visited)
            largest_size=max(largest_size,current_size)
    return largest_size
    
    
@jit(nopython=True)
def get_data(tt,init_state,m_arr,m2_arr,m4_arr):
    for i in range(N_ensemble):
        state_arr=init_state.copy()
        t=0
        for j in range(760): #tt[760] ~ 10^5
            while(t<tt[j]):
                for i in range(N_sites):
                    MC_update(state_arr)
                t+=1
        m=get_largest_cluster(state_arr)
        m_arr[0]=m_arr[0]+m
        m2_arr[0]=m2_arr[0]+m*m
        m4_arr[0]=m4_arr[0]+m*m*m*m
    


if __name__=='__main__':
    tt=[1]
    for i in range(MM):
        tt.append(int(tt[-1]*1.01+1))

    init_state=np.loadtxt(f'state_arr_{L}.txt')
    init_state=np.array(init_state,dtype=int)
    
    m_arr=np.zeros(1)
    m2_arr=np.zeros(1)
    m4_arr=np.zeros(1)
    k=0
    while True:
        k+=1
        get_data(tt,init_state,m_arr,m2_arr,m4_arr)
        y=np.zeros((3,1))
        
        y[0]=m_arr/(N_ensemble*k)
        y[1]=m2_arr/(N_ensemble*k)
        y[2]=m4_arr/(N_ensemble*k)
        np.savetxt(f'data_{J}_{p}_{omega}_{L}.txt',y.reshape(3))
        
        with open(f'data_{J}_{p}_{omega}_{L}.txt','a') as file:
            file.write(f'{k}x{N_ensemble} ensembles written - J={J}, L={L},p={p},omega={omega}')







    
    
    


