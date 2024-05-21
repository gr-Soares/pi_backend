from src.database import client
from src.models import Portfolio
from src.adapter import HttpRequest, HttpResponse, HttpErrors
from bson.objectid import ObjectId
from typing import Type


def create_portfolio(http_request: Type[HttpRequest]) -> HttpResponse:

    response = None

    if http_request.body:
        try:

            data = Portfolio(**http_request.body)

            client.PORTFOLIO.insert_one(data.to_json())

            data.senha = ""

            response = HttpResponse(200, {"Success": True, "Data": data.to_json()})
        except Exception:
            http_error = HttpErrors.error_422()
            response = HttpResponse(
                status_code=http_error["status_code"],
                body=http_error["body"],
            )

    return response


def list_portfolio(http_request: Type[HttpRequest]) -> HttpResponse:
    response = None
    data = None
    try:
        if http_request.query:
            _id = http_request.query["_id"]
            data = client.PORTFOLIO.find_one({"_id": _id})
            data = [data]
        else:
            data = client.PORTFOLIO.find()
            data = list(data)

        dataList = []

        for i in data:
            i = dict(i)

            _id = ObjectId(i["_id"])

            i.pop("_id")

            dt = Portfolio(**i, _id=_id)
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


def update_portfolio(http_request: Type[HttpRequest]) -> HttpResponse:
    response = None

    if http_request.body:
        try:
            if http_request.query:
                _id = http_request.query["_id"]

                client.PORTFOLIO.update_one({"_id": _id}, {"$set": http_request.body})
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


def delete_portfolio(http_request: Type[HttpRequest]) -> HttpResponse:
    response = None

    try:
        if http_request.query:
            _id = http_request.query["_id"]
            client.PORTFOLIO.delete_one({"_id": _id})
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
