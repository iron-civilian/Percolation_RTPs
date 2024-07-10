import numpy as np
import sys

L=int(sys.argv[1])

if __name__=="__main__":
    warr=np.arange(0.001,0.03,.0015)
    with open(f'data_{L}.txt','w') as fl:
        for w in warr:
            dataw=np.loadtxt(f'data_0.04_{w}_{L}.txt',max_rows=3)
            m,m2,m4=dataw[0][-1],dataw[1][-1],dataw[2][-1]
            fl.write(f'{L} 0.04 {w} {m} {m2} {m4}\n')

