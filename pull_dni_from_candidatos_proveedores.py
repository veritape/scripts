#-*- coding: utf-8 -*-
import codecs
import re


proveedores = []
for i in codecs.open("candidatos_proveedores.txt", "r", "utf-8"):
    i = i.strip()
    i = i.replace(",", " ")
    i = re.sub("\s+", " ", i)
    proveedores.append(i)


out = "DNI\tNOMBRE COMPLETO\n"
for i in codecs.open("hoja.tsv.0", "r", "utf-8"):
    i = i.strip()
    i = i.split("\t")
    name = i[8] + " " + i[9] + " " + i[10]
    name = re.sub("\s+", " ", name)

    if name in proveedores:
        out += i[0] + "\t" + name + "\n"

print out.encode("utf-8")
