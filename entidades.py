class Paciente:
    def __init__(self, rg):
        self.rg = rg

class Sessao:
    def __init__(self, id, data, horario, duracao, dados_opcionais):
        self.id = id
        self.data = data
        self.horario = horario
        self.duracao = duracao
        self.dados_opcionais = dados_opcionais

    def __str__(self) -> str:
        return self.data