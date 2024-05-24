from ..models.atuacao import Atuacao
from ..adapter.auth import encrypt_password
from src.database import client
from src.models import Profissional, Endereco, Contato
from src.adapter import HttpRequest, HttpResponse, HttpErrors
from typing import Type

from bson.objectid import ObjectId


def create_profissional(http_request: Type[HttpRequest]) -> HttpResponse:

    response = None

    if http_request.body:
        try:
            endereco = Endereco(**http_request.body["endereco"])
            contato = Contato(**http_request.body["contato"])
            atuacao = http_request.body["atuacao"]

            http_request.body.pop("endereco")
            http_request.body.pop("contato")
            http_request.body.pop("atuacao")

            atuacao_c = []

            for at in list(atuacao):
                d = dict(at)
                s = client.ATUACAO.find_one({"_id": d["_id"]})
                if s != None:
                    atuacao_c.append(Atuacao(**s))
                else:
                    ob = Atuacao(d["descricao"])
                    client.ATUACAO.insert_one(ob.to_json())
                    atuacao_c.append(ob)

            data = Profissional(
                **http_request.body,
                atuacao=atuacao_c,
                contato=contato,
                endereco=endereco
            )
            senha = data.senha
            data = data.to_json()

            data["senha"] = senha

            client.PROFISSIONAL.insert_one(data)

            data.pop("senha")

            response = HttpResponse(200, {"Success": True, "Data": data})
        except:
            http_error = HttpErrors.error_422()
            response = HttpResponse(
                status_code=http_error["status_code"],
                body=http_error["body"],
            )

    return response


def list_profissional(http_request: Type[HttpRequest]) -> HttpResponse:

    try:
        if http_request.query:
            _id = http_request.query["_id"]
            data = client.PROFISSIONAL.find_one({"_id": _id})
            data = [data]
        else:
            data = client.PROFISSIONAL.find()
            data = list(data)

        dataList = []

        for i in data:
            i = dict(i)

            endereco = Endereco(**i["endereco"])
            contato = Contato(**i["contato"])
            atuacao_l = []

            for it in list(i["atuacao"]):
                atuacao_l.append(Atuacao(it["descricao"], it["_id"]))

            _id = ObjectId(i["_id"])

            i.pop("_id")
            i.pop("endereco")
            i.pop("contato")
            i.pop("atuacao")
            i.pop("senha")

            dt = Profissional(
                **i, contato=contato, endereco=endereco, atuacao=atuacao_l, _id=_id
            )
            dt = dt.to_json()
            dataList.append(dt)

        response = HttpResponse(200, {"Success": True, "Data": dataList})

    except Exception as e:
        print(e)
        http_error = HttpErrors.error_422()
        response = HttpResponse(
            status_code=http_error["status_code"],
            body=http_error["body"],
        )

    return response


def list_profissional_atuacao(http_request: Type[HttpRequest]) -> HttpResponse:
    try:
        dataList = []

        if http_request.query:
            _id = http_request.query["_id"]
            data = client.PROFISSIONAL.find_one({"_id": _id})

            for it in list(data["atuacao"]):
                dataList.append(Atuacao(it["descricao"], it["_id"]).to_json())

        response = HttpResponse(200, {"Success": True, "Data": dataList})

    except Exception as e:
        print(e)
        http_error = HttpErrors.error_422()
        response = HttpResponse(
            status_code=http_error["status_code"],
            body=http_error["body"],
        )

    return response


def list_profissional_feed(http_request: Type[HttpRequest]) -> HttpResponse:

    try:
        data = client.PROFISSIONAL.find()
        data = list(data)
        dataList = []

        for i in data:
            i = dict(i)

            endereco = Endereco(**i["endereco"])
            contato = Contato(**i["contato"])
            atuacao_l = []

            media = 0
            qtde = 1

            for it in list(i["atuacao"]):
                atuacao_l.append(Atuacao(it["descricao"], it["_id"]))

            _id = i["_id"]
            ava = client.AVALIACAO.find()
            ava = list(ava)

            for j in ava:
                j = dict(j)

                if j["profissional_id"] == _id:
                    qtde += 1
                    media += j["avaliacao"]

            media = media / (qtde - 1)

            _id = ObjectId(i["_id"])

            i.pop("_id")
            i.pop("endereco")
            i.pop("contato")
            i.pop("atuacao")
            i.pop("senha")

            dt = Profissional(
                **i, contato=contato, endereco=endereco, atuacao=atuacao_l, _id=_id
            )
            dt = dt.to_json()
            dt["nota"] = media
            dt["qtde"] = qtde
            dataList.append(dt)

        response = HttpResponse(200, {"Success": True, "Data": dataList})

    except Exception as e:
        print(e)
        http_error = HttpErrors.error_422()
        response = HttpResponse(
            status_code=http_error["status_code"],
            body=http_error["body"],
        )

    return response


def update_profissional(http_request: Type[HttpRequest]) -> HttpResponse:
    response = None

    if http_request.body:
        try:
            if http_request.query:
                _id = http_request.query["_id"]
                senha = None

                if http_request.query.get("senha"):
                    senha = encrypt_password(http_request.query["senha"])
                    client.CLIENTE.update_one({"_id": _id}, {"$set": {"senha": senha}})

                client.PROFISSIONAL.update_one(
                    {"_id": _id}, {"$set": http_request.body}
                )
                return HttpResponse(200, {"Success": True, "Data": http_request.body})

        except Exception:
            http_error = HttpErrors.error_422()
            response = HttpResponse(
                status_code=http_error["status_code"],
                body=http_error["body"],
            )

    http_error = HttpErrors.error_422()
    response = HttpResponse(
        status_code=http_error["status_code"],
        body=http_error["body"],
    )

    return response


def delete_profissional(http_request: Type[HttpRequest]) -> HttpResponse:
    response = None

    try:
        if http_request.query:
            _id = http_request.query["_id"]
            client.PROFISSIONAL.delete_one({"_id": _id})
            return HttpResponse(200, {"Success": True, "Data": http_request.body})

    except Exception:
        http_error = HttpErrors.error_422()
        response = HttpResponse(
            status_code=http_error["status_code"],
            body=http_error["body"],
        )

    http_error = HttpErrors.error_422()
    response = HttpResponse(
        status_code=http_error["status_code"],
        body=http_error["body"],
    )

    return response
