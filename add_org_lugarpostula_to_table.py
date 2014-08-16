#-*- coding: utf-8 -*-
import codecs
import sys


# file that needs lugar postula
input_file = "hojas_3_4"

# file 0 as reference
ref_file = "hoja.tsv.0"
lugar_que_postula = []
for i in codecs.open(ref_file, "r", "utf-8").readlines():
    # header
    if i.startswith("DNI"):
        continue
    i = i.strip().split("\t")
    # list: dni, departamento, provincia, distrito al que postula
    lista = [ i[0], i[1], i[2], i[3] ]
    lugar_que_postula.append(lista)

for i in codecs.open(input_file, "r", "utf-8").readlines():
    # header
    out = ""
    line = i.strip().split("\t")
    dni = line[1]

    found = "false"
    for j in lugar_que_postula:
        if dni == j[0]:
            out = j[1] + "\t" + j[2] + "\t" + j[3] + "\t"
            out += i.strip()
            print out.encode("utf-8")
            found = "true"
            break
    # this is the header row
    if found == "false":
        out = "DEPARTAMENTO POSTULA" + "\t"
        out += "PROVINCIA POSTULA" + "\t"
        out += "DISTRITO POSTULA" + "\t"
        out += i.strip()
    print out.encode("utf-8")

