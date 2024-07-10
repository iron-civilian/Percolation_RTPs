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
p=float(sys.argv[2])
omega=float(sys.argv[3])
w=omega

u1=int(sys.argv[4])
u2=int(sys.argv[5])

Trlax=10**u1
N_ensemble=10**u2





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

def append_to_file(filename, data, lock):
    with lock:
        with open(filename, 'a') as fl:
            fl.write(data)
            
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
def get_data(init_state):
    state_arr=init_state.copy()
    m=0
    m2=0
    m4=0
    for i in range(Trlax):
        for j in range(N_sites):
            MC_update(state_arr)
    for i in range(N_ensemble):
        for j in range(N_sites):
            MC_update(state_arr)
        phi=get_largest_cluster(state_arr)/N_sites
        m+=phi
        m2+=phi*phi
        m4+=phi*phi*phi*phi
    return m/N_ensemble,m2/N_ensemble,m4/N_ensemble
    

@jit(nopython=True)
def get_states(init_state):
    state_arr=init_state.copy()
    
    for i in range(Trlax):
        for j in range(N_sites):
            MC_update(state_arr)
    return state_arr
        
if __name__=='__main__':
    init_state=np.loadtxt(f'state_arr_{L}.txt')
    init_state=np.array(init_state,dtype=int)

    
    state=get_states(init_state)

    

    
    plt.imshow(state.reshape((L,L)))
    plt.title(f"L={L},p={p},w={omega}")
    plt.savefig(f'figL{L}u1{u1}.png')

    
    '''

    m,m2,m4=get_data(init_state)
    
    filename = f'{u1}_{u2}dataL{L}.txt'
    lock = multiprocessing.Lock()
    
    append_to_file(filename,f'{L},{p},{w},{m},{m2},{m4}\n',lock)
    '''
    
   
    
    






    
    
    



