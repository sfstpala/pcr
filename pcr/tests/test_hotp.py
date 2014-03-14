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
import base64

from pcr.hotp import get_token, new_secret


class HOTPTest(unittest.TestCase):

    def test_get_token(self):
        '''
        HOTP Algorithm Test Values:
            http://tools.ietf.org/html/rfc4226

        '''
        key = "gEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ"
        # the key is the secret from appendix d of rfc4226
        # converted to base 32 and with the first charcter
        # converted to lowercase.
        self.assertEqual(get_token(key, 0), "755224")
        self.assertEqual(get_token(key, 1), "287082")
        self.assertEqual(get_token(key, 2), "359152")
        self.assertEqual(get_token(key, 3), "969429")
        self.assertEqual(get_token(key, 4), "338314")
        self.assertEqual(get_token(key, 5), "254676")
        self.assertEqual(get_token(key, 6), "287922")
        self.assertEqual(get_token(key, 7), "162583")
        self.assertEqual(get_token(key, 8), "399871")
        self.assertEqual(get_token(key, 9), "520489")

    def test_new_secret(self):
        # secrets should be unique and 20 characters long (base 32)
        secrets = set(new_secret() for i in range(100))
        self.assertEqual(len(secrets), 100)
        for s in secrets:
            self.assertTrue(len(s), 20)
            base64.b32decode(s)
