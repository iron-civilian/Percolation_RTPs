import numpy as np
import matplotlib.pyplot as plt

'''
for p in [0.15]:
    data=np.loadtxt(f"dataL50p{p}.csv",delimiter=",")
    data=np.array(sorted(data,key=lambda x: x[1]))[:11]
    y1=list(data[:,1])
    x1=list(data[:,3]/2/50/50)
    x2=list((data[:,4]+data[:,5])/4/50/50)+[0.5]
    x=sorted(x1+x2)
    y=y1+[0.0235]+sorted(y1,reverse=True)
    #with open("data.txt","w") as fl:
    #    for i in range(len(x)):
    #        fl.write(f"{x[i]},{y[i]}\n")
    plt.plot(x,y,marker="o",label=f"p={p}")

'''
def f(x,a,b,c,d,e,f,g,h,i):
    return a+b*x+c*x**2+d*x**3+e*x**4+f*x**5+g*x**6+h*x**7+i*x**8

a1=-0.000453338
b1=0.0796217
c1=0.505197
d1=-5.44833
e1=35.7378
f1=-153.635
g1=368.464
h1=-446.11
i1=213.589

a2=-1.56963
b2=17.3932
c2=-82.3299
d2=220.556
e2=-365.315
f2=382.381
g2=-246.441
h2=89.2686
i2=-13.9454

def g(x):
    return (x-.5)**6*1.7
def h(x):
    return (.5-x)**3.5*.34


data1=np.loadtxt(f"data.txt")[:11]
data2=np.loadtxt(f"data2.txt")[9:]
x=np.append(data1[:,0],data2[:,0])
y=np.append(data1[:,1],data2[:,1])

xx1=np.linspace(0,0.265,1000)

xxx1=np.linspace(0.265,0.5,1000)
yyy1=f(xxx1,a1,b1,c1,d1,e1,f1,g1,h1,i1)


yy1=f(xx1,a1,b1,c1,d1,e1,f1,g1,h1,i1)
xx2=np.linspace(0.81,1,1000)
yy2=f(xx2,a2,b2,c2,d2,e2,f2,g2,h2,i2)

xxx2=np.linspace(0.5,0.81,1000)
yyy2=f(xxx2,a2,b2,c2,d2,e2,f2,g2,h2,i2)


xxx=np.linspace(0.5,1,1000)
xxx1=np.linspace(0,0.5,1000)

plt.plot(xxx,.0235-g(xxx),color='black',lw=2)
plt.plot(xxx1,.0235-h(xxx1),color='black',lw=2)

#plt.plot(xx1,yy1,color='black',lw=2)
#plt.plot(xx2,yy2,color='black',lw=2)
#plt.plot(xxx1,yyy1,linestyle='dashed',lw=2,color='black')
#plt.plot(xxx2,yyy2,linestyle='dashed',lw=2,color='black')

plt.scatter(x,y,color='red',s=150,edgecolor='black',zorder=2)
plt.scatter([0.5],[0.0235],color='blue',marker='*',s=600,edgecolor='black',zorder=2)
plt.xlim(0,1)
plt.ylim(0.001,0.03)
#plt.legend()
plt.xticks(size=15)
plt.yticks(size=15)
plt.ylabel(r'$\omega$',size=20)
plt.xlabel(r'Mean Density $\langle \rho \rangle$',size=20)
plt.tight_layout()
#plt.savefig('phasecoexistence.png')
plt.show()


