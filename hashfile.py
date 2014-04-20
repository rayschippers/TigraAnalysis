__author__ = 'raymond'
import hashlib

def hashingfile(tempfile):
#Purpose: hash a file
    #hachlblocksize limits how many bytes to read in at once
    hashblocksize = 81960
    #set the hashing algorithm to use
    hash = hashlib.sha1()
    #open the file to hash as stream
    filetohash = open(tempfile, 'rb')

    #hash the file
    while True:
        buffer = filetohash.read(hashblocksize)
        hash.update(buffer)
        if not buffer:
            hash_result = hash.hexdigest()
            break

    filetohash.close()
    return hash_result
