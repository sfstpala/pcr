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

''' Diffie-Hellman Key Exchange '''


import random


class DiffieHellman (object):

    def __init__(self, prime, generator, rand_max):
        self.p, self.g = prime, generator
        self.x = random.SystemRandom().randint(0, rand_max)

    def get_public_key(self):
        y = pow(self.g, self.x, self.p)
        return y

    def get_shared_secret(self, yb):
        key = pow(yb, self.x, self.p)
        return key
