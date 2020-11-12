import struct

# Example if you mix format, DON'T DO IT
# pack signed
fmt = "!l"
msg_length = 0 - 4
packed = struct.pack(fmt, msg_length)

# unpacked unsigned
unpacked,  = struct.unpack("!L", packed)
print(unpacked)
