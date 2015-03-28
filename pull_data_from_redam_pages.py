# -*- coding: utf-8 -*-
import codecs
import json
import glob
import re

from bs4 import BeautifulSoup

"""
Extrae nombres, apellidos, dni y monto que deben los ciudadanos por
concepto de juicio por alimentos. Info tomada de REDAM usando curl.
Este script actúa sobre archivos HTML.

curl 'http://casillas.pj.gob.pe/redamWeb/_rlvid.jsp.faces?_rap=pc_Index.obtenerDeudor&_rvip=/index.jsp&idDeudor=[1-3000]' -o '#1.html'
"""


def to_number(string):
    x = string.replace(",", "")
    x = float(x)
    return x


def extract_name(filename):
    this_id = filename.replace(".html", "")
    html = codecs.open(filename, "r", "latin1").read()
    soup = BeautifulSoup(html)
    name = soup.find(id='form1:text155').get_text()
    apellido_paterno = soup.find(id='form1:text156').get_text()
    apellido_materno = soup.find(id='form1:text157').get_text()
    dni = soup.find(id='form1:text158').get_text()
    debe = soup.find_all('span', id=re.compile(".+textNimpadeudado1"))
    dinero = 0
    for i in debe:
        dinero += to_number(i.get_text())

    obj = dict()
    obj['nombres'] = name
    obj['apellido_paterno'] = apellido_paterno
    obj['apellido_materno'] = apellido_materno
    obj['dni'] = dni
    obj['debe'] = dinero
    obj['url'] = "http://casillas.pj.gob.pe/redamWeb/_rlvid.jsp.faces?_rap=pc_Index.obtenerDeudor&_rvip=/index.jsp&idDeudor=" + this_id
    obj['vinculo'] = get_vinculo(soup)
    return obj


def get_vinculo(soup):
    """
    Devuelve datos de persona vinculada a nuestro usuario. Ejemplo:
    - demandante, nombre completo
    """
    vinculos = []
    items = soup.find_all(id=re.compile('form1:tableEx[0-9]:[0-9]:tableEx4.0+'))
    for item in items:
        if 'vinculo' in item['id']:
            vinculo = item.get_text()
        if 'Nombre' in item['id']:
            nombre_completo = item.get_text()
            vinculos.append({'vinculo': vinculo, 'nombre_completo': nombre_completo})

    return list({v['vinculo']: v for v in vinculos}.values())


for filename in glob.glob("*html"):
    obj = extract_name(filename)
    with codecs.open("deudores_redam.json", "a", "utf-8") as f:
        f.write(json.dumps(obj) + "\n")
