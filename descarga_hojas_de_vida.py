# -*- coding: utf-8 -*-
import codecs
import time
import json
import re
import sys

from selenium import webdriver


'''
Descargaba hojas de vida de la web del JNE. Ya no funciona por que el JNE
decidió encriptar los URL.
'''


firefoxpreferences = webdriver.FirefoxProfile()
firefoxpreferences.set_preference("network.proxy.type", 1)
firefoxpreferences.set_preference("network.proxy.socks", "127.0.0.1")
firefoxpreferences.set_preference("network.proxy.socks_port", 9050)

browser = webdriver.Firefox(firefoxpreferences)


def download(candidato_id, browser, outputfile):

    url = "http://200.48.102.67/pecaoe/sipe/HojaVida.htm?c="
    url += str(candidato_id) + "&p=72&op=140"
    obj = {}

    browser.get(url)
    time.sleep(4)

    content = browser.find_element_by_xpath('//span[@id="txtCargoPostula"]')
    obj['cargo_postula'] = content.text

    content = browser.find_element_by_xpath('//span[@id="txtLugarPostula"]')
    obj['lugar_postula'] = content.text

    content = browser.find_element_by_xpath('//span[@id="txtFormaDesignacion"]')
    obj['forma_designacion'] = content.text

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

    content = browser.find_element_by_xpath('//span[@id="txtSexo"]')
    obj['sexo'] = content.text

    content = browser.find_element_by_xpath('//span[@id="txtCorreoElectronico"]')
    obj['correo_electronico'] = content.text

    content = browser.find_element_by_xpath('//span[@id="txtPais"]')
    obj['pais'] = content.text

    content = browser.find_element_by_xpath('//span[@id="txtDepartamentoNac"]')
    obj['departamento_nacimiento'] = content.text

    content = browser.find_element_by_xpath('//span[@id="txtProvinciaNac"]')
    obj['provincia_nacimiento'] = content.text

    content = browser.find_element_by_xpath('//span[@id="txtDistritoNac"]')
    obj['distrito_nacimiento'] = content.text

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

    content = browser.find_element_by_xpath('//span[@id="txtPadre"]')
    obj['nombres_del_padre'] = content.text

    content = browser.find_element_by_xpath('//span[@id="txtMadre"]')
    obj['nombres_de_madre'] = content.text

    content = browser.find_element_by_xpath('//span[@id="txtConyuge"]')
    obj['nombres_de_conyuge'] = content.text

    experiencia = []

    for i in browser.find_elements_by_xpath('//table[@id="tblExperiencia"]//*[td or th]'):
        if re.search("Centro de trabajo (.+) Sector", i.text):
            item = {}
            res_ct = re.search("Centro de trabajo (.+) Sector", i.text)
            item['centro_de_trabajo'] = res_ct.groups()[0]

            res = re.search("Sector (.+)", i.text)
            item['sector'] = res.groups()[0]
        elif re.search("Fecha desde (.+) Fecha hasta", i.text):
            res = re.search("Fecha desde (.+) Fecha hasta", i.text)
            item['fecha_desde'] = res.groups()[0]

            res = re.search("Fecha hasta (.+)", i.text)
            item['fecha_hasta'] = res.groups()[0]
        elif re.search("Cargo ", i.text):
            res = re.search(u"Cargo (.+) Ubicacion", i.text)
            item['cargo'] = res.groups()[0]

            res = re.search(u"Ubicacion (.+)", i.text)
            item['ubicacion'] = res.groups()[0]
            experiencia.append(item)

    obj['experiencia'] = experiencia

    primaria = []
    for i in browser.find_elements_by_xpath('//table[@id="tblEducacionPrimaria"]//*[td or th]'):
        res = re.search("Educativa (.+) Lugar", i.text)
        if res:
            item = {}
            item['inst_educ'] = res.groups()[0]
        res = re.search("Lugar (.+)", i.text)
        if res:
            item['lugar'] = res.groups()[0]
        res = re.search(u"Concluido (.+) Período (.+)", i.text)
        if res:
            item['concluido'] = res.groups()[0]
            item['periodo'] = res.groups()[1]
            primaria.append(item)
    obj['edu_primaria'] = primaria

    secundaria = []
    for i in browser.find_elements_by_xpath('//table[@id="tblEducacionSecundaria"]//*[td or th]'):
        res = re.search("Educativa (.+) Lugar", i.text)
        if res:
            item = {}
            item['inst_educ'] = res.groups()[0]
        res = re.search("Lugar (.+)", i.text)
        if res:
            item['lugar'] = res.groups()[0]
        res = re.search(u"Concluido (.+) Período (.+)", i.text)
        if res:
            item['concluido'] = res.groups()[0]
            item['periodo'] = res.groups()[1]
            secundaria.append(item)
    obj['edu_secundaria'] = secundaria

    tecnico = []
    for i in browser.find_elements_by_xpath('//table[@id="tblTecnico"]//*[td or th]'):
        res = re.search("Nombre del centro de estudios (.+)", i.text)
        if res:
            item = {}
            item['inst_educ'] = res.groups()[0]
        res = re.search("Lugar (.+)", i.text)
        if res:
            item['lugar'] = res.groups()[0]
        res = re.search("Especialidad (.+)", i.text)
        if res:
            item['especialidad'] = res.groups()[0]
        res = re.search("Curso (.+)", i.text)
        if res:
            item['curso'] = res.groups()[0]
        res = re.search("Estado (.+)", i.text)
        if res:
            item['estado'] = res.groups()[0]
        res = re.search("Periodo (.+)", i.text)
        if res:
            item['periodo'] = res.groups()[0]
            tecnico.append(item)
    obj['edu_tecnica'] = tecnico

    f = codecs.open(outputfile, "a", "utf-8")
    f.write(json.dumps(obj) + "\n")
    f.close()

outputfile = sys.argv[1].strip()
for i in range(104272, 104273):
    download(i, browser, outputfile)
