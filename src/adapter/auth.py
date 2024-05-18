import jwt
from decouple import config
from passlib.context import CryptContext

pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000
)

def encrypt_password(password):
    return pwd_context.encrypt(password)


def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)

class Payload:

    def __init__(self, username, _id) -> None:
        self.username = username
        self._id = _id

    def toJson(self):
        return {"username": self.username, "id": self.username}


def encode_token(payload:Payload) -> str:
    salt = config("SECRET_WEB", default="AutonomiaWeb", cast=str)
    return jwt.encode(payload.toJson(), salt, algorithm="HS256")


def decode_token(token) -> bool:
    salt = config("SECRET_WEB", default="AutonomiaWeb", cast=str)
    try:
        decode = jwt.decode(token, salt, algorithms="HS256")
        return decode
    except:
        return None
