#!/usr/bin/env python
# coding:utf-8
# Tests

from nose.tools import *
import filemapper as fm

        
def test_setup():
    print("begin test_setup")
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
        raise ValueError("test_setup failed")
    except IOError:
        print("test_setup passed")


def test_close():
    print("being test_close")
    print(fm.reset())
    try:
        print(fm.close('words.dat'))
        raise ValueError("test_close failed")
    except IOError:
        print("test_close passed")


def test_open():
    print("begin test_open")
    try:
        print(fm.reset())
    except:
        pass
    print(fm.load('resources'))
    try:
        print(fm.close('nouns.dat', 'verbs.dat', 'test.dat'))
        raise ValueError("test_open failed")
    except IOError:
        print("test_open passed")


def test_create():
    print("being test_create")
    try:
        print(fm.reset())
    except:
        pass
    print(fm.create())
    print("test_create passed")


#if __name__ == "__main__":
#    test_setup()
#    test_close()
#    test_open()
