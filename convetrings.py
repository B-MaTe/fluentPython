s = 'café'
len(s) # 4 It has 4 Unicode characters
b = s.encode("utf8")
# b'caf\xc3\xa9'
len(b) # 5 Now it hat 5 bc "é" is encoded as two bytes
b = b.decode("utf8")
# café

cafe = bytes("café", encoding="utf_8")
# b'caf\xc3\xa9'
cafe[0]
# 99
cafe[:1]
# b'c'
cafe_arr = bytearray(cafe)
#bytearray(b'caf\xc3\xa9')
