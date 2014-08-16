#-*- coding: utf-8 -*-
""" Parse tsv file output HTML table deudores"""

import collections
import codecs
import operator
import sys

import locale

locale.setlocale(locale.LC_ALL, "en_US.utf8")



input_file = sys.argv[1].strip()

def to_number(string):
    x = float(string)
    return locale.format("%d", x, grouping=True)

# header
out = "<html><head><meta charset='utf-8'>"
out += "<link rel='stylesheet' href='bootstrap/css/bootstrap.min.css'>"
out += "<style>table { font-size: 10px; font-family: Verdana, Arial, serif; }</style>"
out += "</head>"


# table
out += u"<body>"
out += u"<div class='table-responsive'>"
out += u"<table class='table table-striped'><thead><tr>"
out += u"<th>Departamento</th><th>Provincia</th><th>Distrito</th>"
out += u"<th>Candidato</th><th>Partido político</th>"

out += u"<th>Cargo que postula</th>"

out += u"<th>Reparación Civil</th><th>Pagos Realizados</th>"
out += u"<th>Pagos Pendientes</th><th>Delito</th>"

out += u"</tr></thead><tbody>\n"

for line in codecs.open(input_file, "r", "utf-8").readlines():
    line = line.strip()

    if line.startswith("DNI"):
        continue
    line = line.split("\t")

    out += "<td>" + line[5] + "</td>"
    out += "<td>" + line[6].title() + "</td>"
    out += "<td>" + line[7].title() + "</td>"

    out += u"<td><a title='Link hacia página del MinJus' href='" 
    out += line[8] + "' target='_blank'>"
    out += line[1].upper() + ", " + line[2].upper() + "</a></td>"

    out += "<td>" + line[3] + "</td>"

    out += "<td>" + line[4] + "</td>"

    out += "<td>" + to_number(line[13]) + "</td>"
    out += "<td>" + to_number(line[14]) + "</td>"
    out += "<td>" + to_number(line[15]) + "</td>"

    out += "<td>" + line[18][:33] + "</td>"


    out += "</tr>\n"

out += "</tbody></table>"
out += "</div>"
out += "</body></html>"
print out.encode("utf-8")





