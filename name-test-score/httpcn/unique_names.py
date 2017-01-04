# coding:GB18030

fin = open("./datas/names_girls_source.txt")
fout = open("./datas/names_grils_formal.txt", "w")


names = set()
for line in fin:
    line = str(line).strip()
    if len(line) == 2:
        # print line
        continue
    names.add(line)

print len(names)

for name in names:
    fout.write(name + "\n")
fout.flush()
fout.close()
