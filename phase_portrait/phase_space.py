import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read data from CSV file into a Pandas DataFrame
file_path = '128data.csv'
df = pd.read_csv(file_path)

# Extract columns into arrays
omega = df['omega'].values
p = df['p'].values
order = df['ord'].values
ord2 = df['ord2'].values
ord4 = df['ord4'].values
f4 = df['f4'].values

print(max(p))
print(max(omega))


yarr=[.02,.0275,.08,.15,.235,.0414,.191]
xarr=[.018,.01985,.0247,.0235,.0199,.022,.022]

# Create contour plot
plt.figure(figsize=(10, 8))
contour = plt.tricontourf(omega, p, order, 1001, cmap='gnuplot',levels = np.linspace(0, 1, 1001))
cbar = plt.colorbar(contour, label='$\phi$ (Order parameter)')
plt.title('Phase Space Contour Plot for density = 0.5')
plt.ylabel('p',fontsize = 15)
plt.xlabel('$\omega$',fontsize = 15)
plt.scatter(xarr,yarr,s=50,edgecolors='black', facecolors='red')
plt.savefig('phase_space.png')
plt.clf()

'''
plt.figure(figsize=(10, 8))
contour = plt.tricontourf(omega, p, ord2-order**2,1001, cmap='gnuplot')
cbar = plt.colorbar(contour, label='$\chi (Suceptibility)$')
plt.title('Phase Space Contour Plot for density = 0.5')
plt.ylabel('p',fontsize = 15)
plt.xlabel('$\omega$',fontsize = 15)
plt.savefig('phase_space_sucep.png')
plt.clf()

plt.figure(figsize=(10, 8))
contour = plt.tricontourf(omega, p,1- ord4/3/ord2**2,1001, cmap='gnuplot')
cbar = plt.colorbar(contour, label='$Binder Cumulant$')
plt.title('Phase Space Contour Plot for density = 0.5')
plt.ylabel('p',fontsize = 15)
plt.xlabel('$\omega$',fontsize = 15)
plt.savefig('phase_space_BC.png')
plt.clf()

plt.figure(figsize=(10, 8))
contour = plt.tricontourf(omega, p, f4, 1001, cmap='gnuplot')
cbar = plt.colorbar(contour, label='$\phi$ (Order parameter)')
plt.title('Phase Space Contour Plot for density = 0.5')
plt.ylabel('p',fontsize = 15)
plt.xlabel('$\omega$',fontsize = 15)
plt.savefig('phase_space_f4.png')
plt.clf()
'''