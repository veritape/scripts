import json
import requesocks as requests


url = "http://200.48.102.67/pecaoe/sipe/HojaVida.htm?c=104272&p=72&op=140"
urls = [
        "http://200.48.102.67/pecaoe/servicios/declaracion.asmx/OP_ObtenerNombrePorID",
        ]
parameters = {"objProcesoElectoralBE":{"intIdProceso":"72"},"intCod_OP":"140"}
payload = {'objOPInscritasBE': parameters }
payload = json.dumps(payload)

session = requests.session()
session.proxies = {'http': 'socks5://127.0.0.1:9050',
                  'https': 'socks5://127.0.0.1:9050'}

chunked = str(len(payload)-5)
print chunked
r = session.post(url=urls[0], 
        params=payload, 
        headers={
            'Content-Length': '86',
            'Referer': 'http://200.48.102.67/pecaoe/sipe/HojaVida.htm?c=104272&p=72&op=140',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0',
            'Content-Type': 'application/json; charset=UTF-8',
            })
print(r.status_code)
print(r.headers['content-type'])
print(r.text)
