import time
import json

from selenium import webdriver


candidato_id = 104272

url = "http://200.48.102.67/pecaoe/sipe/HojaVida.htm?c="
url += str(candidato_id) + "&p=72&op=140"

browser = webdriver.Firefox()
browser.get(url)
time.sleep(4)

obj = {}

content = browser.find_element_by_xpath('//span[@id="txtCargoPostula"]')
obj['cargo_postula'] = content.text

content = browser.find_element_by_xpath('//span[@id="txtLugarPostula"]')
obj['lugar_postula'] = content.text

content = browser.find_element_by_xpath('//span[@id="txtDNI"]')
obj['dni'] = content.text

content = browser.find_element_by_xpath('//span[@id="txtApellidoPaterno"]')
obj['apellido_paterno'] = content.text

content = browser.find_element_by_xpath('//span[@id="txtApellidoMaterno"]')
obj['apellido_materno'] = content.text

content = browser.find_element_by_xpath('//span[@id="txtNombres"]')
obj['nombres'] = content.text

content = browser.find_element_by_xpath('//span[@id="txtFechaNacimiento"]')
obj['fecha_nacimiento'] = content.text

content = browser.find_element_by_xpath('//span[@id="txtCorreoElectronico"]')
obj['correo_electronico'] = content.text

content = browser.find_element_by_xpath('//span[@id="txtLugarResicencia"]')
obj['lugar_residencia'] = content.text

content = browser.find_element_by_xpath('//span[@id="txtLugarDepartamentoRes"]')
obj['lugar_departamento_residencia'] = content.text

content = browser.find_element_by_xpath('//span[@id="txtLugarProvinciaRes"]')
obj['lugar_provincia_residencia'] = content.text

content = browser.find_element_by_xpath('//span[@id="txtLugarDistritoRes"]')
obj['lugar_distrito_residencia'] = content.text

content = browser.find_element_by_xpath('//span[@id="txtTiempoRes"]')
obj['lugar_tiempo_residencia'] = content.text


print json.dumps(obj, indent=4)
