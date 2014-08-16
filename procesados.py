# -*- coding: utf-8 -*-
'''
Parse tsv file extrae sentenciados que no han sido absueltos
'''


import collections
import codecs
import operator


keywords = [
    'ABSOLUCION',
    'ABSUELTO',
    'ARCHIVO',
    'ANULACION',
    'ANULAR',
    'ANULESE',
    'ARCHIVADA',
    'ARCHIVADO',
    'ARCHIVAMIENTO',
    'ARCHIVESE',
    'DENEGADO',
    'EXTINGUIDO',
    'FAVORABLE',
    'IMPROCEDENTE',
    'INFUNDADO',
    'INOCENTE',
    'NEGATIVO',
    'NINGUNA',
    'NO ACUSACION PENAL',
    'NO COMPROBADO',
    'NULIDAD',
    'PRESCRITO',
    'SOBRESEIDO',
]

input_file = "hoja.tsv.3_sorted"

procesados = []
for line in codecs.open(input_file, "r", "utf-8").readlines():
    line = line.strip()

    absuelto = "false"
    for word in keywords:
        if word in line:
            absuelto = "true"

    if absuelto == "false":
        line = line.split("\t")
        obj = dict()
        obj['id'] = line[0]
        obj['nombre'] = line[4] + " " + line[2] + " " + line[3]
        obj['acusacion'] = line[8]
        obj['fallo'] = line[9]
        procesados.append(obj)


def total_procesados(procesados):
    nombres = []
    for i in procesados:
        nombres.append(i['nombre'])
    nombres = sorted(set(nombres))
    return "<h2>Total procesados con sentencia condenatoria %i</h2>" % len(nombres)


def ranking_delitos(procesados):
    delitos = []
    for i in procesados:
        delitos.append(i['acusacion'])
    counter = collections.Counter(delitos)
    return counter.most_common(50)


def make_table_procesados(procesados):
    procesados_s = sorted(procesados, key=operator.itemgetter('nombre'))
    out = "<table>"
    out += u"\n<thead><th>Nombre</th><th>Acusación</th><th>Fallo</th></thead>"
    out += "\n<tbody>"
    for i in procesados_s:
        out += "<tr>"
        out += "<td><a href='http://200.48.102.67/pecaoe/sipe/HojaVida.htm?c="
        out += i['id'] + "&p=72&op=160' target='_blank'>"
        out += i['nombre'].title() + "</a></td>"
        out += "<td>" + i['acusacion'].title() + "</td>"
        out += "<td>" + i['fallo'] + "</td>"
        out += "</tr>"
        out += "\n"
    out += "</tbody>"
    out += "</table>"
    return out


""" Use a keyword para seleccionar delitos de interes """


def make_table_de_tal_delito(procesados, keyword):
    procesados_s = sorted(procesados, key=operator.itemgetter('nombre'))
    out = "<table>"
    out += u"\n<thead><th>Nombre</th><th>Acusación</th><th>Fallo</th></thead>"
    out += "\n<tbody>"
    for i in procesados_s:
        if keyword.lower() in i['acusacion'].lower():
            out += "<tr>"
            out += "<td><a href='http://200.48.102.67/pecaoe/sipe/HojaVida.htm?c="
            out += i['id'] + "&p=72&op=160' target='_blank'>"
            out += i['nombre'].title() + "</a></td>"
            out += "<td>" + i['acusacion'].title() + "</td>"
            out += "<td>" + i['fallo'] + "</td>"
            out += "</tr>"
            out += "\n"
    out += "</tbody>"
    out += "</table>"
    return out


print total_procesados(procesados)
for k, v in ranking_delitos(procesados):
    print "'" + k[0:25] + "',"
numeros = ""
for k, v in ranking_delitos(procesados):
    numeros += str(v) + ", "
print numeros

print make_table_procesados(procesados).encode("utf-8")

print "<h2>Sentenciados por Violación</h2>"
print make_table_de_tal_delito(procesados, "violaci").encode("utf-8")

print "<h2>Sentenciados por Homicidio</h2>"
print make_table_de_tal_delito(procesados, "homicidio").encode("utf-8")

print "<h2>Sentenciados por Matrimonio Ilegal-Bigamia</h2>"
print make_table_de_tal_delito(procesados, "matrimonio ilegal").encode("utf-8")

print "<h2>Sentenciados por Terrorismo</h2>"
print make_table_de_tal_delito(procesados, "terrorismo").encode("utf-8")

print "<h2>Sentenciados por Tráfico de Drogas</h2>"
print make_table_de_tal_delito(procesados, "drogas").encode("utf-8")
