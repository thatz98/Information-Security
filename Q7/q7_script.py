#!/usr/bin/python

import sys
import hashlib
import os

def get_pbkdf2(data, iterations, hashfunc, keylen):

    data = data.encode()
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')

    if callable(hashfunc):
        _test_hash = hashfunc()
        hash_name = getattr(_test_hash, "name", None)
    else:
        hash_name = hashfunc
    return hashlib.pbkdf2_hmac(hash_name, data, salt, iterations, keylen)

def main(argv):
    print(str(get_pbkdf2(argv, 200000, "sha512", None).hex()))

main(sys.argv[1])
