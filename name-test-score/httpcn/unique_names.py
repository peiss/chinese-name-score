# coding:GB18030

fin = open("./dicts/names_girls_single_words_source.txt")
fout = open("./dicts/names_girls_single_words_formal.txt", "w")


names = set()
for line in fin:
    line = str(line).strip()
    if len(line) == 0 :
        continue
    names.add(line)

print len(names)

for name in names:
    fout.write(name + "\n")
fout.flush()
fout.close()
