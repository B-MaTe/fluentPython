import collections

#collections.OrederedDict #####PAGE 79
#collections.ChainMap ####PAGE 79

ct = collections.Counter('aaabbc')
#print(ct)
ct.update('bcc')
#print(ct)