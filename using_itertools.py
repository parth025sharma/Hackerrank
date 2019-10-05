#!/bin/python3

from itertools import combinations_with_replacement
string,n=input().split()
a=list(combinations_with_replacement(sorted(string),int(n)))
a=[''.join(i) for i in a]
for i in a:
	print(str(i))

