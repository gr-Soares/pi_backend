from pymongo import MongoClient

from decouple import config

from ..models.atuacao import Atuacao

url = config("DB_URL", default="localhost")

conn = MongoClient(url, 27017)
client = conn.autonomia

profiossional_exists_email = False
profiossional_exists_usuario = False
for i in client.PROFISSIONAL.list_indexes():
    if(i == "user_un"):
        profiossional_exists_usuario = True
        break

if(not profiossional_exists_email):
    client.PORTIFOLIO.create_index("user", name="user_un" ,unique=True)


cliente_exists_email = False
cliente_exists_usuario = False
for i in client.CLIENTE.list_indexes():
    if(i == "user_un"):
        cliente_exists_usuario = True
        break

if(not cliente_exists_usuario):
    client.CLIENTE.create_index("user", name="user_un" ,unique=True)


if(not client.ATUACAO.find_one({"descricao": "Eletricista"})):
    data = Atuacao(descricao="Eletricista")
    client.ATUACAO.insert_one(data.to_json())

if(not client.ATUACAO.find_one({"descricao": "Encanador"})):
    data = Atuacao(descricao="Encanador")
    client.ATUACAO.insert_one(data.to_json())

if(not client.ATUACAO.find_one({"descricao": "Pedreiro"})):
    data = Atuacao(descricao="Pedreiro")
    client.ATUACAO.insert_one(data.to_json())

if(not client.ATUACAO.find_one({"descricao": "Marceneiro"})):
    data = Atuacao(descricao="Marceneiro")
    client.ATUACAO.insert_one(data.to_json())

if(not client.ATUACAO.find_one({"descricao": "Geral"})):
    data = Atuacao(descricao="Geral")
    client.ATUACAO.insert_one(data.to_json())

if(not client.ATUACAO.find_one({"descricao": "Jardineiro"})):
    data = Atuacao(descricao="Jardineiro")
    client.ATUACAO.insert_one(data.to_json())