#!/usr/bin/python
import sys

l = list(map(float, sys.argv[1:]))

l.sort()

if len(l) % 2 == 0:
    n = len(l)
    mediana = (l[int(n/2-1)]+ l[int(n/2)])/2
else:
    mediana =l[int(len(l)/2)]

print(mediana)
