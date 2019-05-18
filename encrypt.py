import argparse
from ntru import *

parser = argparse.ArgumentParser(description='Encrypt message')
parser.add_argument('-m', "--message", metavar='MESSAGE',
                    help='File with message to encrypt', required=True)
parser.add_argument('-p', "--publicKey", metavar='KEY',
                    help="File with recipient's public key", required=True)
args = parser.parse_args()

#
# Load public key and message into binary polynomials
#

message = readMessageFromFile(args.message)
M = messageToBinaryPolynomials(message)
h = readPolynomialFromFile(args.publicKey)

#
# Encrypt character by character
#
E = np.array([[0] * N])
for m in M:
    r = generatePolynomial(N)  # blinding value #TODO (mod N^x - 1) ??
    e = encrypt(m, h, r)
    E = np.append(E, [e], axis=0)

E = np.delete(E, 0, axis=0)  # delete dummy row
savePolynomialListToFile(E, "./message_enc.txt")
