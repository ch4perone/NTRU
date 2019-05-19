import numpy as np
import csv
import random
import sympy as sym
import dill


#
# This file contains all functionality required for the NTRU cryptosystem
#

# public parameter setup
N = 11            # 251 is used in most commercial applications, for improved security can become 347 or better 503 (must be prime)
p = 3               # most commonly used, needs to be relatively small 
q = 61          # must be relatively prime to p and much larger than p              

xN = [0] * (N + 1)  # ring polynomial (x^N - 1)
xN[0] = 1
xN[N] = -1

def toPoly(poly):
    x = sym.Symbol('x')
    f = 0
    for i in range(len(poly)):
        f += (x**i)*(poly[N-1-i])
    return sym.poly(f)


def generatePolynomial(N):
    poly = np.array([random.randint(-1, 1) for i in range(N)])
    return toPoly(poly)


def invertPolynomial(f,p,q):
    x = sym.Symbol('x')
    Fp = sym.polys.polytools.invert(f,x**N-1,domain=sym.GF(p, symmetric=False))
    Fq = sym.polys.polytools.invert(f,x**N-1,domain=sym.GF(q, symmetric=False))
    return Fp, Fq


def savePolynomialToFile(e, path):
    dill.dump(e, open(path, "wb"))
    return


def readMessageFromFile(path):
    with open(path, "r") as infile:
        msg = infile.read()  # TODO find a better way
        return msg


def readPolynomialFromFile(path):
    return dill.load(open(path, "rb"))


def characterFromBinaryPolynomial(poly):
    b = ''.join([str(x) for x in poly])
    return chr(int(b, 2))


def characterToBinaryPolynomial(char):  # TODO find a better way
    poly = [0] * N
    bitstring = format(ord(char), 'b')
    for i in range(len(bitstring)):
        if bitstring[i] == '1':
            poly[i + (N - len(bitstring))] = 1
    return poly


def messageToBinaryPolynomials(msg):
    M = np.array([])
    for char in msg:
        m = characterToBinaryPolynomial(char)
        if M.size == 0:
            M = np.array([m])
        else:
            M = np.append(M, [m], axis=0)
    return M


def encrypt(m, h, r):
    e = toPoly(r).mul(toPoly(h))
    e = e.add(toPoly(m))
    e = sym.rem(e, xN, symmetric=False, modulus = q)
    return e

def decrypt(f, e, fp):
    a = toPoly(f).mul(toPoly(e))
    a = sym.rem(a, xN, symmetric=False, modulus = q)
    #TODO CENTERING -q/2 q/2
    m = toPoly(fp).mul(a)
    m = sym.rem(m, xN, symmetric=False, modulus = p)
    return m
