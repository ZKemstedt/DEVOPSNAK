import struct


# Client packs a command, 1 or 2
#command = struct.pack("!c", b"1")
command = struct.pack("!c", b"2")


# Server unpack command
srv_command, = struct.unpack("!c", command)
print(srv_command)

if (srv_command == b"1"):
    print("do something")

elif (srv_command == b"2"):
    print("do something else")
