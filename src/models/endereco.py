class Endereco:

    def __init__(self, cep, estado, cidade, bairro=None, rua=None, numero=None) -> None:
        self.cep = cep
        self.estado = estado
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero

    def to_json(self):
        return {
            "cep": self.cep,
            "estado": self.estado,
            "cidade": self.cidade,
            "bairro": self.bairro,
            "rua": self.rua,
            "numero": self.numero,
        }
