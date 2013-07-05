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

from pcr.pkcs7 import pad, unpad, check_padding


class PKCS7Test(unittest.TestCase):

    def test_pad(self):
        self.assertEqual(
            pad(b"\0\0\0", 4),
            b"\0\0\0\1")
        self.assertEqual(
            pad(b"\0\0\0\0", 4),
            b"\0\0\0\0\4\4\4\4")

    def test_unpad(self):
        self.assertEqual(
            unpad(b"\0\0\0\1"),
            b"\0\0\0")
        self.assertEqual(
            unpad(b"\0\0\0\0\4\4\4\4"),
            b"\0\0\0\0")

    def test_check_padding(self):
        self.assertEqual(check_padding(b"\0\0\0\0\4\4\4\4", 4), None)
        self.assertRaises(ValueError, check_padding, b"\0\0\0\0\4\4\3\4", 4)
