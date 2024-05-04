from typing import List

from .endereco import Endereco
from .contato import Contato


from bson.objectid import ObjectId

class Profissional:

    def __init__(
        self,
        nome,
        nascimento,
        genero,
        endereco: Endereco = None,
        contato: Contato = None,
        atuacao: List = [],
        habilidades: List = [],
        foto=None,
        _id=None,
    ) -> None:
        self._id = _id
        self.nome = nome
        self.nascimento = nascimento
        self.genero = genero
        self.endereco = endereco
        self.contato = contato
        self.atuacao = atuacao
        self.habilidades = habilidades
        self.foto = foto

    def to_json(self):
        return {
            '_id': ObjectId(self._id).__str__(),
            "nome": self.nome,
            "nascimento": self.nascimento,
            "genero": self.genero,
            "endereco": self.endereco.to_json() if self.endereco else None,
            "contato": self.contato.to_json() if self.contato else None,
            "atuacao": self.atuacao,
            "habilidades": self.habilidades,
            "foto": self.foto,
        }
