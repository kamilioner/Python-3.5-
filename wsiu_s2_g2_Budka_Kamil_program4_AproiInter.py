import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from numpy import array
import numpy.linalg as npl
from numpy import dot

class pkt:
    def __init__(self, a, b):
        self.x = a
        self.y = b


n=int(input('Podaj ilosc punktów z przedziału od 2 do 10:'))
if n == 2:
    list = ['a', 'b']
if n == 3:
    list = ['a', 'b', 'c']
if n == 4:
    list = ['a', 'b', 'c', 'd']
if n == 5:
    list = ['a', 'b', 'c', 'd', 'e']
if n == 6:
    list = ['a', 'b','c', 'd', 'e', 'f']
if n == 7:
    list = ['a', 'b', 'c',' d', 'e', 'f', 'g']
if n == 8:
    list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
if n == 9:
    list = ['a', 'b', 'c' ,'d' ,'e' ,'f' ,'g' ,'h' ,'i']
if n == 10:
    list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

for name in list:
    globals()[name] = pkt(0,0)
    try:
        print("Podaj współrzędne punktu %d" %(i+1))
        
        list[i].x,list[i].y = map(int,sys.stdin.readline().split())
    except:
        print("Podaj inne wartości!")

#a = pkt(0,0)
#b = pkt(0,0)
#z = False
#while not z:
#    try:
#        print("Podaj współrzędne punktu ")
#        a.x,a.y = map(int,sys.stdin.readline().split())
#        print("Podaj współrzędne punktu b")
#        b.x,b.y = map(int,sys.stdin.readline().split())
#        z  = True
#    except:
#        print("Podaj inne wartości!")




c=[[p[0].x,p[0].y],[p[0].x,p[0].y]]
plt.plot(*zip(*c))
c=[[p[0].x,p[0].y],[p[0].x,p[0].y]]
plt.plot(*zip(*c), marker='o', color='r', ls='')
d=[[-20,-20],[20,20]]
plt.plot(*zip(*d), ls='')


pylab.xlabel("X")
pylab.ylabel("Y")

plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.grid(True)
plt.show()
