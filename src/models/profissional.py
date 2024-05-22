from typing import List

from ..adapter.auth import encrypt_password

from .endereco import Endereco
from .contato import Contato


from bson.objectid import ObjectId


class Profissional:

    def __init__(
        self,
        usuario,
        nome,
        nascimento,
        genero,
        bio = "",
        endereco: Endereco = None,
        contato: Contato = None,
        atuacao: List = [],
        foto=None,
        senha = "",
        ativo=False,
        _id=None,
    ) -> None:
        self._id = _id
        self.usuario = usuario
        self.senha = encrypt_password(senha)
        self.nome = nome
        self.nascimento = nascimento
        self.genero = genero
        self.bio = bio
        self.endereco = endereco
        self.contato = contato
        self.atuacao = atuacao
        self.foto = foto
        self.ativo = ativo

    def to_json(self):
        return {
            "_id": ObjectId(self._id).__str__(),
            "usuario": self.usuario,
            "senha": self.senha,
            "nome": self.nome,
            "bio": self.bio,
            "nascimento": self.nascimento,
            "genero": self.genero,
            "endereco": self.endereco.to_json() if self.endereco else None,
            "contato": self.contato.to_json() if self.contato else None,
            "atuacao": [at.to_json() if at else None for at in self.atuacao],
            "foto": self.foto,
            "ativo": self.ativo
        }
