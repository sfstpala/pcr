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

    def test_key_schedule(self):
        out = binascii.unhexlify(
            ("dd5bcb0018e922d494759d7c395d02d3"
             "c8446f8f77abf737685353eb89a1c9eb"
             "af3e30f9c095045938151575c3fb9098"
             "f8cb6274db99b80b1d2012a98ed48f0e"
             "25c3005a1cb85de076259839ab7198ab"
             "9dcbc183e8cb994b727b75be3180769c"
             "a1d3078dfa9169503ed9d4491dee4eb2"
             "8514a5495858096f596e4bcd66b10665"
             "5f40d59ec1b03b33738efa60b2255d31"
             "3477c7f764a41baceff90bf14f92b7cc"
             "ac4e95368d99b9eb78b8da8f81ffa795"
             "8c3c13f8c2388bb73f38576e65b7c446"
             "13c4b9c1dfb66579eddd8a280b9f7316"
             "ddd27820550126698efaadc64b64f66e"
             "f08f2e66d28ed143f3a237cf9de73559"
             "9ea36c525531b880ba124334f57b0b70"
             "d5a39e3dfcc50280bac4a6b5aa0dca7d"
             "370b1c1fe655916d97fd0d47ca1d72b8").encode())
        key = (b"\x1a\xda\x31\xd5\xcf\x68\x82\x21"
               b"\xc1\x09\x16\x39\x08\xeb\xe5\x1d"
               b"\xeb\xb4\x62\x27\xc6\xcc\x8b\x37"
               b"\x64\x19\x10\x83\x32\x22\x77\x2a")
        cip = bytes(n for n, _ in zip(key_stream(
            key_schedule(key)), range(288)))

        for n, (i, j) in enumerate(zip(out, cip)):
            self.assertEqual(bytes([i]), bytes([j]), n)
