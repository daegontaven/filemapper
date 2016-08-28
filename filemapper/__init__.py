#!/usr/bin/env python
# coding:utf-8
# File Mapping Module

"""
This module is designed to create variables for files that are to be accessed
collectively. Since files tend to take up a lot of memory, it is not advised to
use this module to keep multiple files in a directory open. The mapper works by
creating variables with same file name and maps them(Do not confuse this for
the built-in maps() function) to their file location. These variables can then
be accessed like regular files using read(). All the functions defined here
return a tuple of successfully processed files.
"""

# Imports
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from . import core
import sys

# Globals
global flag, closed_files, file_dict
flag = None
file_dict = {}
closed_files = []


def create(path=None):
    """
    Automatically generates variables for files and maps them to their file
    paths. Call create() everytime a new file is added to update the maps.
    """
    if path is not None:
        core.map_files(path)
    else:
        core.map_files('.')  # Root Directory
    global file_dict
    file_dict = core.mapped_files
    return core.mapped_files


def load(path=None, mode='r'):
    """
    Opens all the files in the root of a directory. If create() was called
    before calling load(), then it will be called again to override any
    previous maps.

    Example Usage:
    >>>import filemapper as fm
    >>>open_files = fm.load('resources','w')
    >>>print(open_files)
    ('nouns.dat','adverbs.dat','verbs.txt')
    """
    # Loads The Files
    create(path)
    crr_files = []
    err_files = []
    for file_name in file_dict.items():
        try:
            file_dict[file_name[0]] = open(file_name[1], mode)
            crr_files.append(file_name[0])
        except IOError:
            err_files.append(file_name[0])
    if err_files != []:
        raise IOError(', '.join(str(err_file) for err_file in err_files) +
                      " files are missing")
    global flag
    flag = True
    return tuple(crr_files)


def close(*args):
    """
    Calling this function without arguments closes all or any remaining files
    to be closed. Passing file names as arguments will close those files as
    needed. This function will not unmap any of the files mapped using the
    create function.
    """
    global closed_files
    if flag:
        if args == ():  # This part closes all files
            crr_files = []
            if sys.version_info < (3,):
                difference_files = [i for i in [two_tuple[0] for two_tuple in
                                                file_dict.items()]
                                    if i not in closed_files]
            else:
                difference_files = [i for i in [two_tuple[0] for two_tuple in
                                                list(file_dict.items())]
                                    if i not in closed_files]
            for file_name in difference_files:
                file_dict[file_name].close()  # This is the magic
                crr_files.append(file_name)
                closed_files.append(file_name)
            return tuple(difference_files)
        else:  # This part closes specific files
            crr_files = []
            err_files = []
            same_files = []
            # Do not change file_name to file_name[0]
            # Read the for loop below very carefully
            for file_name in args:
                if file_name not in closed_files:
                    if file_name in [two_tuple[0] for two_tuple in
                                     file_dict.items()]:
                        file_dict[file_name].close()  # This is the magic
                        crr_files.append(file_name)
                        closed_files.append(file_name)
                    else:
                        err_files.append(file_name)
                else:
                    same_files.append(file_name)
            if err_files != []:
                raise IOError(', '.join(str(err_file) for err_file
                                        in err_files)
                              + " not defined in file_dict ")
            if same_files != []:
                if len(same_files) == 1:
                    raise IOError(', '.join(str(same_file) for same_file
                                            in same_files)
                                  + " is closed already")
                else:
                    raise IOError(', '.join(str(same_file) for same_file
                                            in same_files)
                                  + " were closed already")
            return tuple(crr_files)
    else:
        raise IOError("Files not open to be closed")


def read(file_name):
    """
    Should be primarily used for accessing files mapped using the create()
    function.
    Note: The load() function automatically calls create() and also opens the
          files.
    Example Usage:
    for line in read('tale_of_two_cities.txt'):
        print line
    """
    return file_dict[file_name]


def reset():
    """
    Resets, deletes and closes all variables in a map. Be careful when when
    using this function.
    """
    cls = close()
    global flag, closed_files, file_dict
    flag = None
    file_dict = {}
    closed_files = []
    return cls
        

if __name__ == "__main__":
    print(load())
