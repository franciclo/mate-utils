#!/usr/bin/python
import sys

l = list(map(float, sys.argv[1:]))

media = sum(l)/len(l)

print(media)
