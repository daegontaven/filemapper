#!/usr/bin/env python
# coding:utf-8
# Tests

from nose.tools import *
import filemapper as fm


def test_setup():
    print(fm.create())
    print(fm.create('resources'))
    print(fm.load('resources'))
    for i in fm.read('adverbs.dat'):
        print(i)
    print(fm.close('nouns.dat'))
    print(fm.close())
    if 'words.dat' and 'nouns.dat' in fm.create('resources'):
        print('Files Missing')

        
def test_coverage():
    print(fm.create())
    print(fm.close())

if __name__ == "__main__":
    test_setup()
    test_coverage()
