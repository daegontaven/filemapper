============
filemapper
============
This module is designed to create variables for files that are to be accessed collectively.
Since files tend to take up a lot of memory, it is not advised to use this module to keep
multiple files in a directory open. The mapper works by creating variables with same file name
and maps them(Do not confuse this for the built-in maps() function) to their file location.
These variables can then be accessed like regular files using read(). All the functions defined
here return a tuple of successfully processed files.