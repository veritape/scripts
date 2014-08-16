# -*- coding: utf-8 -*-
import codecs


'''
Busca candidatos reubicados por RENIEC en lista de candidatos.
'''


reniec_file = "dni_candidatos_reubicados_x_reniec.csv"

ref_file = "hoja.tsv.0"


dni_candidatos_reubicados = []
for i in codecs.open(reniec_file, "r", "utf-8").readlines():
    i = i.strip()
    dni_candidatos_reubicados.append(i)


for i in codecs.open(ref_file, "r", "utf-8").readlines():
    j = i.strip().split("\t")
    ref_dni = j[0]
    if ref_dni in dni_candidatos_reubicados:
        print i.strip().encode("utf-8")
