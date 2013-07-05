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
