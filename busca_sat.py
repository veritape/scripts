import requests
import codecs

url = "https://www.sat.gob.pe/homesite2007/modulos/BusquedaTributario.aspx"

#r = requests.get(url)
#my_cookies = r.cookies['ASP.NET_SessionId']
#cookies = {'ASP.NET_SessionId': my_cookies}

payload = {
"mysession": "h3JDoaakPeci74XcV/4o8p4BIqXHVAQjIkIFMTFzwGg=",
"TRI": "P",
"ctl00$cplPrincipal$txtCodigoAdmin": "",
"ctl00$cplPrincipal$ddlTipoDocu": "2",
"ctl00$cplPrincipal$txtDocumento": "46377047",
"ctl00$cplPrincipal$btnBuscaDocumento": "Buscar",
"ctl00$cplPrincipal$txtPaterno": "",
"ctl00$cplPrincipal$txtMaterno": "",
"ctl00$cplPrincipal$txtNombre": "",
"ctl00$cplPrincipal$txtRazon": "",
"ctl00$cplPrincipal$hidPaterno": "",
"ctl00$cplPrincipal$hidMaterno": "",
"ctl00$cplPrincipal$hidNombre": "",
"ctl00$cplPrincipal$hidRazon": "",
"ctl00$cplPrincipal$hidCodVeh": "",
"ctl00$cplPrincipal$hidPlaca": "",
}

#r = requests.post(url, params=payload, cookies=cookies)
r = requests.post(url, params=payload)
print r.text.encode("utf-8")
