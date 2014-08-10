#-*- coding: utf-8 -*-
import codecs
import re
import sys


'''
Cruza información entre lista de candidatos y lista de proveedores al Estado
descargados de la OSCE (scripts ``query_osce.py`` ``query_osce2.py``).
'''

if len(sys.argv) < 3:
    print "Error. Usar lista candidatos, proveedores y outfile como argumentos"
    sys.exit()

candidatos = sys.argv[1].strip()
proveedores = sys.argv[2].strip()
outfile = sys.argv[3].strip()


def make_list_from_name(name):
    name = name.strip()
    name = re.sub(",", " ", name)
    name = re.sub("\s+", " ", name)
    name = name.split(" ")
    return name


def compara_nombres(candidato, proveedor):
    candidato = make_list_from_name(candidato)
    proveedor = make_list_from_name(proveedor)
    score = 0
    for i in candidato:
        if i in proveedor:
            score += 1
    return score


#candidato = "TORRES  FRANCISCO ANTONIO"
#proveedor = "CCI CONSTRUCCIONES S.A. SUCURSAL PERU"

# extrae candidatos nombres
candidatos_nombres = []
for i in codecs.open(candidatos, "r", "utf-8").readlines():
    i = i.strip().split("\t")
    nombre = i[8] + " " + i[9] + " " + i[10]
    obj = dict()
    obj['nombre'] = nombre
    obj['dni'] = i[0]
    candidatos_nombres.append(obj)


for line in codecs.open(proveedores, "r", "utf-8").readlines():
    i = line.strip().split("\t")
    if len(i) > 1:
        proveedor = i[1]

        for candidato in candidatos_nombres:
            score = compara_nombres(candidato['nombre'], proveedor)
            if score > 3:
                with codecs.open(outfile, "a", "utf-8") as f:
                    out = "\ncandidato %s" % candidato['nombre']
                    out += "\nproveedor %s" % proveedor
                    out += "\nFound candidato proveedor:\t%s" % line.strip()
                    f.write(out)
                    print out.encode("utf-8")

