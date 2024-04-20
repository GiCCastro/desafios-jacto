from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

Base = declarative_base()

class Carro(Base):
    __tablename__ = 'carros'

    id = Column(Integer, primary_key=True)
    marca = Column(String)
    modelo = Column(String)
    ano = Column(Integer)
    em_estoque = Column(Boolean)

motor = create_engine('sqlite:///database.db')

Base.metadata.create_all(motor)

Sessao = sessionmaker(bind=motor)
sessao = Sessao()

def inserir_carro_relacional(marca, modelo, ano, em_estoque):
    novo_carro_relacional = Carro(marca=marca, modelo=modelo, ano=ano, em_estoque=em_estoque)
    sessao.add(novo_carro_relacional)
    sessao.commit()

def deletar_carro_relacional(carro_id):
    carro_relacional = sessao.query(Carro).get(carro_id)
    if carro_relacional:
        sessao.delete(carro_relacional)
        sessao.commit()

def ler_carro_relacional(carro_id):
    carro_relacional = sessao.query(Carro).get(carro_id)
    if carro_relacional:
        return {
            'id': carro_relacional.id,
            'marca': carro_relacional.marca,
            'modelo': carro_relacional.modelo,
            'ano': carro_relacional.ano,
            'em_estoque': carro_relacional.em_estoque
        }
    return None


def atualizar_carro_relacional(carro_id, marca, modelo, ano, em_estoque):
    carro_relacional = sessao.query(Carro).get(carro_id)
    if carro_relacional:
        carro_relacional.marca = marca
        carro_relacional.modelo = modelo
        carro_relacional.ano = ano
        carro_relacional.em_estoque = em_estoque
        sessao.commit()
        return True  
    else:
        return False  
