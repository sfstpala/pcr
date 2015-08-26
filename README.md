# PCR - Python Cryptography Experimentation Kit

[![Build](https://img.shields.io/travis/sfstpala/pcr.svg?style=flat-square)](https://travis-ci.org/sfstpala/pcr)
[![Coverage](https://img.shields.io/coveralls/sfstpala/pcr.svg?style=flat-square)](https://coveralls.io/r/sfstpala/pcr)
[![PyPI](https://img.shields.io/pypi/v/pcr.svg?style=flat-square)](https://pypi.python.org/pypi/pcr)
![Audited](https://img.shields.io/badge/audited-no-red.svg?style=flat-square)

 - [**Downloads**](https://pypi.python.org/pypi/pcr/)
 - [**API Reference**](https://pythonhosted.org/pcr/)

This package provides pure python implementations of various
cryptographic algorithms and protocols. Since doing cryptography
in Python is inherently slow, it is meant as a study aid and
experimentation kit.

## Before you use PCR

You should know:

  - AES encryption in PCR is *slow*
  - PCR has not been independently audited
  - Using a cryptographic library securely is difficult

Make sure you read and understand this document before using PCR.

Currently, PCR provides the following:

 - AES
 - Cipher-Block Chaining Mode of Operation
 - PKCS7 Padding
 - PBKDF2 (Key Derivation)
 - Diffie-Hellman Key Exchange (with RFC3526 groups)
 - RC4 (Stream Cipher)
 - HOTP (e.g. for Google Authenticator)

Additional modules (especially regarding Public-Key cryptography)
are in the works.

Note: PCR does not (and will never) work with Python 2.x.

## Installation

The easiest way to install PCR is using PIP:

    sudo pip3 install pcr

## Hacking

If you have cloned this repository, you can buld pcr in a virtualenv
and run the test suite like this:

    make test

### Development

PCR comes with a makefile that builds a virtualenv in your working directory.
Assuming you have `make`, `curl`, and `python3`, you can run the test suite
by typing

    make test doctests

And you can build wheels by typing

    make wheels

The process for making a release is as follows:

    make test doctest docs

If everything checks out, update the version number in `setup.py` and
make a release commit:

    git commit -am "Release <version-number>"
    git push origin master

Finally upload the distribution to pypi

    bin/python setup.py bdist_wheel sdist upload
    bin/python setup.py upload_docs --upload-dir=docs/pcr

## Examples

### AES Encryption

Here's an example of encrypting some data using AES:

    >>> import os
    >>> import pcr.aes
    >>> import pcr.cbc
    >>> import pcr.pkcs7
    >>> plaintext = 'hello world!'

First we need to encode and pad our plaintext. Padding is a critical step
that makes the length of our data divisble by the block size of the cipher.
Note that padding has security implications, so do not invent your own. We
use PKCS7 padding.

    >>> plaintext = plaintext.encode()
    >>> plaintext = pcr.pkcs7.pad(plaintext, pcr.aes.AES.block_size)
    >>> plaintext
    b'hello world!\x04\x04\x04\x04'

Next we instantiate of mode of operation, which lets us use AES on arbitrary
length data. This is where we need our initialization vector (IV). The IV is
not a secret. With CBC, each block is xored with the previous block so that
there are no discernable patterns in your ciphertext. For the first round,
when no previous block is available, the IV is used. The IV must be random
and you must never use the same IV twice:

    >>> iv = b'\xFF' * 16  # actually use this: os.urandom(pcr.aes.AES.block_size)
    >>> key = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
    >>> cbc = pcr.cbc.CBC(pcr.aes.AES, iv)
    >>> ciphertext = cbc.encrypt(plaintext, key)
    >>> ciphertext
    b'H\x81\xf3M\x1d\x1d\x89BouX#\x0b\n&\x84'

And decryption works exactly the same way:

    >>> plaintext = cbc.decrypt(ciphertext, key)
    >>> plaintext
    b'hello world!\x04\x04\x04\x04'

    >>> pcr.pkcs7.check_padding(plaintext, pcr.aes.AES.block_size)
    >>> pcr.pkcs7.unpad(plaintext).decode()
    'hello world!'

The length of your key determines which variant of AES is used. A 16 byte key is
AES128, 24 bytes is AES192 and 32 bytes AES256.

Always call `pcr.pkcs7.check_padding()` to make sure of the cipher text integrity.

The encrypted object contains not only the ciphertext but also the IV and the key
derivation parameters, which we'll look at next.

### PBKDF2 - Keys are not the same as passwords

In the example above, we used a 16 byte key (bytes counting up from 0 to 15). To
actually do encryption, we need to derive a key from a password. Do NOT use user
input as the key for AES encryption. If you want to build a secury crypto system,
you absolutely must derive the key.

PCR gives you PBKDF2 ("password-based key derivation function"). It works by stretching
the key, e.g. repeatedly hashing it and it uses HMAC to do this. PBKDF2 is purposefully
slow.

    >>> import hashlib
    >>> import pcr.pbkdf2
    >>> password = "correcthorsebatterystaple"

Let's set up our parameters:

    >>> digestmod = hashlib.sha256
    >>> salt = b'\xFF' * 16  # actually use this: os.urandom(32)
    >>> count = 1000  # actually make this as large as you can tolerate
    >>> dk_length = 32  # make a 32 byte key for AES256

And finally derive our key.

    >>> key = pcr.pbkdf2.pbkdf2(digestmod, password.encode(), salt, count, dk_length)
    >>> key
    b'\x8d_(d6~j1rJ\xe9\x13\xb0\xa7I\x1c\xd7\xeda\xa0\xf4~O\x81M`T\xd7\xfcC\x8b\xa6'

The only secret here is the password. When you store the encrypted object somewhere, you
need to also store all of the parameters used to generate the key, so you can do the
derivation again when you're decrypting. Do not use fixed parameters, you will need to
increase the strength of your keys at some point.

In 2015, a good value for the number of iterations of pbkdf2 is 128,000. This takes about
a second on a reasonable machine. Double this value every 18 months.

### Authentication

Encryption always needs authentication. Without authentication, the ciphertext can be
modified and the entegrity of your decryption is broken.

The recommended method to authenticate encryption is *Encrypt-then-MAC*, where we run
an HMAC on the ciphertext after encryting and before decrypting.

    >>> import hmac
    >>> import hashlib
    >>> digestmod = hashlib.sha256
    >>> mac = hmac.new(key, ciphertext).digest()
    >>> mac
    b'\x06\xf2[K\xc0\xa2Hy_|\x84\x05\xcb\xd2\x96\xfd'

The mac is stored along with your ciphertext, iv, and key derivation parameters. It is
not a secret.

Before decrypting the message, we check the message authentication code:

    >>> hmac.compare_digest(mac, hmac.new(key, ciphertext).digest())
    True

### Comparing MACs

We never compare the results of an HMAC using the `==` operator; instead we
use  `hmac.compare_digest()` from the hmac module. In simple terms, if we were to
compare message authentication code using `==`, an attacker could essentially see
how many bytes of the MAC are correct by seeing how long the comparison takes.

The `compare_digest()` function essentially goes through the values one byte at a
time and continues comparing even if it knows they are unequal, ensuring that each
comparison takes the same amount of time.

### AES – Full Example

    >>> password = "correcthorsebatterystaple"
    >>> plaintext = "hello world!"

    >>> import hmac
    >>> import hashlib
    >>> import os
    >>> import pcr.aes
    >>> import pcr.cbc
    >>> import pcr.pkcs7
    >>> import pcr.pbkdf2

#### Encryption

    >>> digestmod = hashlib.sha256
    >>> salt = os.urandom(32)
    >>> count = 128000
    >>> dk_length = 32
    >>> key = pcr.pbkdf2.pbkdf2(digestmod, password.encode(), salt, count, dk_length)
    >>> plaintext = plaintext.encode()
    >>> plaintext = pcr.pkcs7.pad(plaintext, pcr.aes.AES.block_size)

    >>> cbc = pcr.cbc.CBC(pcr.aes.AES, iv)
    >>> ciphertext = cbc.encrypt(plaintext, key)
    >>> mac = hmac.new(key, ciphertext).digest()

#### Decryption

    >>> assert hmac.compare_digest(mac, hmac.new(key, ciphertext).digest())
    >>> plaintext = cbc.decrypt(ciphertext, key)
    >>> pcr.pkcs7.check_padding(plaintext, pcr.aes.AES.block_size)
    >>> plaintext = pcr.pkcs7.unpad(plaintext)
    >>> plaintext = plaintext.decode()
    >>> plaintext
    'hello world!'
