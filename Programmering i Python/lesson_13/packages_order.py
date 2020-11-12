import struct
import random


def get_byte(size):
    fake_byte_message = b''
    for b in range(size):
        fake_byte_message += chr(b % 26 + 97).encode()
    return fake_byte_message


a_list_of_bytes = []
for i in range(10):
    a_list_of_bytes.append(struct.pack("!LL4088s", 4096, i, get_byte(4088)))

random.shuffle(a_list_of_bytes)


def recv():
    return a_list_of_bytes.pop()


buffer = bytearray(4088*10)

for i in range(10):
    packet = recv()
    size, idx = struct.unpack("!LL", packet[:8])
    message, = struct.unpack_from("!4088s", packet, 8)
    buffer[idx * 4088: idx * 4088 + 4088] = message

print(buffer[0])
print(buffer[4088])
