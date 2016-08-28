import random
import time

Tab = []


def losowe(L):
    L =[]
    for i in range(0, 20000):
        L.append(random.choice(range(0, 1000000)))
    return L

def czesciowo_losowe(L):
    L =[]
    for i in range(0, 10000):
        L.append(random.choice(range(0, 1000000)))
    L.sort();
    for i in range(10001, 20000):
        L.append(random.choice(range(0, 1000000)))
    return L

def rosnaco(L):
    L =[]
    for i in range(0, 20000):
        L.append(random.choice(range(0, 1000000)))
    L.sort();
    return L

def malejaco(L):
    L =[]
    for i in range(0, 20000):
        L.append(random.choice(range(0, 1000000)))
    L.sort(reverse=True)
    return L


def Sortowanie_wstawianie(A):
    startm = int(round(time.time() * 1000))
    for i in range(1,len(A)):
        klucz = A[i]
        j = i - 1
        while j>=0 and A[j]>klucz:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = klucz
    stopm = int(round(time.time() * 1000))
    #print(A)
    return (stopm - startm)

def Sortowanie_wybor(A):
    startm = int(round(time.time() * 1000))
    for i in range(0,len(A)):
        klucz = A[i]
        k = i
        j = i + 1
        for j in range((i+1),len(A)):
            if klucz > A[j]:
                klucz = A[j]
                k = j
        A[k] = A[i]
        A[i] = klucz
    stopm = int(round(time.time() * 1000))
    #print(A)
    return (stopm - startm)

def Sortowanie_zamiana(A):
    startm = int(round(time.time() * 1000))
    for i in range (1,len(A)):
        klucz =  A[i]
        k = i
        j = i + 1
        for j in range(j, len(A)):
            if klucz > A[j]:
                klucz = A[j]
                k = j
            A[k] = A[i]
            A[i] = klucz
    stopm = int(round(time.time() * 1000))
    #print(A)
    return (stopm - startm)

def Part(A, a, b):
    x = a
    for i in range(a, b):
        if A[i] < A[b]:
            A[i],A[x] = A[x],A[i]
            x += 1
            
    A[x],A[b] = A[b],A[x]
    return x

def Quick_s(A, a, b):
    if a < b:
        x = Part(A, a, b)
        Quick_s(A, a, x -1)
        Quick_s(A, x + 1, b)

def Quick_sort(A):
    startm = int(round(time.time() * 1000))
    a = 0
    b = (len(A)-1)
    Quick_s(A, a, b)
    stopm = int(round(time.time() * 1000))
    #print(A)
    return (stopm - startm)

def Sortowanie_zliczanie(A):
    startm = int(round(time.time() * 1000))
    t = max(A) + 1
    tmp = [0] * (t)
    for i in A:
        tmp[i] += 1
    j = 0
    for a in range(t):
        for c in range(tmp[a]):
            A[j] = a
            j += 1
    stopm = int(round(time.time() * 1000))
    #print(A)
    return (stopm - startm)
    


#Tab = losowe(Tab)
#Tab = czesciowo_losowe(Tab)
#Tab = rosnaco(Tab)
#Tab = malejaco(Tab)
#print (Tab)
print("Czas sortowania przez wstawianie: ", Sortowanie_wstawianie(Tab))
#print("Czas sortowania przez zamiane:", Sortowanie_zamiana(Tab))
print("Czas sortowania przez wybor:", Sortowanie_wybor(Tab))
#print("Czas sortowania przez QuickSort:", Quick_sort(Tab))
print("Czas sortowania przez zliczanie", Sortowanie_zliczanie(Tab))

