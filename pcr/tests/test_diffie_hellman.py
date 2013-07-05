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
