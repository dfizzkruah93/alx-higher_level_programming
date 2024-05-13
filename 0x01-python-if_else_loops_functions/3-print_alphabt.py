#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) == 'qi' or chr(i) == 'e':
        continue
    print(chr(i).format(i), end='')
