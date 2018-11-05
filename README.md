# Remove BOM from File
When using Talend Big Data Open Studio, converting XML files, I faced some problems when I detected some files were encoded using UTF-8 BOM.

So, this code is a simple way to remove BOM from a file.

## What is BOM
BOM stands for Byte Order Mark.
You can read more in: https://stackoverflow.com/questions/2223882/whats-different-between-utf-8-and-utf-8-without-bom

## Requirements
Python 3.7 (tested in Windows)


## How to use ?
Set a file with the path of files to be changed.

For example (mylist.txt):

```c:\path\file1.txt 
c:\path\file2.txt 
c:\path\file3.txt 
c:\path\file4.txt
```

Change the first line of the code (`processBOM.py`)

Call the python script:
`$ processBOM.py`

Note that it will *overwrite* the original file.

#### Next Steps
Improve code to run as `$ processBOM.py mypathoflist.txt`
