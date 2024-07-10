import numpy as np
import matplotlib.pyplot as plt
import sys
import random as rdom
from numba import njit

# Calling up the initial array]
L = int(sys.argv[1])
p = float(sys.argv[2])
omega = float(sys.argv[3])
rho = float(sys.argv[4])

# The default system parameters
tsat = 5000000 # saturation time
tmax = 1000000 # The maximum time
ensemble = 1 # The number of ensemble

# System generated parameters
Lx = 6 * L
Ly = 2 * L
vol = Lx * Ly # square length

Ns = round(vol * rho) # Number of particles

@njit
def initialize():
	array = np.zeros(vol, dtype = np.bool_)
	for i in range(Ns):
		array[2*i] = 1
	return array


# defining the position array
positions = np.zeros((vol, 2), dtype = np.int16)
for i in range(Lx):
	for j in range(Ly):
		k = i * Ly + j
		positions[k,0] = i
		positions[k,1] = j
		
pos_rev = np.zeros((Lx,Ly), dtype = np.int16)
for i in range(Lx):
	for j in range(Ly):
		pos_rev[i,j] = i * Ly + j
		
# Define the neighbours
neighbour = np.zeros((vol,4), dtype = np.int16)
for i in range(Lx):
	for j in range(Ly):
		neighbour[i*Ly + j, 0] = ((i - 1) % Lx) * Ly + j
		neighbour[i*Ly + j, 1] = i * Ly + (j - 1) % Ly
		neighbour[i*Ly + j, 2] = ((i + 1) % Lx) * Ly + j
		neighbour[i*Ly + j, 3] = i * Ly + (j + 1) % Ly 

direc =  np.array([[1, 1+p, 1+2*p, 1+3*p,1+3*p+omega, 1+3*p+2*omega], [p, 1+p, 1+2*p, 1+3*p,1+3*p+omega, 1+3*p+2*omega], [p, 2*p, 1+2*p, 1+3*p,1+3*p+omega, 1+3*p+2*omega], [p, 2*p, 3*p, 1+3*p,1+3*p+omega, 1+3*p+2*omega]])

direc = direc / (1 + 3*p + 2*omega)

# The circular 4 array
circ = np.array([[1,2,3,0],[3,0,1,2]])

@njit
def sites(array, size):
	locations = np.zeros(size, dtype = np.int32)
	c = 0
	for ij in range(vol):
		if array[ij] == 1:
			locations[c] = ij
			c += 1
	return locations
	
@njit
def movement(lattice, locations, size, direction):
	for iter in range(vol):
		r = np.random.randint(size)
		site = locations[r]
		
		# random number for movement
		r2 = np.random.uniform(0,1)
		d = direction[r]
		
		move = 0
		while r2 >= direc[d][move]:
			move += 1
			
		if move == 4:
			direction[r] = circ[0][d]
		elif move == 5:
			direction[r] = circ[1][d]
		else:
			if move <= 4 and lattice[neighbour[site,move]] == 0:
				lattice[site] = 0
				nbr = neighbour[site, move]
				lattice[nbr] = 1
				locations[r] = nbr
	return lattice, locations, direction


Lstx = np.zeros((Lx,Lx), dtype = int)
for i in range(Lx):
	for j in range(Lx):
		Lstx[i,j] = (i + j) % Lx

@njit
def cal_density(lattice):
	xs = np.zeros(Lx)
	for i in range(Lx):
		index = pos_rev[i,:]
		xarr = lattice[index]
		xs[i] = sum(xarr)
	
	xv = np.zeros(Lx)
	for i in range(Lx):
		for j in range(L):
			xv[i] += xs[Lstx[i,j]]
	maxarr = max(xv)
	ind = np.argmax(xv)
	minarr = xv[Lstx[ind, 3*L]]
	min2 = min(xv)
	return maxarr, minarr, min2

@njit
def run():
	vmin = 0
	vmin2 = 0
	vmax = 0
	
	for en in range(ensemble):
		lattice = initialize()
		locations = sites(lattice, Ns)
		direction = np.zeros(Ns, dtype = np.int8)
		for ind in range(Ns):
			direction[ind] = np.random.randint(4)
		
		for t in range(tsat):
			lattice, locations, direction = movement(lattice, locations, Ns, direction)
			
		for t in range(tmax):
			lattice, locations, direction = movement(lattice, locations, Ns, direction)
			mmax, mmin, mmin2 = cal_density(lattice)
			
			vmin += mmin/tmax/ensemble
			vmin2 += mmin2/tmax/ensemble
			vmax += mmax/tmax /ensemble
		
	return vmax, vmin, vmin2, lattice
	
vmax, vmin, vmin2, lattice = run()
fname =f"2dataL{L}p{p}.csv"
file1 = open(fname, "a")  # append mode
data1 = str(p) + "," + str(omega) + "," + str(rho) + "," + str(vmax) + "," + str(vmin) + "," + str(vmin2) + "\n"
file1.write(data1)
file1.close()

make2D = np.zeros((Lx, Ly))
for i in range(Lx):
	for j in range(Ly):
		make2D[i,j] = lattice[i * Ly + j]
plt.imshow(make2D.T, cmap = 'binary')
fname = 'omega' + str(omega) + '.png'
plt.savefig(fname)
