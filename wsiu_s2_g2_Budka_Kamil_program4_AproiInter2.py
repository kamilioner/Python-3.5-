import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from numpy import array
import numpy.linalg as npl
from numpy import dot

def f_i(x,xf,yf,n):
    y=0
    for i in range(n):
        temp=1
        for j in range(n):
            if i!=j:
                temp*=(x-xf[j])/(xf[i]-xf[j])
        y+=+yf[i]*temp
    return y

def f_al(x,xf,yf,n):
    s1=0 
    s2=0 
    s3=0 
    s4=0 
    for i in range(n):
        s1+=yf[i]
        s2+=xf[i]*xf[i]
        s3+=xf[i]
        s4+=xf[i]*yf[i]
    a0=(s1*s2-s3*s4)/(n*s2-s3*s3)
    a1=(n*s4-s3*s1)/(n*s2-s3*s3)
    return a0+a1*x

def korel(xf,yf,n):
    s1=0 #suma 
    s2=0 #suma 
    s3=0 #suma 
    s4=0 #suma
    s5=0
    for i in range(n):
        s1+=xf[i]*yf[i]
        s2+=xf[i]
        s3+=xf[i]
        s4+=xf[i]*xf[i]
        s5+=yf[i]*yf[i]
    try:
        r=(n*s1-s2*s3)/(sqrt(n*s4-s2*s2)*sqrt(n*s5-s3*s3))
    except:
        r="wartość urojona"
    return r
n=int(input('Podaj ilosc punktów n='))
xf=[]
yf=[]
for i in range(n):
    xf.append(float(input('Podaj x'+str(i+1)+'=')))
    yf.append(float(input('Podaj y'+str(i+1)+'=')))
#podajemy argumenty w tym wypadku 100 od argumentu najmniejszego do najwiekszego, 5% marginesu
x=np.arange(min(xf)-5*((max(xf)-min(xf))/100),max(xf)+5*((max(xf)-min(xf))/100),(max(xf)-min(xf))/100)


plt.subplot(211)
plt.plot(x,f_i(x,xf,yf,n),'k',xf,yf,'bo')
plt.subplot(212)
plt.plot(x,f_al(x,xf,yf,n),'k',xf,yf,'bo')
print('Współczynnik korelacji liniowej='+str(korel(xf,yf,n)))
plt.show()


