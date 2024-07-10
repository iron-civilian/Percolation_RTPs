import  numpy as np


def get_data(fname):
	data=np.loadtxt(fname,max_rows=3)
	string=0
	with open(fname,'r') as file:
		for line in file:
			string=line
	j=string.find('x')
	return data,int(string[:j])
def merge(data1,n1,data2,n2):
	data=(data1*n1+data2*n2)/(n1+n2)
	n=n1+n2
	return data,n

if __name__=='__main__':
	omega_arr=np.linspace(0.015,0.03,18)
	for omega in omega_arr:
		fname1=f"data_{omega}_1.txt"
		data1,n1=get_data(fname1)
		fname2=f"data_{omega}_2.txt"
		data2,n2=get_data(fname2)
		
		data,n=merge(data1,n1,data2,n2)
		np.savetxt(f'data_0.1_0.04_{omega}_16.txt',data)
		with open(f'data_0.1_0.04_{omega}_16.txt','a') as file:
			file.write(f"{n}x{1000} ensembles written - J=0.1, L=16,p=0.04,omega={omega}")

			
	
