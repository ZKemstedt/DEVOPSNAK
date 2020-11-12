import struct
import json

cars = {
    "volvo": "yellow",
    "saab": "blue",
    "Vålvå": "RÖda"
}

cars_as_json = json.dumps(cars)
print(cars_as_json)
print(type(cars_as_json))
# We have cars as a json with type str
# Now we need to convert it to bytes

# as utf-8 with encode & decode
cars_json_as_bytes = cars_as_json.encode()
cars_length = len(cars_json_as_bytes)
print("car length", cars_length)

format_string = f"!L{cars_length}s"
format_length = struct.calcsize(format_string)
print("total format_length = ", format_length)
print("prefix format length = ", struct.calcsize("!L"))

struct_message = struct.pack(format_string, format_length, cars_json_as_bytes)
print(struct_message)


def recv():
    return struct_message


print("\n\n\n ------------- fake socket ----------------- \n\n\n")

# struct_message incoming to SERVERSIDE

a_message = recv()
fmt = "!L"

total_length, = struct.unpack(fmt, a_message[0:4])
print(total_length)

total_fmt = f"!4x{total_length - struct.calcsize(fmt)}s"
json_bytes, = struct.unpack(total_fmt, a_message)
json_str = json_bytes.decode()
dict_from_json = json.loads(json_str)

print(dict_from_json)
print(type(dict_from_json))

dict_from_json["mazda"] = "green"
del dict_from_json["saab"]
print(dict_from_json)
