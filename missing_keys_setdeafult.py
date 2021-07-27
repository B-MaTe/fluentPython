import re
import sys

# r'' = RAW STRING
WORD_RE = re.compile(r'\w+')

index = {}

with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)
            """         I
                        I
                        V
      THIS IS THE LONG VARIATION OF THE UPPER CODE
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences"""
    
# print in abc order
for word in sorted(index, key=str.upper):
    print(word, index[word])


