from ..adapter.auth import encrypt_password
from .endereco import Endereco
from .contato import Contato

from bson.objectid import ObjectId


class Cliente:

    def __init__(
        self,
        usuario,
        nome,
        nascimento,
        genero,
        endereco: Endereco = None,
        contato: Contato = None,
        senha = "",
        foto=None,
        ativo=False,
        _id=None,
    ) -> None:
        self._id = _id
        self.usuario = usuario
        self.senha = encrypt_password(senha)
        self.nome = nome
        self.nascimento = nascimento
        self.genero = genero
        self.endereco = endereco
        self.contato = contato
        self.foto = foto
        self.ativo = ativo

    def to_json(self):
        return {
            "_id": ObjectId(self._id).__str__(),
            "usuario": self.usuario,
            "senha": self.senha,
            "nome": self.nome,
            "nascimento": self.nascimento,
            "genero": self.genero,
            "endereco": self.endereco.to_json() if self.endereco else None,
            "contato": self.contato.to_json() if self.contato else None,
            "foto": self.foto,
            "ativo": self.ativo,
        }
