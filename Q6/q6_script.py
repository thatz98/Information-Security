#!/usr/bin/python

import sys
import hashlib

def get_pbkdf2(data, salt, iterations, hashfunc, keylen):

    data = data.encode()
    salt = salt.encode()

    if callable(hashfunc):
        _test_hash = hashfunc()
        hash_name = getattr(_test_hash, "name", None)
    else:
        hash_name = hashfunc
    return hashlib.pbkdf2_hmac(hash_name, data, salt, iterations, keylen)

def main(argv):
    print(str(get_pbkdf2(argv, "Km5d5ivMy8iexuHcZrsD", 200000, "sha512", None).hex()))

main(sys.argv[1])
