#-*- coding: utf-8 -*-
import codecs
import re
import sys


input_file = sys.argv[1].strip()

data = []
for i in codecs.open(input_file, "r", "utf-8"):
    i = i.strip()
    i = i.split("\t")
    obj = dict()
    obj['dni'] = i[1]
    obj['departamento'] = i[2]

    coord = i[3].split(",")
    if len(coord) > 1:
        obj['lat'] = coord[0]
        obj['long'] = coord[1]
        data.append(obj)

out = ""
for i in data:
    out += "\t[" + i['lat'] + "," + i['long'] + "],\n"

out = out.strip()
out = re.sub(",$", "", out)

html = open("base.html", "r").read()
html = html.replace("{{ content }}", out)
print html
