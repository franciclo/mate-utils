#!/usr/bin/python
import sys

l = map(float, sys.argv[1:])

l.sort()
print l

if len(l) % 2 == 0:
    n = len(l)
    mediana = (l[n/2-1]+ l[n/2])/2
else:
    mediana =l[len(l)/2]

print(mediana)
