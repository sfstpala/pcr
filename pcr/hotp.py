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

''' Time OTP implementation for 2-factor authentication '''


import hmac
import base64
import struct
import hashlib
import os
import time


def get_token(secret, i=None):
    key = base64.b32decode(secret, True)
    msg = struct.pack(">Q", i if i is not None else (int(time.time()) // 30))
    h = hmac.new(key, msg, hashlib.sha1).digest()
    return str((struct.unpack(">I", h[h[19] & 15:(h[19] & 15) + 4])[0]
                & 0x7fffffff) % 1000000).rjust(6, "0")


def new_secret():
    return base64.b32encode(os.urandom(10))
