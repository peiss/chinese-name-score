# coding:GB18030

"""
给一个文件地址，把文件的行去重、删除空行
"""
import os

fpath_source = "../dicts/names_boys_single.txt"

fpath_tmp = "%s_tmp" % fpath_source


def unique_file_a_to_b(fpath_input, fpath_output):
    fin = open(fpath_input)
    fout = open(fpath_output, "w")
    
    names = set()
    for line in fin:
        line = str(line).strip()
        if len(line) == 0 :
            continue
        names.add(line)
    
    for name in names:
        fout.write(name + "\n")
    fout.flush()
    fout.close()

unique_file_a_to_b(fpath_source, fpath_tmp)
unique_file_a_to_b(fpath_tmp, fpath_source)
os.remove(fpath_tmp)

print "over"