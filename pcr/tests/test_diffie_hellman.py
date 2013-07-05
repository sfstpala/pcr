import unittest

from pcr.diffie_hellman import DiffieHellman
from pcr.rfc3526 import groups


class DiffieHellmanTest(unittest.TestCase):

    def test_key_exchange(self):
        prime, generator = groups[2048]
        alice = DiffieHellman(prime, generator, 2 ** 512)
        bob = DiffieHellman(prime, generator, 2 ** 512)
        alices_secret = alice.get_shared_secret(bob.get_public_key())
        bobs_secret = bob.get_shared_secret(alice.get_public_key())
        self.assertEqual(alices_secret, bobs_secret)
