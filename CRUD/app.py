
from flask import Flask, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from sql import inserir_carro_relacional, ler_carro_relacional, atualizar_carro_relacional, deletar_carro_relacional, Carro, sessao  
from mongo import inserir_carro_nao_relacional, ler_carro_nao_relacional, atualizar_carro_nao_relacional, deletar_carro_nao_relacional, colecao  

app = Flask(__name__)

# Rotas para manipulação do banco de dados relacional
@app.route('/carros_relacional', methods=['GET', 'POST'])
def carros_relacional():
    if request.method == 'GET':
        try:
            carros = [ler_carro_relacional(carro.id) for carro in sessao.query(Carro).all()]
            return jsonify(carros)
        except SQLAlchemyError as e:
            return str(e), 500
    elif request.method == 'POST':
        data = request.json
        marca = data.get('marca')
        modelo = data.get('modelo')
        ano = data.get('ano')
        em_estoque = data.get('em_estoque')
        try:
            inserir_carro_relacional(marca, modelo, ano, em_estoque)
            return 'Carro inserido com sucesso', 201
        except SQLAlchemyError as e:
            return str(e), 400

@app.route('/carros_relacional/<int:carro_id>', methods=['GET', 'PUT', 'DELETE'])
def carro_relacional(carro_id):
    if request.method == 'GET':
        try:
            carro = ler_carro_relacional(carro_id)
            if carro:
                return jsonify(carro)
            else:
                return 'Carro não encontrado', 404
        except SQLAlchemyError as e:
            return str(e), 500
    elif request.method == 'PUT':
        data = request.json
        marca = data.get('marca')
        modelo = data.get('modelo')
        ano = data.get('ano')
        em_estoque = data.get('em_estoque')
        try:
            if atualizar_carro_relacional(carro_id, marca, modelo, ano, em_estoque):
                return 'Carro atualizado com sucesso', 200
            else:
                return 'Carro não encontrado', 404
        except SQLAlchemyError as e:
            return str(e), 400
    elif request.method == 'DELETE':
        try:
            deletar_carro_relacional(carro_id)
            return 'Carro deletado com sucesso', 200
        except SQLAlchemyError as e:
            return str(e), 400

# Rotas para manipulação do banco de dados não relacional
@app.route('/carros_nao_relacional', methods=['GET', 'POST'])
def carros_nao_relacional():
    if request.method == 'GET':
        try:
            carros = [carro for carro in colecao.find()]
            return jsonify(carros)
        except Exception as e:
            return str(e), 500
    elif request.method == 'POST':
        data = request.json
        marca = data.get('marca')
        modelo = data.get('modelo')
        ano = data.get('ano')
        em_estoque = data.get('em_estoque')
        try:
            inserir_carro_nao_relacional(marca, modelo, ano, em_estoque)
            return 'Carro inserido com sucesso', 201
        except Exception as e:
            return str(e), 400

@app.route('/carros_nao_relacional/<carro_id>', methods=['GET', 'PUT', 'DELETE'])
def carro_nao_relacional(carro_id):
    if request.method == 'GET':
        try:
            carro = ler_carro_nao_relacional(carro_id)
            if carro:
                return jsonify(carro)
            else:
                return 'Carro não encontrado', 404
        except Exception as e:
            return str(e), 500
    elif request.method == 'PUT':
        data = request.json
        marca = data.get('marca')
        modelo = data.get('modelo')
        ano = data.get('ano')
        em_estoque = data.get('em_estoque')
        try:
            atualizar_carro_nao_relacional(carro_id, marca, modelo, ano, em_estoque)
            return 'Carro atualizado com sucesso', 200
        except Exception as e:
            return str(e), 400
    elif request.method == 'DELETE':
        try:
            deletar_carro_nao_relacional(carro_id)
            return 'Carro deletado com sucesso', 200
        except Exception as e:
            return str(e), 400

if __name__ == '__main__':
    app.run(debug=True)