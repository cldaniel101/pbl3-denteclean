from entidades import *

class Operacoes:
    def __init__(self, lista_pacientes: list, lista_sessoes: list):
        self.pacientes = lista_pacientes
        self.sessoes = lista_sessoes

    def adicionar_sessao_clinica(self, id, data, horario, duracao, dados_opcionais = ""):
        sessao = Sessao(id, data, horario, duracao, dados_opcionais)
        self.sessoes.append(sessao)

    def exibir_sessoes(self):
        for s in self.sessoes:
                print("--------------------------")
                print(f"Id: {s.id}")
                print(f"Data: {s.data}")
                print(f"Horário: {s.horario}")
                print(f"Duração: {s.duracao}")
                if s.dados_opcionais != "":
                    print(f"Dados Adicionais: {s.dados_opcionais}")
                print("--------------------------")

    def buscar_sessao_clinica(self, data, horario):
        for s in self.sessoes:
            if s.data == data and s.horario == horario:
                print(f"Id: {s.id}")
                print(f"Data: {s.data}")
                print(f"Horário: {s.horario}")
                print(f"Duração: {s.duracao}")
                if s.dados_opcionais != "":
                    print(f"Dados Adicionais: {s.dados_opcionais}")
            # else:
            #     print("Sessão não encontrada.")
            #     return
        