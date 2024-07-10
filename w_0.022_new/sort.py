import numpy as np
import sys

L=int(sys.argv[1])

if __name__=="__main__":
    data1=f"4data_L{L}.txt"
    data2=f"44data_L{L}.txt"
    data3=f"444data_L{L}.txt"
    #data4=f"4444data_L{L}.txt"

    arr1=np.loadtxt(data1)
    arr2=np.loadtxt(data2)
    arr3=np.loadtxt(data3)
    #arr4=np.loadtxt(data4)

    arr=np.append(arr1,arr2,axis=0)
    arr=np.append(arr,arr3,axis=0)
    #arr=np.append(arr,arr4,axis=0)

    farr=np.array(sorted(arr,key=lambda x:x[0]))
    np.savetxt(f"4finaldata_{L}.txt",farr)

