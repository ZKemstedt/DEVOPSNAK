def print_bin(num):
    print(f"integer {num} in bits {bin(num)} bit length {num.bit_length()}")


print_bin(1)
print_bin(2)
print_bin(16)
print_bin(255)
print_bin(256)
# 0000 0001
#

print((1).to_bytes(1, byteorder="big"))
print((255).to_bytes(1, byteorder="big"))

print((256).to_bytes(2, byteorder="big"))

# one byte
code_1 = "1".encode()
code_2 = "2".encode()
code_3 = "9".encode()

print(len(code_1))
print(len(code_2))
print(len(code_3))

# two bytes
code_4 = "10".encode()
print(len(code_4))
