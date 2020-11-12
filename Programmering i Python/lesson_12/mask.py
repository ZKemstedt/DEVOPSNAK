

EVENT_READ = (1 << 0)
EVENT_WRITE = (1 << 1)


print("Value 1 - 0000 0001")
print("EVENT_READ", EVENT_READ & 1)
print("EVENT_WRITE", EVENT_WRITE & 1)

print("Value 2 - 0000 0010")
print("EVENT_READ", EVENT_READ & 2)
print("EVENT_WRITE", EVENT_WRITE & 2)


print("Value 3 - 0000 0011")
print("EVENT_READ", EVENT_READ & 3)
print("EVENT_WRITE", EVENT_WRITE & 3)


"""
    0 & 1

    0000 0000
    0000 0001
    & -------
    0000 0000

    1 & 1
    0000 0001
    0000 0001
    & -------
    0000 0001

    2 & 2
    0000 0010
    0000 0010
    & -------
    0000 0010

    2 & 1
    0000 0010
    0000 0001
    & -------
    0000 0000

"""
