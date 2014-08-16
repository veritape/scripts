#-*- coding: utf-8 -*-
import codecs
import sys


# file that needs org politica
input_file = "hojas_3_4"

# file 0 as reference
ref_file = "hoja.tsv.0"
org_politicas = []
for i in codecs.open(ref_file, "r", "utf-8").readlines():
    i = i.strip().split("\t")
    obj = {i[0]: i[2]}
    org_politicas.append(obj)

for i in codecs.open(input_file, "r", "utf-8").readlines():
    out = ""
    line = i.strip().split("\t")
    dni = line[0]

    found = "false"
    for j in org_politicas:
        if dni == j.keys()[0]:
            out = j.values()[0] + "\t" + i.strip()
            print out.encode("utf-8")
            found = "true"
            break
    # this is the header row
    if found == "false":
            out = "ORGANIZACION POLITICA" + "\t" + i.strip()
            print out.encode("utf-8")

