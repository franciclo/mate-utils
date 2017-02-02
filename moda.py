#!/usr/bin/python
import sys

l = sys.argv[1:]

repeticiones = 0
for i in l:
    apariciones = l.count(i)
    if apariciones > repeticiones:
        repeticiones = apariciones

modas = []
for i in l:
    apariciones = l.count(i)
    if apariciones == repeticiones and i not in modas:
        modas.append(i)

print modas
