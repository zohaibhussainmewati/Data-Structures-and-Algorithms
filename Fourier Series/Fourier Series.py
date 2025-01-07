import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.pyplot import *
import scipy.integrate as integrate

fig = figure(figsize=(7, 7), dpi=120)

def periodicf(li,lf,f,x):
    if x>=li and x<=lf :
        return f(x)
    elif x>lf:
        x_new=x-(lf-li)
        return periodicf(li,lf,f,x_new)
    elif x<(li):
        x_new=x+(lf-li)
        return periodicf(li,lf,f,x_new)

def sawtoothP(li,lf,x):
    return periodicf(li,lf,sawtooth,x)
def sawtooth(x):
    return x
def squareP(li,lf,x):
    return periodicf(li,lf,square,x)
def square(x):
    if x>0:
        return np.pi
    else:
        return -np.pi
def triangleP(li,lf,x):
    return periodicf(li,lf,triangle,x)
def triangle(x):
    if x>0:
        return x
    else:
        return -x
def cycloidP(li,lf,x):
    return periodicf(li,lf,cycloid,x)
def cycloid(x):
    return np.sqrt(np.pi**2-x**2)


def fourierCoeffs(li, lf, n, f):
    l = (lf-li)/2 
    a0=1/l*integrate.quad(lambda x: f(x), li, lf)[0]
    A = np.zeros((n))
    B = np.zeros((n))
    
    for i in range(1,n+1):
        A[i-1]=1/l*integrate.quad(lambda x: f(x)*np.cos(i*np.pi*x/l), li, lf)[0]
        B[i-1]=1/l*integrate.quad(lambda x: f(x)*np.sin(i*np.pi*x/l), li, lf)[0]

    return [a0/2.0, A, B]
def fourierSeries(coeffs,x,l,n):
    value = coeffs[0]
    for i in range(1,n+1):
        value = value + coeffs[1][i-1]*np.cos(i*np.pi*x/l) +  coeffs[2][i-1]*np.sin(i*np.pi*x/l)
    return value
    
if __name__ == "__main__":
    plt.style.use('seaborn')
    li = -np.pi
    lf = np.pi
    l = (lf-li)/2.0
    n = 1
    for n in range(1,10):

        plt.title('Fourier Series Approximation\nSawtooth Wave\n n = '+str(n))
        coeffsSawtooth = fourierCoeffs(li,lf,n,sawtooth)
        coeffsTriangle = fourierCoeffs(li,lf,n,triangle)
        coeffsSquare = fourierCoeffs(li,lf,n,square)
        coeffsCycloid = fourierCoeffs(li,lf,n,cycloid)

        step_size = 0.05
        x_l = -np.pi*2
        x_u = np.pi*2

        x = np.arange(x_l,x_u,step_size)
        y1 = [sawtoothP(li,lf,xi) for xi in x]
        y1_fourier = [fourierSeries(coeffsSawtooth,xi,l,n) for xi in x]
        y2 = [squareP(li,lf,xi) for xi in x]
        y2_fourier = [fourierSeries(coeffsSquare,xi,l,n) for xi in x]
        y3 = [triangleP(li,lf,xi) for xi in x]
        y3_fourier = [fourierSeries(coeffsTriangle,xi,l,n) for xi in x]
        y4 = [cycloidP(li,lf,xi) for xi in x]
        y4_fourier = [fourierSeries(coeffsCycloid,xi,l,n) for xi in x]

        x_plot =[]
        y_plot1 = []
        y_plot1_fourier = []
        y_plot2 = []
        y_plot2_fourier = []
        y_plot3 = []
        y_plot3_fourier = []
        y_plot4 = []
        y_plot4_fourier = []
    
        x_l_plot = x_l - 13
        x_u_plot = x_l_plot + 14
        plt.xlim(x_l_plot,x_u_plot)
        plt.ylim(-6,7)

        for i in range(x.size):
            
            x_plot.append(x[i])
            y_plot1.append(y1[i])
            y_plot2.append(y2[i])
            y_plot3.append(y3[i])
            y_plot4.append(y4[i])
            y_plot1_fourier.append(y1_fourier[i])
            y_plot2_fourier.append(y2_fourier[i])
            y_plot3_fourier.append(y3_fourier[i])
            y_plot4_fourier.append(y4_fourier[i])

            plt.plot(x_plot,y_plot1,c='darkkhaki',label='Sawtooth Wave')
            plt.plot(x_plot,y_plot1_fourier,c='forestgreen',label='Fourier Approximation')            
            x_l_plot = x_l_plot + step_size
            x_u_plot = x_u_plot + step_size
            plt.xlim(x_l_plot,x_u_plot)
            plt.pause(0.001)
            if i==0:
                plt.legend()

        
        plt.clf()
    
    plt.show()