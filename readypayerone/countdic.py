import pprint
from coloring import colors

str = input()

count = {}

for l in str:
    count.setdefault(l, 0)
    count[l] += 1

pprint.pprint(count)
