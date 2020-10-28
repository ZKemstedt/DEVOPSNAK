import uuid
import hashlib
import threading
import struct

msg = b"hello world 2"

m = hashlib.sha256()
m.update(msg)
print(m.digest())
print(m.hexdigest())
print(m.digest_size)

m_2 = hashlib.sha256()
msg_1 = b"hello"
m_2.update(msg_1)
msg_2 = b" world 2"
m_2.update(msg_2)
print(m_2.hexdigest())

my_uuid = uuid.uuid4()
print(my_uuid)
print(my_uuid.bytes)
print(len(my_uuid.bytes))

counter = 0


def get_id(lock):
    with lock:
        global counter
        if counter > 4294967294:
            counter = 0
        counter += 1
        return counter


def print_ids(lock):
    for i in range(100):
        # use uuid or get_id function
        print(struct.pack("!16sL", my_uuid.bytes, i))
        print(struct.pack("!LL", get_id(lock), i))
        # send part i of 100


lock = threading.Lock()
threading.Thread(target=print_ids, args=(lock,)).start()
threading.Thread(target=print_ids, args=(lock,)).start()


# request number, package number, checksum (total or incremental?)
#
