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

import random


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


def get_prime(bits):
    '''
    Return a random prime up to a certain length

    This function uses random.SystemRandom.

    '''
    def check_size(n, bits):
        return len(bin(n)[2:]) == bits
    system_random = random.SystemRandom()
    while True:
        n = system_random.randint(0, 2 ** bits - 1)
        if check_size(n, bits) and is_prime(n):
            return n


def phi(n, p, q):
    '''
    Euler's totient function for n which can be written as pq

    This is the number of k in the range 0 <= k <= n where
    gcd(n, k) is = 1 or, in other words, the number of integers
    k <= n that are relatively prime to n.
    '''
    return (n + 1) - (p + q)