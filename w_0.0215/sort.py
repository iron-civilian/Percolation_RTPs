import numpy as np
import sys

L=int(sys.argv[1])

if __name__=="__main__":
    data1=f"3data_L{L}.txt"
    data2=f"33data_L{L}.txt"

    arr1=np.loadtxt(data1)
    arr2=np.loadtxt(data2)
    arr=np.append(arr1,arr2,axis=0)
    farr=np.array(sorted(arr,key=lambda x:x[0]))
    np.savetxt(f"3finaldata_{L}.txt",farr)

