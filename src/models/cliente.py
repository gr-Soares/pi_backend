from .endereco import Endereco
from .contato import Contato
 

class Cliente:
    
    def __init__(self, nome, nascimento, genero, endereco:Endereco=None, contato:Contato=None, foto=None) -> None:
        self.nome = nome
        self.nascimento = nascimento
        self.genero = genero
        self.endereco = endereco
        self.contato = contato
        self.foto = foto

    def to_json(self):
        return {
            'nome': self.nome,
            'nascimento': self.nascimento,
            'genero': self.genero,
            'endereco': self.endereco.to_json() if self.endereco else None,
            'contato': self.contato.to_json() if self.contato else None,
            'foto': self.foto
        }