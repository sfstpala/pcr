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

from pcr.xtea import encrypt, decrypt


class XTEATest(unittest.TestCase):

    # test vectors from <www.freemedialibrary.com/index.php/XTEA_test_vectors>

    def test_encrypt(self):
        self.assertEqual(encrypt(b"\x41\x42\x43\x44\x45\x46\x47\x48",
                                 b"\x00\x01\x02\x03\x04\x05\x06\x07"
                                 b"\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"),
                         b"\x49\x7d\xf3\xd0\x72\x61\x2c\xb5")
        self.assertEqual(encrypt(b"\x41\x41\x41\x41\x41\x41\x41\x41",
                                 b"\x00\x01\x02\x03\x04\x05\x06\x07"
                                 b"\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"),
                         b"\xe7\x8f\x2d\x13\x74\x43\x41\xd8")
        self.assertEqual(encrypt(b"\x5a\x5b\x6e\x27\x89\x48\xd7\x7f",
                                 b"\x00\x01\x02\x03\x04\x05\x06\x07"
                                 b"\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"),
                         b"\x41\x41\x41\x41\x41\x41\x41\x41")
        self.assertEqual(encrypt(b"\x41\x42\x43\x44\x45\x46\x47\x48",
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"),
                         b"\xa0\x39\x05\x89\xf8\xb8\xef\xa5")
        self.assertEqual(encrypt(b"\x41\x41\x41\x41\x41\x41\x41\x41",
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"),
                         b"\xed\x23\x37\x5a\x82\x1a\x8c\x2d")
        self.assertEqual(encrypt(b"\x70\xe1\x22\x5d\x6e\x4e\x76\x55",
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"),
                         b"\x41\x41\x41\x41\x41\x41\x41\x41")

    def test_decrypt(self):
        self.assertEqual(decrypt(b"\x49\x7d\xf3\xd0\x72\x61\x2c\xb5",
                                 b"\x00\x01\x02\x03\x04\x05\x06\x07"
                                 b"\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"),
                         b"\x41\x42\x43\x44\x45\x46\x47\x48",)
        self.assertEqual(decrypt(b"\xe7\x8f\x2d\x13\x74\x43\x41\xd8",
                                 b"\x00\x01\x02\x03\x04\x05\x06\x07"
                                 b"\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"),
                         b"\x41\x41\x41\x41\x41\x41\x41\x41",)
        self.assertEqual(decrypt(b"\x41\x41\x41\x41\x41\x41\x41\x41",
                                 b"\x00\x01\x02\x03\x04\x05\x06\x07"
                                 b"\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f"),
                         b"\x5a\x5b\x6e\x27\x89\x48\xd7\x7f",)
        self.assertEqual(decrypt(b"\xa0\x39\x05\x89\xf8\xb8\xef\xa5",
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"),
                         b"\x41\x42\x43\x44\x45\x46\x47\x48",)
        self.assertEqual(decrypt(b"\xed\x23\x37\x5a\x82\x1a\x8c\x2d",
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"),
                         b"\x41\x41\x41\x41\x41\x41\x41\x41",)
        self.assertEqual(decrypt(b"\x41\x41\x41\x41\x41\x41\x41\x41",
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"),
                         b"\x70\xe1\x22\x5d\x6e\x4e\x76\x55",)
