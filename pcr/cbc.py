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

''' Cipher Block Chaining Mode of Operation '''


class CBC (object):

    def __init__(self, BlockCipher, iv):
        self.block_cipher = BlockCipher()
        if len(iv) != self.block_cipher.block_size:
            raise ValueError("iv must be {} bytes long".format(
                self.block_cipher.block_size))
        self.iv = iv

    @staticmethod
    def xor(a, b):
        return bytes(i ^ j for i, j in zip(a, b))

    def encrypt(self, data, key):
        b = self.block_cipher.block_size
        if len(data) % b:
            raise ValueError("length of data must be divisible by %d" % b)
        p, result = self.iv, b''
        for i in range(len(data) // b):
            plain = data[i * b:i * b + b]
            ciph = self.block_cipher.encrypt(self.xor(plain, p), key)
            result, p = result + ciph, ciph
        return result

    def decrypt(self, data, key):
        b = self.block_cipher.block_size
        if len(data) % b:
            raise ValueError("length of data must be divisible by %d" % b)
        result, p = b'', self.iv
        for i in range(len(data) // b):
            ciph = data[i * b:i * b + b]
            plain = self.xor(self.block_cipher.decrypt(ciph, key), p)
            p = ciph
            result += plain
        return result
