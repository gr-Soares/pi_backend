from bson import ObjectId


class Atuacao:

    def __init__(self, descricao, _id = None) -> None:
        self.descricao = descricao
        self._id = _id


    def to_json(self):
        return {
            "_id": ObjectId(self._id).__str__(),
            "descricao": self.descricao
        }