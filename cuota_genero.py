# -*- coding: utf-8 -*-
import codecs
import glob
import subprocess


'''
Obtiene porcentaje femenino en listas de candidatos.
'''


filename = "hoja.tsv.0"

def make_files():
    for line in codecs.open(filename, "r", "utf-8").readlines():
        line = line.strip()
        line = line.split("\t")
        op = "op/" + "op_" + line[5].replace(" ", "_") + ".tsv"

        f = codecs.open(op, "a", "utf-8")
        if line[11].lower() == "masculino":
            f.write(line[5] + "\t" + line[11] + "\n")
        if line[11].lower() == "femenino":
            f.write(line[5] + "\t" + line[11] + "\n")
        f.close()

#make_files()
print "ORG POLITICA\tMASCULINO\tFEMENINO\tCUOTA FEMENINA(%)"
for i in glob.glob("op/*"):
    out = ""
    op = i.replace("op/op_", "")
    op = op.replace(".tsv", "")

    cmd = "grep -c 'MASCULINO' " + i
    p = subprocess.check_output(cmd, shell=True)
    masculino = p.strip()
    out += op + "\t" + masculino + "\t" 

    cmd = "grep -c 'FEMENINO' " + i
    p = subprocess.check_output(cmd, shell=True)
    femenino = p.strip()
    out += femenino

    total = int(femenino) + int(masculino)
    cuota = float(femenino)*100/float(total)
    out += "\t" + str(cuota)
    print out
