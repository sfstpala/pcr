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
