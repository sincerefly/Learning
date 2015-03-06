#!/usr/bin/python
"""
Use:
    input  ./md5.py password
    ouput  5f4dcc3b5aa765d61d8327deb882cf99

DateTime: 2015-03-06 23:08
"""
import sys
import hashlib

src = sys.argv[1]
m2 = hashlib.md5()
m2.update(src)
print m2.hexdigest()
