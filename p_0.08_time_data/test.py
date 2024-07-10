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
    if 0<=pos<N_sites and (pos not in visited) and state_arr[pos]:
        visited.append(pos)
        current_size+=1
        current_size=df1(state_arr,nbrarr[pos][0],current_size,visited)
        current_size=df1(state_arr,nbrarr[pos][1],current_size,visited)
        current_size=df1(state_arr,nbrarr[pos][2],current_size,visited)
        current_size=df1(state_arr,nbrarr[pos][3],current_size,visited)
    return current_size
        
@jit(nopython=True)
def update_ns(state_arr,s_bin):
    visited=[-1,]
   
    current_size=0
    
    for i in range(N_sites):
        if state_arr[i] and (i not in visited):
            current_size=0
            current_size=df1(state_arr,i,current_size,visited)
            s_bin[current_size]+=1
    
    
@jit(nopython=True)
def get_data(state_arr):
    Trlax=10**6
    Nens=10**7
    m=0
    m2=0
    m4=0
    s_bin=np.zeros(N_sites+1)
    for i in range(Trlax):
        for k in range(N_sites):
            MC_update(state_arr)
    for i in range(Nens):
        update_ns(state_arr,s_bin)
        for k in range(N_sites):
            MC_update(state_arr)
    return s_bin/Nens

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
        return data*k*Nens,k,Nens
    except:
        return np.zeros((3,1224)),0,0



if __name__=='__main__':
    state_arr=np.loadtxt(f'state_arr_{L}.txt')
    state_arr=np.array(state_arr,dtype=int)
   
    ti=time.time()
    s_bin=get_data(state_arr)
    tf=time.time()
    
    fname=f"L{L}p{p}w{omega}.txt"
    np.savetxt(fname,s_bin)

