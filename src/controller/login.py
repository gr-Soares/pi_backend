from ..adapter.auth import Payload, check_encrypted_password, encode_token, encrypt_password
from src.database import client
from src.adapter import HttpRequest, HttpResponse, HttpErrors
from bson.objectid import ObjectId
from typing import Type


def login_control(http_request: Type[HttpRequest]) -> HttpResponse:
    response = None

    if http_request.body:
        try:
            senha = http_request.body["senha"]
            username = http_request.body["usuario"]

            type = http_request.body["tipo"]
            data = None
            token = None
            _id = None

            if type == "Profissional":
                data = client.PROFISSIONAL.find_one({"usuario": username})
            elif type == "Cliente":
                data = client.CLIENTE.find_one({"usuario": username})

            if data != None:
                data = dict(data)

                if check_encrypted_password(senha, data["senha"]):
                    _id =  ObjectId(data["_id"]).__str__()
                    payload = Payload(data["usuario"], ObjectId(data["_id"]).__str__())
                    token = encode_token(payload)

            response = HttpResponse(200, {"Success": True, "Token": token, "_id":_id})

            if token == None:
                http_error = HttpErrors.error_403()
                response = HttpResponse(
                    status_code=http_error["status_code"],
                    body=http_error["body"],
                )

        except Exception:
            http_error = HttpErrors.error_422()
            response = HttpResponse(
                status_code=http_error["status_code"],
                body=http_error["body"],
            )

    return response
