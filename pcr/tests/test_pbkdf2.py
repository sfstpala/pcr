# Copyright (c) 2013 Stefano Palazzo <stefano.palazzo@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import unittest
import hashlib

from pcr.pbkdf2 import pbkdf2


class PBKDF2Test(unittest.TestCase):

    def test_pbkdf2(self):
        '''
        PBKDF2 HMAC-SHA1 Test Vectors:
            http://tools.ietf.org/html/rfc6070

        '''
        # One of the test vectors has been removed because it takes
        # too long to calculate. This was a test vector of 2^24 iterations.
        # Since there is no difference between integers and long integers
        # in python3, this will work as well as the others.
        rfc6070_test_vectors = (
            (b"password", b"salt", 1, 20),
            (b"password", b"salt", 2, 20),
            (b"password", b"salt", 4096, 20),
            (b"passwordPASSWORDpassword",
             b"saltSALTsaltSALTsaltSALTsaltSALTsalt", 4096, 25),
            (b"pass\0word", b"sa\0lt", 4096, 16),
        )
        rfc6070_results = (
            b"\x0c\x60\xc8\x0f\x96\x1f\x0e\x71\xf3\xa9" +
            b"\xb5\x24\xaf\x60\x12\x06\x2f\xe0\x37\xa6",
            b"\xea\x6c\x01\x4d\xc7\x2d\x6f\x8c\xcd\x1e" +
            b"\xd9\x2a\xce\x1d\x41\xf0\xd8\xde\x89\x57",
            b"\x4b\x00\x79\x01\xb7\x65\x48\x9a\xbe\xad" +
            b"\x49\xd9\x26\xf7\x21\xd0\x65\xa4\x29\xc1",
            b"\x3d\x2e\xec\x4f\xe4\x1c\x84\x9b\x80\xc8" +
            b"\xd8\x36\x62\xc0\xe4\x4a\x8b\x29\x1a\x96" +
            b"\x4c\xf2\xf0\x70\x38",
            b"\x56\xfa\x6a\xa7\x55\x48\x09\x9d\xcc\x37" +
            b"\xd7\xf0\x34\x25\xe0\xc3",
        )
        for v, r in zip(rfc6070_test_vectors, rfc6070_results):
            self.assertEqual(pbkdf2(hashlib.sha1, *v), r, v)
