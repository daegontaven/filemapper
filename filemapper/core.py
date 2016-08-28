from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import sys
import os

global mapped_files
mapped_files = {}


def map_files(path):
    global mapped_files
    if sys.version_info < (3,):
        root, dirs, files = os.walk(path).next()
    else:
        root, dirs, files = os.walk(path).__next__()
    for f in files:
        mapped_files[f] = os.path.join(root, f)
    return mapped_files
