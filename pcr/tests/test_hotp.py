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
import unittest.mock
import base64

from pcr.hotp import get_token, verify_token, new_secret


class HOTPTest(unittest.TestCase):

    # HOTP Algorithm Test Values:
    #     http://tools.ietf.org/html/rfc4226
    # The secret from appendix d of rfc4226 is converted to base 32
    # and the first charcter is converted to lowercase:
    secret = "gEZDGNBVGY3TQOJQGEZDGNBVGY3TQOJQ"
    # these are the first 10 matching tokens (c = 0..9):
    tokens = [
        "755224",
        "287082",
        "359152",
        "969429",
        "338314",
        "254676",
        "287922",
        "162583",
        "399871",
        "520489",
    ]

    def test_get_token(self):
        self.assertEqual(get_token(self.secret, 0), self.tokens[0])
        self.assertEqual(get_token(self.secret, 1), self.tokens[1])
        self.assertEqual(get_token(self.secret, 2), self.tokens[2])
        self.assertEqual(get_token(self.secret, 3), self.tokens[3])
        self.assertEqual(get_token(self.secret, 4), self.tokens[4])
        self.assertEqual(get_token(self.secret, 5), self.tokens[5])
        self.assertEqual(get_token(self.secret, 6), self.tokens[6])
        self.assertEqual(get_token(self.secret, 7), self.tokens[7])
        self.assertEqual(get_token(self.secret, 8), self.tokens[8])
        self.assertEqual(get_token(self.secret, 9), self.tokens[9])

    @unittest.mock.patch("time.time")
    def test_verify_token(self, time):
        self.assertEqual(verify_token(
            self.tokens[2], self.secret, 0, window_size=3), 3)
        self.assertEqual(verify_token(
            self.tokens[2], self.secret, 1, window_size=3), 2)
        self.assertEqual(verify_token(
            self.tokens[2], self.secret, 2, window_size=3), 1)
        # we're past the window size:
        self.assertIs(verify_token(
            self.tokens[2], self.secret, 3, window_size=3), False)
        # time based tokens don't have a window size
        time.return_value = 2 * 30
        self.assertIs(verify_token(self.tokens[2], self.secret), True)

    def test_new_secret(self):
        # secrets should be unique and 20 characters long (base 32)
        secrets = set(new_secret() for i in range(100))
        self.assertEqual(len(secrets), 100)
        for s in secrets:
            self.assertTrue(len(s), 20)
            base64.b32decode(s)
