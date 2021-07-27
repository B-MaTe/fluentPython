from dis import dis
from unicodedata import name

l = ['spam', 'spam', 'eggs', 'spam']
#print(set(l)) # {'eggs', 'spam'} CLEARS THE DUPLICATES
#print(list(set(l))) # ['eggs', 'spam']

haystack = 'aaadasgaaaaass'
needle = 'jancsi'
found = len(set(haystack) & set(needle))
#print(found) = 2 -> a, s


#dis('{1}')
#print('\n')
#dis('set([1])')
"""
1           0 LOAD_CONST               0 (1)
              2 BUILD_SET                1
              4 RETURN_VALUE


  1           0 LOAD_NAME                0 (set)
              2 LOAD_CONST               0 (1)
              4 BUILD_LIST               1
              6 CALL_FUNCTION            1
              8 RETURN_VALUE
"""

a = frozenset(range(10))
# frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})

b = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')}
# {'®', '+', '$', '¶', '%', '¤', 'µ', '°', '¬', '=', '¥', '£', '©', '¢', '÷', '#', '<', '>', '±', '×', '§'}1