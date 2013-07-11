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

''' Various mathematical function used in public key cryptography '''

import os
import random

random = random.SystemRandom()


def is_prime(n, k=64):
    '''
    Test whether n is prime using the probabilistic Miller-Rabin
    primality test. If n is composite, then this test will declare
    it to be probably prime with a probability of at most 4**-k.

    To be on the safe side, a value of k=64 for integers up to
    3072 bits is recommended (error probability = 2**-128). If
    the function is used for RSA or DSA, NIST recommends some
    values in FIPS PUB 186-3:

    <http://csrc.nist.gov/publications/fips/fips186-3/fips_186-3.pdf>

    Do not use this function for small numbers.

    '''
    def check_candidate(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, 2048):  # performace optimisation
        if n % i == 0:
            return False
    s = 0
    d = n - 1
    while True:
        q, r = divmod(d, 2)
        if r == 1:
            break
        s += 1
        d = q
    for i in range(k):
        a = random.randint(2, n - 1)
        if check_candidate(a):
            return False
    return True


def get_prime(bits, k=64):
    '''
    Return a random prime up to a certain length

    This function uses random.SystemRandom.

    '''
    if bits % 8 != 0 or bits == 0:
        raise ValueError("bits must be >= 0 and divisible by 8")
    while True:
        n = int.from_bytes(os.urandom(bits // 8), "big")
        if is_prime(n, k):
            return n


def phi(n, p, q):
    '''
    Euler's totient function for n which can be written as pq

    This is the number of k in the range 0 <= k <= n where
    gcd(n, k) is = 1 or, in other words, the number of integers
    k <= n that are relatively prime to n.
    '''
    return (n + 1) - (p + q)


def mult_inv(a, b):
    '''
    Calculate the multiplicative inverse a**-1 % b

    This function works for n >= 5 where n is prime.
    '''
    # in addition to the normal setup, we also remember b
    last_b, x, last_x, y, last_y = b, 0, 1, 1, 0
    while b != 0:
        q = a // b
        a, b = b, a % b
        x, last_x = last_x - q * x, x
        y, last_y = last_y - q * y, y
    # and add b to x if x is negative
    if last_x < 0:
        return last_x + last_b
    return last_x


def make_rsa_keys(bits=2048, e=65537, k=64):
    '''
    Create RSA key pair

    Returns n, e, d, where (n, e) is the public
    key and (n, e, d) is the private key (and k is
    the number of rounds used in the Miller-Rabin
    primality test).

    '''
    p, q = None, None
    while p == q:
        p, q = get_prime(bits // 2), get_prime(bits // 2)
    n = p * q
    phi_n = phi(n, p, q)
    d = mult_inv(e, phi_n)
    return n, e, d
