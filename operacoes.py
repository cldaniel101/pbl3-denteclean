from entidades import *

class Operacoes:
    def __init__(self, lista_pacientes: list, lista_sessoes: list):
        self.pacientes = lista_pacientes
        self.sessoes = lista_sessoes

    def adicionar_sessao_clinica(self, id, data, horario, duracao, dados_opcionais=""):
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
        encontrada = False
        for s in self.sessoes:
            if s.data == data and s.horario == horario:
                encontrada = True
                print("--------------------------")
                print(f"Id: {s.id}")
                print(f"Data: {s.data}")
                print(f"Horário: {s.horario}")
                print(f"Duração: {s.duracao}")
                if s.dados_opcionais != "":
                    print(f"Dados Adicionais: {s.dados_opcionais}")
                print("--------------------------")

        if not encontrada:
            print("Sessão não encontrada.")

    def iniciar_sessao_clinica_recepcao(self, data, horario):
        # Encontrar uma sessão clínica existente para a data e horário fornecidos
        sessao_existente = next(
            (sessao for sessao in self.sessoes if sessao.data == data and sessao.horario == horario), None
        )

        if sessao_existente:
            # Verifica se a sessão já está em andamento
            if sessao_existente.horario_fim:
                print("A sessão clínica já foi encerrada para este horário.")
            else:
                print("Sessão clínica iniciada pela recepção para atendimento.")
        else:
            print("Não há sessão clínica para a data e horário fornecidos.")

    def adicionar_novo_paciente(self, rg, nome, outros_dados=""):
        # Verifica se o paciente já está cadastrado
        paciente_existente = next((paciente for paciente in self.pacientes if paciente.rg == rg), None)

        if paciente_existente:
            print("Paciente já cadastrado.")
        else:
            # Cria um novo paciente e o adiciona à lista de pacientes
            novo_paciente = Paciente(rg, nome, outros_dados)
            self.pacientes.append(novo_paciente)
            print("Novo paciente cadastrado com sucesso.")

    