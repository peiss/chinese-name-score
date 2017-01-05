# coding:utf8

import os

dirpath = "C:/Users/pss/git/name-test-score/name-test-score/main/data"
all_count = 0
for fname in os.listdir(dirpath):
    if 'input' in fname:
        for line in open(dirpath + "/" + fname):
            all_count += 1
            
print all_count
