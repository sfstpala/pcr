# PCR - Python Cryptography Experimentation Kit

[![Build](https://img.shields.io/travis/sfstpala/pcr.svg?style=flat-square)](https://travis-ci.org/sfstpala/pcr)
[![Coverage](https://img.shields.io/coveralls/sfstpala/pcr.svg?style=flat-square)](https://coveralls.io/r/sfstpala/pcr)

 - [Downloads](https://pypi.python.org/pypi/pcr/)
 - [Documentation](https://pythonhosted.org/pcr/)

This package provides pure python implementations of various
cryptographic algorithms and protocols. Since doing cryptography
in python is inherently slow, it is meant as a study aid and
experimentation kit.

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

You can also build the Debian package by running
`debuild -b -tc -us -uc` in the source tree.
