import unittest

from pcr.cbc import CBC


class MockCipher:

    block_size = 1

    def encrypt(self, data, key):
        return bytes([data[0] ^ key[0]])

    def decrypt(self, data, key):
        return bytes([data[0] ^ key[0]])


class CBCTest(unittest.TestCase):

    def test_init(self):
        self.assertRaises(ValueError, CBC, MockCipher, b"")
        self.assertTrue(CBC(MockCipher, b'\0' * 1))

    def test_xor(self):
        x = CBC(MockCipher, b'\0' * 1).xor(b"one", b"two")
        self.assertEqual(x, b'\x1b\x19\n')

    def test_encrypt(self):
        m = CBC(MockCipher, b'\0')
        e = m.encrypt(b'\1\1\1', b'\2')
        self.assertEqual(e, b'\3\0\3')

    def test_decrypt(self):
        m = CBC(MockCipher, b'\0')
        e = m.decrypt(b'\3\0\3', b'\2')
        self.assertEqual(e, b'\1\1\1')
