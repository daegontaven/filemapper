from __future__ import absolute_import, division, print_function, unicode_literals
import os, sys
from sys import platform as _platform

global mapped_files, sep
mapped_files = {}
sep = '/'

if _platform == "win32":
    sep = '\\'

def map_files(path):
    global mapped_files, sep
    if sys.version_info < (3,):
        root, dirs, files = os.walk(path).next()
    else:
        root, dirs, files = os.walk(path).__next__()
    for f in files:
        mapped_files[f]='%s%s%s' % (root,sep,f)
    return mapped_files

if __name__=="__main__":
    print(map_files())
