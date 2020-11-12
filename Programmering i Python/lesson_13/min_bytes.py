import random
import struct

fake_byte_message = b''
for b in range(4096):
    fake_byte_message += chr(b % 26 + 97).encode()

print(type(fake_byte_message))
print(len(fake_byte_message))

struct_fake_message = struct.pack("!L4092s", 4096, fake_byte_message)


def recv(msg, buf_size):
    inner_buf_size = min([buf_size, 4096, len(msg)])
    bytes_returned = random.randint(1, inner_buf_size)
    return msg[:bytes_returned], msg[bytes_returned:]


# use a fake recv

"""
# Alt 1
recv_buf_size = 4096
recv_message, remainder = recv(struct_fake_message, recv_buf_size)
print(len(recv_message))
recv_message_length = min(len(recv_message), recv_buf_size)
message, = struct.unpack(f"!{recv_message_length}s", recv_message)
print(message)

# Alt 2 fix bufsize 4096
recv_buf_size = 4096
total_msg = b""
while len(total_msg) < recv_buf_size:
    recv_message, struct_fake_message = recv(struct_fake_message, recv_buf_size)
    total_msg += recv_message
    print(len(total_msg))

assert len(total_msg) == 4096

"""
# Alt 3 check struct len
recv_buf_size = 4096
total_msg = b""

bytes_to_fetch = None
while True:
    recv_message, struct_fake_message = recv(struct_fake_message, recv_buf_size)
    total_msg += recv_message
    if(not bytes_to_fetch):
        bytes_to_fetch,  = struct.unpack("!L", recv_message[:4])

    bytes_to_fetch -= len(recv_message)

    if(bytes_to_fetch < 1):
        break

print(len(total_msg))
print(total_msg)
