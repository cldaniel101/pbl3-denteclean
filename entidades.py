class Paciente:
    def __init__(self, rg, nome, outros_dados=""):
        self.rg = rg
        self.nome = nome
        self.outros_dados = outros_dados

class Sessao:
    def __init__(self, id, data, horario, duracao, dados_opcionais):
        self.id = id
        self.data = data
        self.horario = horario
        self.duracao = duracao
        self.dados_opcionais = dados_opcionais

    def __str__(self) -> str:
        return self.data
    
class Consulta:
    def __init__(self, paciente, sessao):
        self.paciente = paciente
        self.sessao = sessao