from pymongo import MongoClient

uri = "mongodb://localhost:27017/"
cliente = MongoClient(uri)
db = cliente.carros 
colecao = db.carro  

def inserir_carro_nao_relacional(marca, modelo, ano, em_estoque):
    dados_carro = {
        'marca': marca,
        'modelo': modelo,
        'ano': ano,
        'em_estoque': em_estoque,
    }
    colecao.insert_one(dados_carro)

def deletar_carro_nao_relacional(carro_id):
    colecao.delete_one({'_id': carro_id})

def ler_carro_nao_relacional(carro_id):
    return colecao.find_one({'_id': carro_id})

def atualizar_carro_nao_relacional(carro_id, marca, modelo, ano, em_estoque):
    novo_valor = {
        '$set': {
            'marca': marca,
            'modelo': modelo,
            'ano': ano,
            'em_estoque': em_estoque
        }
    }
    colecao.update_one({'_id': carro_id}, novo_valor)
