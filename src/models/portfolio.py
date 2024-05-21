
from bson import ObjectId


class Portfolio:
    def __init__(self, profissional_id, descricao, titulo, imagens, capa, _id=None) -> None:
        self._id = _id
        self.profissional_id = profissional_id
        self.titulo = titulo
        self.descricao = descricao
        self.imagens = imagens
        self.capa = capa

    def to_json(self):
        return {
            "_id": ObjectId(self._id).__str__(),
            "profissional_id":self.profissional_id,
            "titulo": self.titulo,
            "descricao":self.descricao,
            "imagens":self.imagens,
            "capa":self.capa
        }