from __future__ import absolute_import, division, print_function, unicode_literals
import os, sys

global mapped_files
mapped_files = {}

def map_files(path):
    global mapped_files
    if sys.version_info < (3,):
        root, dirs, files = os.walk(path).next()
    else:
        root, dirs, files = os.walk(path).__next__()
    for f in files:
        mapped_files[f]='%s\%s' % (root,f)
    return mapped_files

if __name__=="__main__":
    print(map_files())
