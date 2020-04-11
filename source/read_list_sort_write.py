import numpy as np
"""
str1 = "words with    spaces of different  lenghts "
list1 = str1.split()
for _ in list1:
    print(_)

str2 = "qqq words @ with, special @ ch,ar @spe@rate them "
list2 = str2.split("@")
for _ in list2:
    print(_)
"""
in_file = open("inFile.txt","r") # r, w, a, r+
out_file = open("outFile.txt","r+")

for aRow in in_file.readlines():
    print(aRow)
    list3 = aRow.split()
    print(list3)
    for _ in list3:
        out_file.write(_+"\n") #excape char


in_file.close()
out_file.close()