# -*- coding: utf-8 -*-
import codecs
import json
import socket
import sys

from bs4 import BeautifulSoup
import requests
'''
Hace pedidos a la web dela REDAM para descargar personas deudoras por
cuestiones de alimentos.
http://casillas.pj.gob.pe/redamWeb/index.faces


'''

_tor_proxies = {'http': 'socks5://127.0.0.1:9050',
                'https': 'socks5://127.0.0.1:9050'}

_headers = {
    "Content-Length": "115",
}

TIMEOUT = 3

def get_by_dni(dni, TIMEOUT):
payload = {
    #"action": "enviar",
    "form1:cboDocumentoTipo": "01",
    "form1:textNumeroDocumento1": str(dni),
    "form1:btnBuscarDeudor": "Buscar+Deudor",
    "form1": "form1",
}
kargs = {
    "data": payload,
    "headers": _headers,
    "timeout": TIMEOUT,
}

    url = "http://casillas.pj.gob.pe/redamWeb/index.faces"
    tor_req = req_socks.session()
    tor_req.proxies = _tor_proxies
    try:
        r = requests.post(url, **kargs)
        print r.text.encode("utf-8")
        sys.exit()
        name = extract_name(r.text)
        if name is not None:
            with codecs.open("out_redam.tsv", "a") as myfile:
                myfile.write(number.encode("utf-8") + "\t")
                myfile.write(name.encode("utf-8") + "\n")
    except req_socks.exceptions.Timeout:
        with codecs.open("out_redam.tsv", "a") as myfile:
            out = "Timeout error %s" % number.encode("utf-8")
            myfile.write(out + "\n")
    except socket.timeout:
        with codecs.open("out_redam.tsv", "a") as myfile:
            out = "Timeout error %s" % number.encode("utf-8")
            myfile.write(out + "\n")


def extract_name(html):
    soup = BeautifulSoup(html)
    name = soup.find_all('td', 'TDData')
    if len(name) > 1:
        name = name[2].text
        print name.encode("utf-8")
        return name
    else:
        return None


dni_file = sys.argv[1].strip()

for i in open(dni_file, "r").readlines():
    dni = i.strip()
    get_by_dni(dni, TIMEOUT)
