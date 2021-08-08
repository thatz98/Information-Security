#!/usr/bin/python

import sys
import hashlib
import os
import binascii

def get_hash(data, iterations, hashfunc, keylen):

    data = data.encode()
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')

    if callable(hashfunc):
        _test_hash = hashfunc()
        hash_name = getattr(_test_hash, "name", None)
    else:
        hash_name = hashfunc
    return (salt + binascii.hexlify(hashlib.pbkdf2_hmac(hash_name, data, salt, iterations, keylen))).decode('ascii')

def main(argv):
    print(str(get_hash(argv, 200000, "sha512", None)))

main(sys.argv[1])
