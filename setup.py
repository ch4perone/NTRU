import numpy as np
from ntru import *

f = np.array([-1,1,0,0,1,0, -1, 0,1,1,-1])
g = np.array([-1,0,-1,0,0,1,0,1,1,0,-1])

Fp = 1 #todo
Fq = np.array([30, 18, 20, 22, 16, 15, 4, 16, 6, 9, 5]) #todo euclid inverse

xN = np.array([1, 0,0,0,0,0,0,0,0,0,0,-1])


_, rem = np.polydiv( np.polymul(p * Fq, g), xN)
h = rem % q
h = h.astype(int)

savePolynomialToFile(f, "./private_key.txt")
savePolynomialToFile(h, "./public_key.txt")

print(h)

#todo save private and public key