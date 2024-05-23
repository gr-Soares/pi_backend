
from bson import ObjectId


class Avaliacao:

    def __init__(self, avaliacao, profissional_id, _id=None) -> None:
        self._id = _id
        self.avaliacao = avaliacao
        self.profissional_id = profissional_id

    def to_json(self):
        return {
            "_id": ObjectId(self._id).__str__(),
            "profissional_id": self.profissional_id,
            "avaliacao": self.avaliacao
        }