from types import MappingProxyType

d = {1:'A'}
d_proxy = MappingProxyType(d)

#d_proxy[2] = 'd' ######ERROR TypeError: 'mappingproxy' object does not support item assignment
d[2]='B' # {1: 'A', 2: 'B'}
#print(d_proxy[2]) = B ITS DINAMIC TO NEW CHANGES
