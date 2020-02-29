# copy_files
Python program to copy files from one directory to another. It has options for deep and shallow copy, and to only copy files modified since a given date.

To copy files from a directory, call the function `copyDir`

copyDir(sourceDir,destDir,since=None,deep=False)

`sourceDir` and `destDir` are the complete paths as strings. `since` is a string of the date represented in YYYYMMDD format.
