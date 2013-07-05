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

''' PKCS7 Padding for Block Cipher Modes '''


def pad(data, block_size):
    padding_length = block_size - (len(data) % block_size)
    return data + bytes(padding_length for i in range(padding_length))


def unpad(data):
    padding_length = data[-1]
    return data[:-padding_length]


def check_padding(data, block_size):
    if not data or len(data) % block_size:
        raise ValueError("padding error")
    if data[-1] > block_size:
        raise ValueError("padding error")
    if not all(i == data[-1] for i in data[-data[-1]:]):
        raise ValueError("padding error")
