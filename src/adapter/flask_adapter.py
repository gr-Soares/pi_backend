from typing import Type, Any

from .auth import decode_token
from .helpers import HttpRequest, HttpResponse, HttpErrors

import json


def flask_adapter_no_token(request: Any, route) -> Any:
    try:
        query_string_params = request.args.to_dict()

    except:
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    token = None

    try:
        response = None
        http_request = None

        if request.method == "GET" or request.method == "DELETE":
            http_request = HttpRequest(
                header=request.headers, query=query_string_params, token=token
            )
        elif request.mimetype == "application/json":
            http_request = HttpRequest(
                header=request.headers,
                body=request.json,
                query=query_string_params,
                token=token,
            )
        elif request.mimetype == "multipart/form-data":
            files = []
            files_keys = request.files.keys()
            for key in files_keys:
                files.append(request.files.getlist(key)[0])
            http_request = HttpRequest(
                header=request.headers,
                body=json.loads(request.form["desc"]),
                files=files,
                query=query_string_params,
                token=token,
            )
    except Exception:
        http_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    try:
        if http_request:
            response = route(http_request=http_request)
        else:
            print("No request")
            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

    except:
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    return response


def flask_adapter(request: Any, route) -> Any:
    try:
        query_string_params = request.args.to_dict()

    except:
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    token = None

    try:
        token_str = ""
        if request.headers.get("token"):
            token_str = request.headers.get("token")
        elif request.headers.get("Token"):
            token_str = request.headers.get("Token")
        else:
            http_error = HttpErrors.error_401()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )
        token = decode_token(token_str)
    except:
        http_error = HttpErrors.error_401()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    try:
        response = None
        http_request = None

        if request.method == "GET" or request.method == "DELETE":
            http_request = HttpRequest(
                header=request.headers, query=query_string_params, token=token
            )
        elif request.mimetype == "application/json":
            http_request = HttpRequest(
                header=request.headers,
                body=request.json,
                query=query_string_params,
                token=token,
            )
        elif request.mimetype == "multipart/form-data":
            files = []
            files_keys = request.files.keys()
            for key in files_keys:
                files.append(request.files.getlist(key)[0])
            http_request = HttpRequest(
                header=request.headers,
                body=json.loads(request.form["desc"]),
                files=files,
                query=query_string_params,
                token=token,
            )
    except Exception:
        http_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    try:
        if http_request:
            if token != None:
                response = route(http_request=http_request)
            else:
                http_error = HttpErrors.error_403()
                return HttpResponse(
                    status_code=http_error["status_code"], body=http_error["body"]
                )
        else:
            print("No request")
            http_error = HttpErrors.error_422()
            return HttpResponse(
                status_code=http_error["status_code"], body=http_error["body"]
            )

    except:
        http_error = HttpErrors.error_500()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"]
        )

    return response
