#!/usr/bin/env python
# coding:utf-8
# Tests

from nose.tools import *
import filemapper as fm

        
def test_setup():
    print("begin test_close")
    print(fm.create('resources'))
    if 'words.dat' and 'nouns.dat' in fm.create('resources'):
        print('Files Missing')
    print(fm.load('resources'))
    for i in fm.read('adverbs.dat'):
        print(i)
    print(fm.close('words.dat'))
    print(fm.close())
    try:
        print(fm.close('words.dat'))
    except IOError:
        print("test_close passed")
    

if __name__ == "__main__":
    #test_setup()
    test_close()
