# coding:GBK

import os
import sys

reload(sys) 
sys.setdefaultencoding("GB18030")

dirpath = "D:\\workbench\\chinese-name-score\\name-test-score\\main\\data"

fout = open("../dicts/names_boys_double.txt", "w")

all_names = set()
for fname in os.listdir(dirpath):
    if 'txt' in fname:
        for line in open(dirpath + "/" + fname):
            name = str(line).strip()
            clear_name = name.replace(u"裴", u"")
            if not clear_name or len(clear_name) == 0:
                continue
            all_names.add(clear_name)
            
for name in all_names:
    fout.write(name + "\n")
            
fout.flush()
fout.close()
