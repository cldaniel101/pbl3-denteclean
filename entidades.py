import json

class Paciente:
    """
    Classe para representar um paciente.

    Contém informações básicas sobre o paciente e seu prontuário.
    """
    def __init__(self, rg, nome, outros_dados=""):
        self.rg = rg
        self.nome = nome
        self.outros_dados = outros_dados
        self.prontuario = {}

    def to_dict(self):
        return {
            'rg': self.rg,
            'nome': self.nome,
            'outros_dados': self.outros_dados,
            'prontuario': self.prontuario
        }

    @classmethod
    def from_dict(cls, data):
        paciente = cls(data['rg'], data['nome'], data['outros_dados'])
        paciente.prontuario = data['prontuario']
        return paciente

class Sessao:
    """
    Classe para representar uma sessão clínica.

    Contém informações sobre a data, horário, duração e dados opcionais da sessão.
    """
    def __init__(self, id, data, horario, duracao, dados_opcionais):
        self.id = id
        self.data = data
        self.horario = horario
        self.duracao = duracao
        self.dados_opcionais = dados_opcionais

    def to_dict(self):
        return {
            'id': self.id,
            'data': self.data,
            'horario': self.horario,
            'duracao': self.duracao,
            'dados_opcionais': self.dados_opcionais
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], data['data'], data['horario'], data['duracao'], data['dados_opcionais'])

    def __str__(self) -> str:
        return f"{self.data} às {self.horario}"
    
class Consulta:
    """
    Classe para representar uma consulta.

    Contém informações sobre o paciente associado e a sessão em que a consulta ocorreu.
    """
    def __init__(self, paciente, sessao):
        self.paciente = paciente
        self.sessao = sessao

    def to_dict(self):
        return {
            'paciente': self.paciente.to_dict(),
            'sessao': self.sessao.to_dict()
        }

    @classmethod
    def from_dict(cls, data):
        paciente = Paciente.from_dict(data['paciente'])
        sessao = Sessao.from_dict(data['sessao'])
        return cls(paciente, sessao)
