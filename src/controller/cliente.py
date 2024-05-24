from ..adapter.auth import encrypt_password
from src.database import client
from src.models import Cliente, Endereco, Contato
from src.adapter import HttpRequest, HttpResponse, HttpErrors
from bson.objectid import ObjectId
from typing import Type


def create_cliente(http_request: Type[HttpRequest]) -> HttpResponse:

    response = None

    if http_request.body:
        try:
            endereco = Endereco(**http_request.body["endereco"])
            contato = Contato(**http_request.body["contato"])

            http_request.body.pop("endereco")
            http_request.body.pop("contato")

            data = Cliente(**http_request.body, contato=contato, endereco=endereco)
            senha = data.senha
            data = data.to_json()

            data["senha"] = senha

            client.CLIENTE.insert_one(data)

            data.pop("senha")

            response = HttpResponse(200, {"Success": True, "Data": data})
        except Exception:
            http_error = HttpErrors.error_422()
            response = HttpResponse(
                status_code=http_error["status_code"],
                body=http_error["body"],
            )

    return response


def list_cliente(http_request: Type[HttpRequest]) -> HttpResponse:
    response = None
    data = None
    try:
        if http_request.query:
            _id = http_request.query["_id"]
            data = client.CLIENTE.find_one({"_id": _id})
            data = [data]
        else:
            data = client.CLIENTE.find()
            data = list(data)

        dataList = []

        for i in data:
            i = dict(i)

            endereco = Endereco(**i["endereco"])
            contato = Contato(**i["contato"])
            _id = ObjectId(i["_id"])

            i.pop("endereco")
            i.pop("contato")
            i.pop("_id")
            i.pop("senha")

            dt = Cliente(**i, contato=contato, endereco=endereco, _id=_id)
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


def update_cliente(http_request: Type[HttpRequest]) -> HttpResponse:
    response = None

    if http_request.body:
        try:
            if http_request.query:
                _id = http_request.query["_id"]
                senha = None
                
                if(http_request.query.get("senha")):
                    senha = encrypt_password(http_request.query["senha"])
                    client.CLIENTE.update_one({"_id": _id}, {"$set": {"senha":senha}})

                client.CLIENTE.update_one({"_id": _id}, {"$set": http_request.body})
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


def delete_cliente(http_request: Type[HttpRequest]) -> HttpResponse:
    response = None

    try:
        if http_request.query:
            _id = http_request.query["_id"]
            client.CLIENTE.delete_one({"_id": _id})
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
