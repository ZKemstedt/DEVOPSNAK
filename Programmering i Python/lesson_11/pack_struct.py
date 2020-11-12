import struct
import pickle

# Setup
TEXT = b"t"
DICT = b"d"
print(1, struct.calcsize('!Lc'))

message_type = DICT
message = {"key": "hello world åäö"}
message_as_bytes = pickle.dumps(message)

# Pack message
struct_format = f'!Lc{len(message_as_bytes)}s'
struct_size = struct.calcsize(f'!Lc{len(message_as_bytes)}s')
print(2, "struct_format", struct_format)
print(3, "struct_size", struct_size)

packed_message = struct.pack(struct_format, struct_size, message_type, message_as_bytes)
print(4, packed_message)
print(5, f"packed_message len {len(packed_message)}")

# Send over socket packed_message

# Recv from socket

# Unpack
message_length, message_type = struct.unpack('!Lc', packed_message[0:5])
print(6, struct.calcsize('!Lc'))
message,  = struct.unpack(f"!{message_length-5}s", packed_message[5:message_length])

if(message_type == TEXT):
    print(7, message.decode())

if(message_type == DICT):
    print(8, pickle.loads(message))
