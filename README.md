# PCR - Python Cryptography Experimentation Kit

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

Additional modules (especially regarding Public-Key cryptography)
are in the works.

Note: PCR does not (and will never) work with Python 2.x.

## Installation

The easiest way to install PCR is using PIP:

    git clone https://github.com/sfstpala/pcr.git
    cd pcr
    sudo pip3 install .

You can also type `make install` or build the Debian package
by running `debuild -b -tc -us -uc`.
