from entidades import *
from datetime import datetime

class Operacoes:
    def __init__(self, lista_pacientes: list, lista_sessoes: list, lista_consultas: list):
        self.pacientes = lista_pacientes
        self.sessoes = lista_sessoes
        self.consultas = lista_consultas

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
            data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M")
            data_hora_sessao = f"{sessao_existente.data} {sessao_existente.horario}"

            if data_hora_sessao < data_hora_atual:
                print("A data ou hora da sessão já passaram. Não é possível iniciar essa sessão.")
                return
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

    def marcar_horario_para_paciente(self, rg_paciente, id_sessao):
        # Verifica se o paciente está cadastrado
        paciente = next((p for p in self.pacientes if p.rg == rg_paciente), None)

        if not paciente:
            print("Paciente não encontrado. Cadastre o paciente antes de marcar um horário.")
            return

        # Verifica se a sessão existe
        sessao = next((s for s in self.sessoes if s.id == id_sessao), None)

        if not sessao:
            print("Sessão não encontrada. Verifique o ID da sessão e tente novamente.")
            return

        # Verifica se a sessão já foi encerrada
        data_hora_atual = datetime.now().strftime("%Y-%m-%d %H:%M")
        data_hora_sessao = f"{sessao.data} {sessao.horario}"

        if data_hora_sessao < data_hora_atual:
            print("Esta sessão já foi encerrada ou já está em andamento. Marque horário para uma sessão posterior, com mais chances de ter vagas disponíveis.")
            return

        # Cria uma nova consulta e a adiciona à lista de consultas
        nova_consulta = Consulta(paciente, sessao)
        self.consultas.append(nova_consulta)

        print(f"Horário marcado para o paciente {paciente.nome} na sessão {id_sessao}.")

    def listar_horarios_marcados_paciente(self, rg_paciente):
        # Verifica se o paciente está cadastrado
        paciente = next((p for p in self.pacientes if p.rg == rg_paciente), None)

        if not paciente:
            print("Paciente não encontrado. Cadastre o paciente antes de listar os horários marcados.")
            return

        consultas_paciente = [consulta for consulta in self.consultas if consulta.paciente.rg == rg_paciente]

        if consultas_paciente:
            print(f"Horários marcados para o paciente {consultas_paciente[0].paciente.nome}:")
            for consulta in consultas_paciente:
                print(
                    f"{consulta.sessao.data} {consulta.sessao.horario} - Sessão {consulta.sessao.id} "
                    f"({consulta.sessao.duracao} horas)"
                )
        else:
            print(f"O paciente {paciente.nome} não possui horários marcados.")


