import json
from flask import send_file

def formatar_relatorio(bd):
    result = bd.model_consult("select * from Dados where situacao != 'COM' order by data;", "")
    sistemas = json.loads(bd.model_consult("Select distinct sistema from Dados;", ""))
    print(sistemas)
    out = "\n"
    for sis in sistemas:
        out = out + "DEPARTAMENTO DE " + sis[0].upper() + "\n"
        out = out + "...ID || NOME || DATA || SITUAÇÃO\n"
        entradas = json.loads(bd.model_consult("Select * from Dados where sistema = '{}' and situacao != 'COM' order by data;".format(sis[0]), ""))
        for entrada in entradas:
            out = out + "......{} || {} || {} || {} || {}\n".format(str(entrada[0]), entrada[1], str(entrada[2]), entrada[3], entrada[4])
    out = out + "FIM RELATÓRIO\n"
    print(out)
    try:
        f = open("relatorio.txt", 'w')
        f.write(out)
        f.close()
    except OSError as e:
        print(e)
    return send_file("./relatorio.txt", as_attachment=True)

"""
def formatar_string(entrada):
    entrada = entrada.replace('"', "")
    entrada = entrada.replace('[', "")
    entrada = entrada.replace(']', "")
    return entrada.split(', ')
"""