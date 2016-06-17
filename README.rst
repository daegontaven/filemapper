============
filemapper
============

This module is designed to create variables for files that are to be accessed collectively.
Since files tend to take up a lot of memory, it is not advised to use this module to keep
multiple files in a directory open. The mapper works by creating variables with same file name
and maps them(Do not confuse this for the built-in maps() function) to their file location.
These variables can then be accessed like regular files using read(). All the functions defined
here return a tuple of successfully processed files.

-------------
Compatability
-------------

Tested Combinations:
  - Windows 10/8/7
  - Most Linux Distros
  - Python (3.5,3.4,2.7)
  
Using this module in any combination other than those listed above may produce unexpected results.

------------
Installation
------------

     pip install filemapper

-----
Usage
-----

     >>>import filemapper as fm
     
     >>>help(fm) #This will display help for this module

Creating variables
""""""""""""""""""

     >>>import filemapper as fm
     >>>print fm.create('resources') #Creates variables for files within the folder resources
     {'nouns.dat':u'resources\\nouns.dat','adjectives.dat':u'resources\\adjectives.dat'}
     
     >>>f = open(fm.read('nouns.dat')) #'nouns.dat', our variable here needs to be passed into read() before it can be used.
     
     >>>for i in f:print i #Prints out the whole 'nouns.dat' file even though we never assigned a variable directly.
     
     A-bomb
     
     A-bombs
     
     A-frame
     
     [Trunctuated 90959 Lines]
     
     zymurgy

Example Cases
     >>>f = fm.create('resources')
     
     >>>new_f = [sub_f[0] for sub_f in f.items()]
     
     >>>for i in new_f: #Only prints the content of files that start with 'a'
     
     ...    if i[0] == 'a':
     
     ...        for x in  open(i, 'r'):print x
     
     [Stdout Ommitted due to large size]

Loading Files
"""""""""""""

     >>>print fm.load('resources','w') #Omittiing the second argument will default to read only mode
     
     ('nouns.dat','adjectives.dat')
     
     >>>for i in fm.read('nouns.dat'):print i
     
     [Stdout Ommitted due to large size]
     
Closing Files
"""""""""""""

     >>>fm.close('nouns.dat')
     
     ('adjectives.dat')
     
     >>>fm.close() #Closes all the files
