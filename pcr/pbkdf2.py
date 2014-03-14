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

''' Password based key-derivation function - PBKDF2 '''

import hmac
import struct


def pbkdf2(digestmod, password, salt, count, dk_length):
    '''
    PBKDF2, from PKCS #5 v2.0:
        http://tools.ietf.org/html/rfc2898

    For proper usage, see NIST Special Publication 800-132:
        http://csrc.nist.gov/publications/PubsSPs.html

    The arguments for this function are:

        digestmod
            a crypographic hash constructor, such as hashlib.sha256
            which will be used as an argument to the hmac function.
            Note that the performance difference between sha1 and
            sha256 is not very big. New applications should choose
            sha256 or better.

        password
            The arbitrary-length password (passphrase) (bytes)

        salt
            A bunch of random bytes, generated using a cryptographically
            strong random number generator (such as os.urandom()). NIST
            recommend the salt be _at least_ 128bits (16 bytes) long.

        count
            The iteration count. Set this value as large as you can
            tolerate. NIST recommend that the absolute minimum value
            be 1000. However, it should generally be in the range of
            tens of thousands, or however many cause about a half-second
            delay to the user.

        dk_length
            The lenght of the desired key in bytes. This doesn't need
            to be the same size as the hash functions digest size, but
            it makes sense to use a larger digest hash function if your
            key size is large.

    '''
    def pbkdf2_function(pw, salt, count, i):
        # in the first iteration, the hmac message is the salt
        # concatinated with the block number in the form of \x00\x00\x00\x01
        r = u = hmac.new(pw, salt + struct.pack(">i", i), digestmod).digest()
        for i in range(2, count + 1):
            # in subsequent iterations, the hmac message is the
            # previous hmac digest. The key is always the users password
            # see the hmac specification for notes on padding and stretching
            u = hmac.new(pw, u, digestmod).digest()
            # this is the exclusive or of the two byte-strings
            r = bytes(i ^ j for i, j in zip(r, u))
        return r
    dk, h_length = b'', digestmod().digest_size
    # we generate as many blocks as are required to
    # concatinate to the desired key size:
    blocks = (dk_length // h_length) + (1 if dk_length % h_length else 0)
    for i in range(1, blocks + 1):
        dk += pbkdf2_function(password, salt, count, i)
    # The length of the key wil be dk_length to the nearest
    # hash block size, i.e. larger than or equal to it. We
    # slice it to the desired length befor returning it.
    return dk[:dk_length]
