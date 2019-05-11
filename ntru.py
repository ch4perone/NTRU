import numpy as np
import csv
import random

#
# This file contains all functionality required for the NTRU cryptosystem
#

# public parameter setup
N = 11
p = 3
q = 32
xN = [0] * (N + 1)  # ring polynomial
xN[0] = 1
xN[N] = -1


def generatePolynomial(N):
    return np.array([random.randint(0, q - 1) for i in range(N)])


def savePolynomialToFile(e, path):
    with open(path, "w") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(e.astype(int))
    return 1


def savePolynomialListToFile(E, path):
    with open(path, "w") as outfile:
        writer = csv.writer(outfile)
        for e in E:
            writer.writerow(e.astype(int))
    return 1


def readMessageFromFile(path):
    with open(path, "r") as infile:
        msg = infile.read()  # TODO find a better way
        return msg


def readPolynomialFromFile(path):
    with open(path, "r") as infile:
        reader = csv.reader(infile)
        poly = np.array(list(reader)[0], dtype=int)
    return poly


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
    e_hat = np.polyadd(np.polymul(r, h), m)
    _, e = np.polydiv(e_hat, xN)
    e = (e % q).astype(int)
    return e
