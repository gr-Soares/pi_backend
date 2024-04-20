from src.database import client
from src.models import Cliente, Endereco, Contato
from src.adapter import HttpRequest, HttpResponse, HttpErrors
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

            client.CLIENTE.insert_one(data.to_json())

            response = HttpResponse(200, {"Success": True, "Data": data.to_json()})
        except Exception:
            http_error = HttpErrors.error_422()
            response = HttpResponse(
                status_code=http_error["status_code"],
                body=http_error["body"],
            )

    return response

def list_cliente(http_request: Type[HttpRequest]) -> HttpResponse:

    try:
        data = client.CLIENTE.find({}, {'_id': False})
        data = list(data)

        response = HttpResponse(200, {"Success": True, "Data": data})

    except:
        http_error = HttpErrors.error_422()
        response = HttpResponse(
            status_code=http_error["status_code"],
            body=http_error["body"],
        )

    return response
