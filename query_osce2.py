# -*- coding: utf-8 -*-
import codecs
import json
import socket
import sys

from bs4 import BeautifulSoup
import requesocks as req_socks


'''
Usar luego de depurar datos descargados con ``query_osce2.py``.
Trata de descargar aquellos que no pudieron ser descargados antes debido a
Timout errors.

Hace pedidos a la web de la OSCE para descargar personas registradas como
proveedores del Estado.
http://www.osce.gob.pe/consultasenlinea/rnp_consulta/ProveedoresInscritos.asp

por ejemplo busca por RNP del 00001 al 00100:

    ``python query_osce2.py 1 100``

Resultados seran grabados en archivo out_osce.tsv.
'''

_tor_proxies = {'http': 'socks5://127.0.0.1:9050',
                'https': 'socks5://127.0.0.1:9050'}

_headers = {
    "Content-Length": "49",
}

TIMEOUT = 3

def get_by_rnp(number, TIMEOUT):
    payload = {
        #"action": "enviar",
        "txtRuc": "",
        "txtRnp": str(number),
        "cmbCapitulo": "",
        "cmbTipoPersona": "",
    }

    kargs = {
        "data": payload,
        "headers": _headers,
        "timeout": TIMEOUT,
    }

    url = "http://www.osce.gob.pe/consultasenlinea/rnp_consulta/ProveedoresInscritos.asp?action=enviar"
    tor_req = req_socks.session()
    tor_req.proxies = _tor_proxies
    try:
        r = tor_req.post(url, **kargs)
        name = extract_name(r.text)
        if name is not None:
            with codecs.open("out_osce.tsv", "a") as myfile:
                myfile.write(number.encode("utf-8") + "\t")
                myfile.write(name.encode("utf-8") + "\n")
    except req_socks.exceptions.Timeout:
        with codecs.open("out_osce.tsv", "a") as myfile:
            out = "Timeout error %s" % number.encode("utf-8")
            myfile.write(out + "\n")
    except socket.timeout:
        with codecs.open("out_osce.tsv", "a") as myfile:
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


# keep downloaded IDs in RAM
descargados = []
for i in codecs.open("out_osce.tsv", "r", "utf-8"):
    i = i.strip()
    if not i.startswith("Time"):
        i = i.split()
        descargados.append(i[0])


start_id = sys.argv[1].strip()
end_id = sys.argv[2].strip()

for i in range(int(start_id), int(end_id)):
    i = str(i).zfill(5)
    if i not in descargados:
        print "Descargando %s" % i
        get_by_rnp(i, TIMEOUT)
