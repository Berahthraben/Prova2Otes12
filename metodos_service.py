from flask import render_template
from relatorio_service import *
from sistema_service import *

# Intenção desse arquivo é fazer o redirecionamento

def handler(metodo, url, dados, bd):
    if metodo == 'GET':
        if dados:
            if dados == 'relatorio':
                return formatar_relatorio(bd)
            elif dados == 'sistema':
                return str(formatar_sistema(bd))
            else:
                return str(bd.model_consult('SELECT {} FROM Dados'.format(dados), ""))
        else:
            return render_template('index.html')
    elif metodo == 'POST' or metodo == 'PUT':
        if dados:
            dados = dados.replace('[', '')
            dados = dados.replace(']', '')
            dados = dados.replace('"', '')
            dados = dados.split(',')
            query = """INSERT INTO dados VALUES ({}, '{}', '{}', '{}', '{}') ON CONFLICT(id) DO UPDATE SET id={}, nome='{}', data='{}', sistema='{}', situacao='{}' where dados.id = {};""".format(dados[0], dados[1], dados[2], dados[3], dados[4], dados[0], dados[1], dados[2], dados[3], dados[4], dados[0])
            return str(bd.model_create_update(query, dados))
        else:
            return ""
    elif metodo == 'DELETE':
        if dados:
            query = "DELETE FROM Dados WHERE id={}".format(dados)
            return str(bd.model_create_update(query, dados))
        else:
            return ""
    else:
        return ""

"""
def formatar_query(res):
    retorno = []
    for tupla in res:
        retorno.append(dict(tupla))
    return retorno
"""