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

from pcr.maths import is_prime, get_prime, phi, mult_inv, make_rsa_keys


def is_really_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


class MathsTest(unittest.TestCase):

    def test_is_prime(self):
        for i in range(3000 + 1, 4000 + 1):
            self.assertEqual(is_prime(i), is_really_prime(i), i)

    def test_get_prime(self):
        self.assertRaises(ValueError, get_prime, 0)
        self.assertRaises(ValueError, get_prime, 1)
        self.assertRaises(ValueError, get_prime, 4)
        for i in range(32):
            n = get_prime(16)
            self.assertTrue(is_really_prime(n), n)

    def test_phi(self):
        # ps and qs are prime
        ps = 233, 239, 241, 251
        qs = 257, 263, 269, 271
        for p, q in zip(ps, qs):
            n = p * q
            t = 0  # number of n where gcd(n, k) = 1 in 0 <= k <= n
            c = phi(n, p, q)  # test candidate
            for k in range(0, (p * q) + 1):
                if gcd(n, k) == 1:
                    t += 1
        self.assertEqual(t, c, (p, q))

    def test_mult_inv(self):
        for n in range(4096, 8192):
            if not is_prime(n):
                continue
            m = mult_inv(n, 8192)
            self.assertEqual(n * mult_inv(n, 8192) % 8192, 1, m)

    def test_make_rsa_keys(self):
        n, e, d = make_rsa_keys(512)
        self.assertEqual(e, 65537)
        self.assertNotEqual(n, d)
        self.assertLess(len(bin(n)[2:]), 513)
        self.assertGreater(len(bin(n)[2:]), 384)
        self.assertLess(len(bin(d)[2:]), 513)
        self.assertGreater(len(bin(d)[2:]), 384)
