from flask import Flask, render_template, request
import json
from banco_service import *
from relatorio_service import *
from metodos_service import *
from sistema_service import *

instance_bd = bd()

app = Flask(__name__)

# Metodologia de retorno: {metodo, url, dados, bd}

@app.route('/sistema', methods=['GET'])
def sistema():
    if request:
        return formatar_sistema(instance_bd)

@app.route('/relatorio', methods=['GET'])
def relatorio():
    if request:
        return formatar_relatorio(instance_bd)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def index():
    if request:
        if request.args.get('dados'):
            return handler(request.method, request.url, request.args.get('dados'), instance_bd)
        else:
            return handler(request.method, request.url, request.data.decode(), instance_bd)
if __name__ == '__main__':
    app.run()

