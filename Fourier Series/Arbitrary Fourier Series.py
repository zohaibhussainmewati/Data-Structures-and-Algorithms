import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
L=1.0
freq=2 
samples=1001
terms=50

x=np.linspace(-L,L,samples,endpoint=False)
F=lambda x: np.array([u**2 if 0<=u<=L else 1 if 0<u<0.5 else 0
for u in x])

f=lambda x: F(freq*x%(2*L)-L)

a0=1./L*simps(f(x),x)
an=lambda n:1.0/L*simps(f(x)*np.cos(1.*np.pi*n*x/L),x)
bn=lambda n:1.0/L*simps(f(x)*np.sin(1.*np.pi*n*x/L),x)

xp=x
s=a0/2.+sum([an(k)*np.cos(1.*np.pi*k*xp/L)+bn(k)*np.sin(1.*np.pi
*k*xp/L) for k in range(1,terms+1)])

plt.plot(xp,s,label="Fourier series")
plt.plot(xp,f(xp),label="Original wave")
plt.legend(loc='best',prop={'size':10})
plt.savefig("arb_ud.png")
plt.show()