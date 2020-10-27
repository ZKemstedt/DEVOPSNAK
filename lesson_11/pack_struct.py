import struct

# Setup
TEXT = b"t"
print(struct.calcsize('!Lc'))

message_type = TEXT
message = "hello world"
message_as_bytes = message.encode()

# Pack message
struct_format = f'!Lc{len(message_as_bytes)}s'
struct_size = struct.calcsize(f'!Lc{len(message_as_bytes)}s')
print("struct_format", struct_format)
print("struct_size", struct_size)

packed_message = struct.pack(struct_format, struct_size, message_type, message_as_bytes)
print(packed_message)
print(f"packed_message len {len(packed_message)}")

# Unpack
message_length, message_type = struct.unpack('!Lc', packed_message[0:5])
print(struct.calcsize('!Lc'))
message,  = struct.unpack(f"!{message_length-5}s", packed_message[5:message_length])

if(message_type == b"t"):
    print(message.decode())
