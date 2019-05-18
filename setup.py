import numpy as np
from ntru import *

while True:
	try:
		F = generatePolynomial(N)
		Fp, Fq = invertPolynomial(F,p,q)
		break
	except sym.polys.polyerrors.NotInvertible:
		pass

G = generatePolynomial(N)
xN = toPoly(xN)

h = sym.rem(Fq.mul_ground(p).mul(G), xN, symmetric=False, modulus = q)

# savePolynomialListToFile([F,Fp], "./private_key.txt")
# savePolynomialToFile(h, "./public_key.txt")

print(h)

#todo save private and public key