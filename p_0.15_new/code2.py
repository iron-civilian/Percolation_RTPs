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
#J=float(sys.argv[4])
u=int(sys.argv[4])

z=1+3*p+2*omega
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
def MC_update2(state_arr):
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
def MC_update(state_arr):
    pos=np.random.randint(N_sites)
    if state_arr[pos]==-1:
        return None
    r=np.random.random()
    
    v=state_arr[pos]

    if r<1/z:
        if state_arr[nbrarr[pos][v]]!=-1:
            return None
        state_arr[nbrarr[pos][v]]=v
        state_arr[pos]=-1
    elif r<(1+p)/z:
        v1=(v+1)%4
        if state_arr[nbrarr[pos][v1]]!=-1:
            return None
        state_arr[nbrarr[pos][v1]]=v
        state_arr[pos]=-1
    elif r<(1+2*p)/z:
        v1=(v+2)%4
        if state_arr[nbrarr[pos][v1]]!=-1:
            return None
        state_arr[nbrarr[pos][v1]]=v
        state_arr[pos]=-1
    elif r<(1+3*p)/z:
        v1=(v+3)%4
        if state_arr[nbrarr[pos][v1]]!=-1:
            return None
        state_arr[nbrarr[pos][v1]]=v
        state_arr[pos]=-1
    elif r<(1+3*p+omega)/z:
        state_arr[pos]=(v+1)%4
    else:
        state_arr[pos]=(v+3)%4

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
        for j in range(1000): #tt[1000] ~ 10^5
            while(t<tt[j]):
                for k in range(N_sites):
                    MC_update(state_arr)
                t+=1
            m=get_largest_cluster(state_arr)
            m_arr[j]=m_arr[j]+m
            m2_arr[j]=m2_arr[j]+m*m
            m4_arr[j]=m4_arr[j]+m*m*m*m
    

def get_k_Nens(fname):
    #data=np.loadtxt(fname,max_rows=3)
    k=0
    Nens=0
    rline=0

    try:
        data=np.loadtxt(fname,max_rows=3)
        with open(fname,'r') as file:
            for line in file:
                rline=line
        i=rline.find("x")
        j=rline.find(" ")
        k=int(rline[:i])
        Nens=int(rline[i+1:j])
        if Nens!=N_ensemble:
            print("N ensembles dont match!!!")
            exit()
        return data*k*Nens,k,Nens
    except FileNotFoundError:
        return np.zeros((3,1000)),0,0



if __name__=='__main__':
    tt=[1]
    for i in range(MM):
        tt.append(int(tt[-1]*1.01+1))

    init_state=np.loadtxt(f'state_arr_{L}.txt')
    init_state=np.array(init_state,dtype=int)
    
    fname=f"data_{p}_{omega}_{L}.txt"
    data,k,Nens=get_k_Nens(fname)


    m_arr=data[0]
    m2_arr=data[1]
    m4_arr=data[2]
    while True:
        k+=1
        get_data(tt,init_state,m_arr,m2_arr,m4_arr)
        y=np.zeros((3,1000))
        
        y[0]=m_arr/(N_ensemble*k)
        y[1]=m2_arr/(N_ensemble*k)
        y[2]=m4_arr/(N_ensemble*k)
        np.savetxt(f'data_{p}_{omega}_{L}.txt',y)
        
        with open(f'data_{p}_{omega}_{L}.txt','a') as file:
            file.write(f'{k}x{N_ensemble} ensembles written - L={L},p={p},omega={omega}')







    
    
    



