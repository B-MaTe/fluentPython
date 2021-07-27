from array import array
from random import random
'''
floats = array('d', (random() for i in range(10**7)))
# print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
# print(floats2[-2])
# print(floats == floats2)

numbers = array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
# len(memv)= 5
# memv[-1] = 2

memv_oct = memv.cast('B')
# memv_oct = <memory at 0x00D46208>
memv_oct.tolist()
memv_oct[5] = 4
#print(numbers)


nums = array('h', [-2, -1, 0, 1, 2]) # 'h' creates an array of short int (16bits)
octets = bytes(nums) # holds a copy of the bytes that make up the nums
# b'\xfe\xff\xff\xff\x00\x00\x01\x00\x02\x00' 10 Bytes that represent the 5 short int

'''