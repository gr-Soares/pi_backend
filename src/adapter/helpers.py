from typing import Dict

class HttpRequest:
    def __init__(
        self,
        header: Dict = None,
        body: Dict = None,
        query: Dict = None,
        token: Dict = None,
        files: Dict = None,
    ) -> None:
        self.body = body
        self.header = header
        self.query = query
        self.files = files
        self.token = token


class HttpResponse:
    def __init__(self, status_code: int, body: Dict = None) -> None:
        self.body = body
        self.status_code = status_code

class HttpErrors:
    """Class to define errors in http"""

    @staticmethod
    def error_400():
        """HTTP 400"""

        return {"status_code": 400, "body": {"error": "Bad Request"}}

    @staticmethod
    def error_401():
        """HTTP 401"""

        return {"status_code": 401, "body": {"error": "Unauthorized"}}

    @staticmethod
    def error_403():
        """HTTP 403"""

        return {"status_code": 403, "body": {"error": "Forbidden"}}

    @staticmethod
    def error_409():
        """HTTP 409"""

        return {"status_code": 409, "body": {"error": "Conflict"}}

    @staticmethod
    def error_422():
        """HTTP 422"""

        return {"status_code": 422, "body": {"error": "Unprocessable Entity"}}

    @staticmethod
    def error_500():
        """HTTP 500"""

        return {"status_code": 500, "body": {"error": "Internal Server Error"}}