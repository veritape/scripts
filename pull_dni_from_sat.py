# -*- coding: utf-8 -*-
import codecs
import sys
import re


'''
Extrae DNIs presentes en lista de morosos del SAT.
'''


sat_file = "Notificacion_Deudas_Tributarias.txt"

dni = []
for i in codecs.open(sat_file, "r", "utf-8"):
    i = i.strip()
    res = re.findall("DNI/LE\s+([0-9]+)", i)
    if res is not None:
        if len(res) > 0:
            dni += res

for i in dni:
    print i
