import numpy as np

N = 11
p = 3
q = 32

f = np.array([-1,1,0,0,1,0, -1, 0,1,1,-1])
g = np.array([-1,0,-1,0,0,1,0,1,1,0,-1])

Fp = 1 #todo
Fq = np.array([30, 18, 20, 22, 16, 15, 4, 16, 6, 9, 5]) #todo euclid inverse

xN = np.array([1, 0,0,0,0,0,0,0,0,0,0,-1])


_, rem = np.polydiv( np.polymul(p * Fq, g), xN)
h = rem % q
print(h)