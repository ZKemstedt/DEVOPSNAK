
import pickle

str_to_byte = b'abcdef'

print(str_to_byte)
print(type(str_to_byte))

# b prefix
# try to convert åäö
# str_to_byte_2 = b'åäö'

# bytes
str_to_byte_2 = bytes('åäö', "utf-8")
print(str_to_byte_2)

# encode / decode (default is utf-8)
str_to_byte_3 = 'åäö'.encode()
print(type(str_to_byte_3))
print(str_to_byte_3)

byte_3_to_str = str_to_byte_3.decode()
print(type(byte_3_to_str))
print(byte_3_to_str)


b = pickle.dumps([12123123, 2, 3])
print(type(b))
print(b)

print(pickle.loads(b))
