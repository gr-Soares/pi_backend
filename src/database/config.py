from pymongo import MongoClient

from decouple import config

url = config("DB_URL", default="localhost")

conn = MongoClient(url, 27017)
client = conn.autonomia

profiossional_exists_email = False
profiossional_exists_usuario = False
for i in client.PORTIFOLIO.list_indexes():
    if(i == "email_un"):
        profiossional_exists_email = True
        break
    if(i == "user_un"):
        profiossional_exists_usuario = True
        break

if(not profiossional_exists_email):
    client.PORTIFOLIO.create_index("email", name="email_un" ,unique=True)
if(not profiossional_exists_email):
    client.PORTIFOLIO.create_index("user", name="user_un" ,unique=True)


cliente_exists_email = False
cliente_exists_usuario = False
for i in client.CLIENTE.list_indexes():
    if(i == "email_un"):
        cliente_exists_email = True
        break
    if(i == "user_un"):
        cliente_exists_usuario = True
        break

if(not cliente_exists_email):
    client.CLIENTE.create_index("email", name="email_un" ,unique=True)
if(not cliente_exists_usuario):
    client.CLIENTE.create_index("user", name="user_un" ,unique=True)