#-*- coding: utf-8 -*-
import codecs
import json
import sys


input_file = sys.argv[1].strip()


out = "DNI\tAPELLIDO PATERNO\tAPELLIDO MATERNO\tNOMBRES\tMONTO DEUDA\tURL\n"
for i in codecs.open(input_file, "r", "utf-8"):
    i = i.strip()
    i = json.loads(i)
    out += i['dni'] + "\t" + i['apellido_paterno'] + "\t"
    out += i['apellido_materno'] + "\t" + i['nombres'] + "\t"
    out += str(i['debe']) + "\t" + i['url'] + "\n"

with codecs.open("todos_deudores_REDAM.tsv", "w", "utf-8") as f:
    f.write(out)
