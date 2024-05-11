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

            http_request.body.pop("endereco")
            http_request.body.pop("contato")

            data = Profissional(**http_request.body, contato=contato, endereco=endereco)

            client.PROFISSIONAL.insert_one(data.to_json())

            response = HttpResponse(200, {"Success": True, "Data": data.to_json()})
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
            _id = ObjectId(i["_id"])

            i.pop("endereco")
            i.pop("contato")
            i.pop("_id")

            dt = Profissional(**i, contato=contato, endereco=endereco, _id=_id)
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


def update_profissional(http_request: Type[HttpRequest]) -> HttpResponse:
    response = None

    if http_request.body:
        try:
            if http_request.query:
                _id = http_request.query["_id"]
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
