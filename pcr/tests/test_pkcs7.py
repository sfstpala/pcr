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
