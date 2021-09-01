#!/usr/bin/python3
inpencode = input("Encode text: ")
print(''.join(['\\x'+hex(c)[2:] for c in inpencode.encode()]))
