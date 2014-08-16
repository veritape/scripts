#-*- coding: utf-8 -*-

import sys
import codecs


filename = sys.argv[1].strip()

for i in codecs.open(filename, "r", "utf-8").readlines():
    out = ""
    i = i.strip()
    i = i.split("\t")
    dni = str(i[0])
    if len(dni) < 8:
        i[0] = dni.zfill(8)
    for j in i:
        out += j + "\t"
    out = out.strip()
    out += "\n"
    print out.encode("utf-8")
