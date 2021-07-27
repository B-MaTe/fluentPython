import struct

fmt = '<3s3sHH'
FILE = 'C:\\Users\\akosm\\Downloads\\giphy.gif'

with open(FILE, 'rb') as fp:
    img = memoryview(fp.read())

header = img[:10]
print(bytes(header))

struct.unpack(fmt, header)
print(header)
del header
del img