# -*- coding: utf-8 -*-
import codecs
import json
import re
import locale
import glob
import sys

from bs4 import BeautifulSoup


'''
Extrae nombres, apellidos, dni y monto que deben personas debido a juicio por
alimentos. Info tomada de REDAM usando curl.
'''
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
    deudas = []
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
    return obj


for filename in glob.glob("*html"):
    obj = extract_name(filename)
    with codecs.open("deudores_redam.txt", "a", "utf-8") as f:
        f.write(json.dumps(obj) + "\n")

