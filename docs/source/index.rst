.. pcr documentation master file, created by
   sphinx-quickstart on Tue Jan 14 04:39:01 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pcr's documentation!
===============================

AES
===
.. automodule:: pcr.aes
.. autoclass:: pcr.aes.AES
   :members: xor, rotate, rijndael_key_schedule, encrypt, decrypt, start, get_round_key, add_round_key, main, sub_bytes, shift_rows, mix_columns

CBC
===
.. automodule:: pcr.cbc
.. autoclass:: pcr.cbc.CBC
   :members:
   :undoc-members:

Diffie-Hellman
==============
.. automodule:: pcr.diffie_hellman
.. autoclass:: pcr.diffie_hellman.DiffieHellman
   :members:
   :undoc-members:

HOTP (Two-Factor Authentication)
================================
.. automodule:: pcr.hotp
.. autofunction:: pcr.hotp.get_token
.. autofunction:: pcr.hotp.new_secret

Maths
=====
.. automodule:: pcr.maths
.. autofunction:: pcr.maths.is_prime
.. autofunction:: pcr.maths.get_prime
.. autofunction:: pcr.maths.phi
.. autofunction:: pcr.maths.mult_inv
.. autofunction:: pcr.maths.make_rsa_keys

PBKDF2
======
.. automodule:: pcr.pbkdf2
.. autofunction:: pcr.pbkdf2.pbkdf2

PKCS7
=====
.. automodule:: pcr.pkcs7
.. autofunction:: pcr.pkcs7.pad
.. autofunction:: pcr.pkcs7.unpad
.. autofunction:: pcr.pkcs7.check_padding

RC4
===
.. automodule:: pcr.rc4
.. autofunction:: pcr.rc4.key_schedule
.. autofunction:: pcr.rc4.key_stream

RFC 3526
========
.. automodule:: pcr.rfc3526

XTEA
====
.. automodule:: pcr.xtea
.. autofunction:: pcr.xtea.encrypt
.. autofunction:: pcr.xtea.decrypt


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

