import numpy as np
import matplotlib.pyplot as plt
from numba import jit
import pickle
from scipy.optimize import curve_fit as cf
import sys
#%matplotlib notebook
from matplotlib.colors import LinearSegmentedColormap
import time
from matplotlib import colors
import matplotlib.colors as mcolors
import multiprocessing


MM=1500
#L=int(sys.argv[1])
p=float(sys.argv[1])
omega=float(sys.argv[2])



L=256
Lx=L
Ly=L
N_sites=Lx*Ly

colors = [(0, 'white'),  # Value 0 is white
          (0.5, 'black'),  # Value 1 is black
          (1, 'red')]  # Value 2 is red

# Create the colormap
cmap = LinearSegmentedColormap.from_list('custom_cmap', colors)

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
    if 0<=pos<N_sites and (pos not in visited) and state_arr[pos]==1:
        visited.append(pos)
        current_size+=1
        current_size=df1(state_arr,nbrarr[pos][0],current_size,visited)
        current_size=df1(state_arr,nbrarr[pos][1],current_size,visited)
        current_size=df1(state_arr,nbrarr[pos][2],current_size,visited)
        current_size=df1(state_arr,nbrarr[pos][3],current_size,visited)
    return current_size

@jit(nopython=True)        
def percolate(state_arr,i,v2,c_arr,c):
    if 0<=i<N_sites and (i not in v2) and state_arr[i]==1:
        v2.append(i)
        c_arr[i]=c
        for j in range(4):
            percolate(state_arr,nbrarr[i][j],v2,c_arr,c)



@jit(nopython=True)
def get_largest_cluster(state_arr,c_arr,fl):
    visited=[-1,]
    
    largest_size=0
    current_size=0
    #n=0
    #c=0
    for i in range(N_sites):
        
        if (state_arr[i]==1) and (i not in visited):
            #c=c+fl*.01
            #n+=1
            current_size=0
            current_size=df1(state_arr,i,current_size,visited)
            v2=[-1,]
            percolate(state_arr,i,v2,c_arr,(current_size))
    #return n
    
    
@jit(nopython=True)
def get_data(tt,init_state,m_arr,m2_arr,m4_arr):
    for i in range(N_ensemble):
        state_arr=init_state.copy()
        t=0
        for j in range(760): #tt[760] ~ 10^5
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
        return data*k*Nens,k,Nens
    except:
        return np.zeros((3,760)),0,0

def getc2(c_arr):
    c_arr2=np.zeros_like(c_arr)
    c=np.max(c_arr)
    N=len(c_arr)
    for i in range(N):
        if c_arr[i]!=0 and c_arr[i]==c:
            c_arr2[i]=1
        elif c_arr[i]!=0 and c_arr[i]!=c:
            c_arr2[i]=.5
    return c_arr2

if __name__=='__main__':
    data=np.loadtxt(f'dataL128T7p{p}w{omega}.txt')
    c_arr=np.zeros_like(data)
    get_largest_cluster(data,c_arr,1)
    c_arr2=getc2(c_arr)
    #print(n)
    #data=data*-1
    #get_largest_cluster(data,c_arr,-1)
    #norm = colors.Normalize(vmin=0, vmax=10.2)
    #plt.imshow(c_arr2.reshape((L,L)),cmap=cmap)
    #plt.colorbar()
    #plt.colorbar()
    #plt.title("Only Down Spins",size="xx-large")
    #plt.show()
    np.savetxt(f"2dataL128T7p{p}w{omega}.txt",c_arr2)
    
    







    
    
    



