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
import binascii

from pcr.rc4 import key_schedule, key_stream


class RC4Test(unittest.TestCase):

    def test_key_schedule_256(self):
        '''
        RC4 Test Vectors (256 bit key):
            http://tools.ietf.org/html/rfc6229

        '''
        key = (b'\x1a\xda1\xd5\xcfh\x82!\xc1\t\x169\x08\xeb' +
               b'\xe5\x1d\xeb\xb4b\'\xc6\xcc\x8b7d\x19\x10\x832"w*')
        cip = bytes(n for n, _ in zip(key_stream(
            key_schedule(key)), range(4096 + 16)))
        self.assertEqual(cip[0:0 + 16], binascii.unhexlify(
            b"dd5bcb0018e922d494759d7c395d02d3"))
        self.assertEqual(cip[16:16 + 16], binascii.unhexlify(
            b"c8446f8f77abf737685353eb89a1c9eb"))
        self.assertEqual(cip[240:240 + 16], binascii.unhexlify(
            b"af3e30f9c095045938151575c3fb9098"))
        self.assertEqual(cip[256:256 + 16], binascii.unhexlify(
            b"f8cb6274db99b80b1d2012a98ed48f0e"))
        self.assertEqual(cip[496:496 + 16], binascii.unhexlify(
            b"25c3005a1cb85de076259839ab7198ab"))
        self.assertEqual(cip[512:512 + 16], binascii.unhexlify(
            b"9dcbc183e8cb994b727b75be3180769c"))
        self.assertEqual(cip[752:752 + 16], binascii.unhexlify(
            b"a1d3078dfa9169503ed9d4491dee4eb2"))
        self.assertEqual(cip[768:768 + 16], binascii.unhexlify(
            b"8514a5495858096f596e4bcd66b10665"))
        self.assertEqual(cip[1008:1008 + 16], binascii.unhexlify(
            b"5f40d59ec1b03b33738efa60b2255d31"))
        self.assertEqual(cip[1024:1024 + 16], binascii.unhexlify(
            b"3477c7f764a41baceff90bf14f92b7cc"))
        self.assertEqual(cip[1520:1520 + 16], binascii.unhexlify(
            b"ac4e95368d99b9eb78b8da8f81ffa795"))
        self.assertEqual(cip[1536:1536 + 16], binascii.unhexlify(
            b"8c3c13f8c2388bb73f38576e65b7c446"))
        self.assertEqual(cip[2032:2032 + 16], binascii.unhexlify(
            b"13c4b9c1dfb66579eddd8a280b9f7316"))
        self.assertEqual(cip[2048:2048 + 16], binascii.unhexlify(
            b"ddd27820550126698efaadc64b64f66e"))
        self.assertEqual(cip[3056:3056 + 16], binascii.unhexlify(
            b"f08f2e66d28ed143f3a237cf9de73559"))
        self.assertEqual(cip[3072:3072 + 16], binascii.unhexlify(
            b"9ea36c525531b880ba124334f57b0b70"))
        self.assertEqual(cip[4080:4080 + 16], binascii.unhexlify(
            b"d5a39e3dfcc50280bac4a6b5aa0dca7d"))
        self.assertEqual(cip[4096:4096 + 16], binascii.unhexlify(
            b"370b1c1fe655916d97fd0d47ca1d72b8"))
