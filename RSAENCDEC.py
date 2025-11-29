#!/usr/bin/env python
#-*- coding: utf-8 -*-
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto import Random
import base64
import StringIO

# passphrase, random string => private key, public key pair
# encrypt with public key
# decrypt with pem, passphrase

def gen_key_pair(passpharse):
    random_generator = Random.new().read
    key = RSA.generate(2048, random_generator)
    return key.exportKey(passphrase=passphrase), key.publickey().exportKey()

def rsa_encrypt(message, pub):
    keystream = StringIO.StringIO(pub)
    pubkey = RSA.importKey(keystream.read())
    h = SHA.new(message)
    cipher = PKCS1_v1_5.new(pubkey)
    return base64.encodestring(cipher.encrypt(message+h.digest()))

def rsa_decrypt(ciphertext, pem, passphrase):
    ciphertext = base64.decodestring(ciphertext)
    keystream = StringIO.StringIO(pem)
    pemkey = RSA.importKey(keystream.read(), passphrase=passphrase)
    dsize = SHA.digest_size
    sentinel = Random.new().read(15+dsize)
    cipher = PKCS1_v1_5.new(pemkey)
    message = cipher.decrypt(ciphertext, sentinel)
    digest = SHA.new(message[:-dsize]).digest()
    if digest == message[-dsize:]:
        return message[:-dsize]
    else:
        raise ValueError('Cannot decrypt message')


if __name__ == '__main__':
    message = 'To be encrypted'
    passphrase = 'Your Passphrase'

    pem, pub = gen_key_pair(passphrase)
    print 'Private Key:\n%s\n' % pem
    print 'Public Key:\n%s\n' % pub
    #encdata = rsa_encrypt(message, pub)
    #print 'Encrypted Message:\n', encdata
    encdata = 'PWMb3oUhC0ouw/zkRcIUZCmQ0lSaLUcQTBtp9KcrpnsRerTgb4Yoa8ZhhIEI7iO7cPdSjlDv8CN6xdtn94ut15p6kJW7tB3l+EEJMR5rZOlfmsI4A/oWq1WsD/eaEFbocgatV71/x7EUG38Tj5xGfKaGN/8VIj9EiPXv0rIaIl+ZgYtrAIKdl1Z9m1htK0g4+UcFbxKhORDULGsC9lcmSkKEbdT6UmHh8r6jmT9CDvfdbqu07R69/rOpkaIrqxkx+LMtd4blyBZZwQxbgVtO+/h8xPivKxOvhchHq95IsQJPZ0RGrPxPgsCgm0Xdv9PuTNnhEAQOhVyikcABlsC9tg=='
    decdata = rsa_decrypt(encdata, pem, passphrase)
print 'Decrypted Message:\n', decdata