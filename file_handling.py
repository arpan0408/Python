'''File handling

========= ===============================================================
Character Meaning
--------- ---------------------------------------------------------------
'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)


read()
readline()
write()
'''

file = open("python/test.txt",'r')
# file = open("python/test.txt",'w')
# file = open("python/test.txt",'a')
# file.write("this is new line")
# print(file.read())
# print(file.readline())
# print(file.readline())

file.close()

#modules

import functions as f

f.sum(5,7)