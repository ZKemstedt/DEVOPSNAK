import struct

header = struct.pack('!L3xc', 123, b'0')
print(f'len of header1: {len(header)}')

for x in struct.unpack('!L3xc', header):
    print(f'unpacked data: {x}')


header = struct.pack('!10s', b'HelloWorld')
print(f'len of header2: {len(header)}')

for x in struct.unpack('!10s', header):
    print(f'unpacked data: {x}')
