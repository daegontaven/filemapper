#!/usr/bin/env python
#coding:utf-8
#Tests

import filemapper as fm

def main():
    print(fm.create('resources'))
    print(fm.load('resources'))
    for i in fm.read('adverbs.dat'):
        print(i)
    print(fm.close('nouns.dat'))
    print(fm.close())
    

if __name__ == "__main__":
    main()
