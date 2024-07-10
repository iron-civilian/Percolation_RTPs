import numpy as np
import matplotlib.pyplot as plt
import sys

L=int(sys.argv[1])
omega=float(sys.argv[2])

if __name__=='__main__':
	fname=f'data_0.08_{omega}_{L}.txt'
	data=np.loadtxt(fname,max_rows=3)
	
	m_arr=data[0]/L**2
	tt_arr=[1]
	
	for i in range(999):
		tt_arr.append(int(tt_arr[-1]*1.01+1))
	tt_arr=np.array(tt_arr)
	
	plt.plot(tt_arr,m_arr)
	plt.xscale('log')
	plt.show()
	


