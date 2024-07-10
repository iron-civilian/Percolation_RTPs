import numpy as np

Larr=[10,16,20,32,50]

with open('2data.txt','w') as fl:
    for L in Larr:
        data=np.loadtxt(f"2dataL{L}p0.15.csv",delimiter=",")
        rho=np.mean(data[:,3]*.5+data[:,6]*.25+data[:,9]*.25)
        #sigma=np.mean((data[:,4]-data[:,3]**2)**.5*.5+ (data[:,6]-data[:,5]**2)**.5*.25+(data[:,8]-data[:,7]**2)**.5*.25)
        sigma=0
        fl.write(f"{L} {rho} {sigma}\n")

