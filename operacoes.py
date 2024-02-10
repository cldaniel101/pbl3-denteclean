from entidades import *
from datetime import datetime

class Operacoes:
    def __init__(self, lista_pacientes: list, lista_sessoes: list, lista_consultas: list, fila_atendimento: list):
        """
        Inicializa a classe Operacoes com listas de pacientes, sessões, consultas e fila de atendimento.

        Args:
        lista_pacientes (list): Lista de pacientes
        lista_sessoes (list): Lista de sessões clínicas
        lista_consultas (list): Lista de consultas
        fila_atendimento (list): Fila de atendimento
        """
        self.pacientes = lista_pacientes
        self.sessoes = lista_sessoes
        self.consultas = lista_consultas
        self.fila_atendimento = fila_atendimento
        self.sessao_atual = None
        self.consulta_atual = None

        self.anotacoes_pacientes = {}

    def adicionar_sessao_clinica(self, id, data, horario, duracao, dados_opcionais=""):
        """
        Adiciona uma nova sessão clínica à lista de sessões.

        Args:
        id (str): Identificador da sessão
        data (str): Data da sessão
        horario (str): Horário da sessão
        duracao (str): Duração da sessão
        dados_opcionais (str, optional): Dados opcionais da sessão. Defaults to "".
        """
        sessao = Sessao(id, data, horario, duracao, dados_opcionais)
        self.sessoes.append(sessao)

    def obter_maior_id_sessao(self):
        """
        Obtém o maior ID entre as sessões existentes.

        Returns:
        int: Maior ID de sessão
        """
        if not self.sessoes:
            return 0
        else:
            return max(sessao.id for sessao in self.sessoes)

    def salvar_sessoes_json(self, filename):
        """
        Salva as sessões em um arquivo JSON.

        Args:
        filename (str): Nome do arquivo JSON
        """
        with open(filename, 'w') as f:
            sessoes_dict = [sessao.to_dict() for sessao in self.sessoes]
            json.dump(sessoes_dict, f)

    def carregar_sessoes_json(self, filename):
        """
        Carrega as sessões a partir de um arquivo JSON.

        Args:
        filename (str): Nome do arquivo JSON
        """
        with open(filename, 'r') as f:
            sessoes_dict = json.load(f)
            self.sessoes = [Sessao.from_dict(data) for data in sessoes_dict]

    def exibir_sessoes(self):
        """Exibe as sessões clínicas."""
        for s in self.sessoes:
            print("--------------------------")
            print(f"Id: {s.id}")
            print(f"Data: {s.data}")
            print(f"Horário: {s.horario}")
            print(f"Duração (h): {s.duracao}")
            if s.dados_opcionais != "":
                print(f"Dados Adicionais: {s.dados_opcionais}")
            print("--------------------------")

    def buscar_sessao_clinica(self, data, horario):
        """
        Busca uma sessão clínica a partir de uma data e horário.

        Args:
        data (str): Data da sessão
        horario (str): Horário da sessão
        """
        encontrada = False
        for s in self.sessoes:
            if s.data == data and s.horario == horario:
                encontrada = True
                print("\nSESSÃO LOCALIZADA: ")
                print("--------------------------")
                print(f"Id: {s.id}")
                print(f"Data: {s.data}")
                print(f"Horário: {s.horario}")
                print(f"Duração (h): {s.duracao}")
                if s.dados_opcionais != "":
                    print(f"Dados Adicionais: {s.dados_opcionais}")
                print("--------------------------")

        if not encontrada:
            print("Sessão não encontrada.")

    def iniciar_sessao_clinica_recepcao(self, data, horario, iniciada_pelo_dentista=False):
        # Encontrar uma sessão clínica existente para a data e horário fornecidos
        sessao_existente = next(
            (sessao for sessao in self.sessoes if sessao.data == data and sessao.horario == horario), None
        )

        if sessao_existente:
            # Verifica se a sessão já está em andamento
            data_hora_atual = datetime.now().strftime("%d-%m-%Y %H:%M")
            data_hora_sessao = f"{sessao_existente.data} {sessao_existente.horario}"

            if data_hora_sessao < data_hora_atual:
                print("A data ou hora da sessão já passaram. Não é possível iniciar essa sessão.")
                return
            else:
                self.sessao_atual = sessao_existente
                if iniciada_pelo_dentista:
                    print("Sessão clínica iniciada pelo dentista para atendimento.")
                else:
                    print("Sessão clínica iniciada pela recepção para atendimento.")
        else:
            print("Não há sessão clínica para a data e horário fornecidos.")

    def id_da_sessao_atual(self):
        return self.sessao_atual.id

    def salvar_pacientes_json(self, filename):
        with open(filename, 'w') as f:
            pacientes_dict = [paciente.to_dict() for paciente in self.pacientes]
            json.dump(pacientes_dict, f)

    def salvar_consultas_json(self, filename):
        with open(filename, 'w') as f:
            consultas_dict = [consulta.to_dict() for consulta in self.consultas]
            json.dump(consultas_dict, f)

    def carregar_pacientes_json(self, filename):
        with open(filename, 'r') as f:
            pacientes_dict = json.load(f)
            self.pacientes = [Paciente.from_dict(data) for data in pacientes_dict]

    def carregar_consultas_json(self, filename):
        with open(filename, 'r') as f:
            consultas_dict = json.load(f)
            self.consultas = [Consulta.from_dict(data) for data in consultas_dict]

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
        data_hora_atual = datetime.now().strftime("%d-%m-%Y %H:%M")
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

    def confirmar_paciente_marcado_sessao_atual(self, rg_paciente, id_sessao):
        # Verifica se o paciente está cadastrado
        paciente = next((p for p in self.pacientes if p.rg == rg_paciente), None)

        if not paciente:
            print("Paciente não encontrado. Cadastre o paciente antes de confirmar a presença na sessão.")
            return

        # Verifica se o paciente está marcado para a sessão atual
        consulta = next(
            (consulta for consulta in self.consultas if consulta.sessao.id == id_sessao and consulta.paciente.rg == rg_paciente),
            None
        )

        if consulta:
            print(f"O paciente {paciente.nome} está marcado para a sessão de {consulta.sessao.data} às {consulta.sessao.horario}.")
        else:
            print(f"O paciente {paciente.nome} não está marcado para esta sessão.")

    def colocar_paciente_na_fila_atendimento(self, rg_paciente, id_sessao):
        # Verifica se o paciente está cadastrado
        paciente = next((p for p in self.pacientes if p.rg == rg_paciente), None)

        if not paciente:
            print("Paciente não encontrado. Cadastre o paciente antes de colocá-lo na fila de atendimento.")
            return

        # Verifica se o paciente está marcado para a sessão atual
        consulta = next(
            (consulta for consulta in self.consultas if consulta.sessao.id == id_sessao and consulta.paciente.rg == rg_paciente),
            None
        )

        if not consulta:
            print(f"O paciente {paciente.nome} não está marcado para a sessão com ID {id_sessao}.")
            return

        # Adiciona o paciente à fila de atendimento
        self.fila_atendimento.append(consulta)

        print(f"O paciente {paciente.nome} foi adicionado à fila de atendimento da sessão de {consulta.sessao.data} às {consulta.sessao.horario}.")

    def listar_proximo_paciente_fila_atendimento(self):
        """
        Exibe informações sobre o próximo paciente na fila de atendimento.

        Verifica se a fila de atendimento está vazia e, se não estiver,
        extrai as informações do próximo paciente e sessão na fila e as imprime.
        """
        if not self.fila_atendimento:
            print("A fila de atendimento está vazia.")
            return

        proxima_consulta = self.fila_atendimento[0]
        paciente = proxima_consulta.paciente
        sessao = proxima_consulta.sessao

        print(f"Próximo paciente a ser atendido:")
        print(f"Paciente: {paciente.nome}")
        print(f"Sessão: {sessao.data} às {sessao.horario}")

    def atender_proximo_paciente_fila_atendimento(self):
        """
        Atende o próximo paciente na fila de atendimento.

        Verifica se a fila de atendimento está vazia e, se não estiver,
        remove o próximo paciente da fila, registra a consulta como atual
        e solicita uma anotação sobre a visita ao paciente.
        """
        if not self.fila_atendimento:
            print("A fila de atendimento está vazia.")
            return

        proxima_consulta = self.fila_atendimento.pop(0)
        paciente = proxima_consulta.paciente
        sessao = proxima_consulta.sessao
        self.consulta_atual = proxima_consulta

        print(f"Atendendo próximo paciente da fila de atendimento.")
        print(f"Paciente: {paciente.nome}")
        print(f"Sessão: {sessao.data} às {sessao.horario}")

        print("Antes de finalizar o atendimento, registre uma anotação sobre a visita: ")
        anotacao = input("> ")
        self.registrar_anotacao_de_visita(paciente.rg, anotacao)

    def ler_prontuario_completo_paciente_atual(self):
        """
        Exibe o prontuário completo do paciente atualmente sendo atendido.

        Verifica se há um paciente sendo atendido no momento e, se sim,
        exibe as informações completas do prontuário desse paciente.
        """
        if not self.consulta_atual:
            print("Nenhum paciente está atualmente sendo atendido.")
            return

        paciente = self.consulta_atual.paciente

        print(f"Prontuário completo do paciente {paciente.nome}:")
        print(f"Número de Identidade (RG): {paciente.rg}")
        print(f"Outros dados: {paciente.outros_dados}")
        print("Prontuários:")
        for s, p in paciente.prontuario.items():
            print(f"{s}: {p}")

    def registrar_anotacao_de_visita(self, rg_paciente, anotacao):
        """
        Registra uma anotação de visita do paciente.

        Verifica se o paciente já possui anotações registradas e, se não,
        cria uma nova entrada para o paciente no dicionário de anotações.
        """
        if rg_paciente not in self.anotacoes_pacientes:
            self.anotacoes_pacientes[rg_paciente] = [anotacao]
            print("Primeira anotação de visita registrada.")
        else:
            self.anotacoes_pacientes[rg_paciente].append(anotacao)
            print("Anotação de visita registrada.")

    def ler_primeira_anotacao_paciente_atual(self):
        """
        Exibe a primeira anotação de visita do paciente atualmente sendo atendido.

        Verifica se há um paciente sendo atendido no momento e, se sim,
        exibe a primeira anotação de visita registrada para esse paciente.
        """
        if not self.consulta_atual:
            print("Nenhum paciente está atualmente sendo atendido.")
            return

        paciente = self.consulta_atual.paciente
        rg_paciente = paciente.rg

        if rg_paciente not in self.anotacoes_pacientes or not self.anotacoes_pacientes[rg_paciente]:
            print("Nenhuma anotação registrada para a primeira visita deste paciente.")
        else:
            primeira_anotacao = self.anotacoes_pacientes[rg_paciente][0]
            print(f"Primeira anotação do paciente {paciente.nome} na primeira visita:")
            print(primeira_anotacao)

    def ler_ultima_anotacao_paciente_atual(self):
        """
        Exibe a última anotação de visita do paciente atualmente sendo atendido.

        Verifica se há um paciente sendo atendido no momento e, se sim,
        exibe a última anotação de visita registrada para esse paciente.
        """
        if not self.consulta_atual:
            print("Nenhum paciente está atualmente sendo atendido.")
            return

        paciente = self.consulta_atual.paciente
        rg_paciente = paciente.rg

        if rg_paciente not in self.anotacoes_pacientes or not self.anotacoes_pacientes[rg_paciente]:
            print("Nenhuma anotação registrada para a última visita deste paciente.")
        else:
            ultima_anotacao = self.anotacoes_pacientes[rg_paciente][-1]
            print(f"Última anotação do paciente {paciente.nome} na última visita:")
            print(ultima_anotacao)

    def anotar_prontuario_paciente_atual(self, prontuario):
        """
        Adiciona uma anotação ao prontuário do paciente atualmente sendo atendido.

        Verifica se há um paciente sendo atendido no momento e, se sim,
        registra uma anotação no prontuário do paciente com a data e horário da sessão atual.
        """
        if not self.consulta_atual:
            print("Nenhum paciente está atualmente sendo atendido.")
            return

        paciente = self.consulta_atual.paciente

        # Registra uma anotação no prontuário do paciente com a data e horário da sessão atual
        data_hora_sessao = self.sessao_atual
        print(self.sessao_atual)

        if data_hora_sessao not in paciente.prontuario:
            paciente.prontuario[data_hora_sessao] = [prontuario]
        else:
            paciente.prontuario[data_hora_sessao].append(prontuario)

        print(f"Prontuário registrado para o paciente {paciente.nome}.")

    def listar_consultas_sessao_clinica(self, id_sessao):
        """
        Lista as consultas realizadas em uma sessão clínica específica.

        Verifica se há consultas associadas à sessão clínica com o ID fornecido.
        Se houver, exibe as informações sobre cada consulta (paciente, data e horário).
        """
        consultas_sessao = [consulta for consulta in self.consultas if consulta.sessao.id == id_sessao]

        if not consultas_sessao:
            print(f"Nenhuma consulta realizada na sessão clínica com ID {id_sessao}.")
        else:
            print(f"Consultas realizadas na sessão clínica com ID {id_sessao}:")
            for consulta in consultas_sessao:
                print(f"Paciente: {consulta.paciente.nome}")
                print(f"Data: {consulta.sessao.data}")
                print(f"Horário: {consulta.sessao.horario}")
                print("--------------------------")
    