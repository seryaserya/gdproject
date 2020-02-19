import sys
import argparse
from operator import itemgetter

text = ""

if len(sys.argv) == 1:
    text = input()
else:
    for i in range(1, len(sys.argv)):
        #print(sys.argv[i])
        text = text + sys.argv[i]+" "

fixed = list()
counts = dict()
words = text.split()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
    fixed = sorted(sorted(counts.items()), key=itemgetter(1), reverse=True)
print("\n".join(str(x) for x in fixed))







