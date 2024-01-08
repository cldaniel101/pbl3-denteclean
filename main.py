from datetime import datetime
from time import sleep

from entidades import *
from operacoes import Operacoes

print("Seja bem-vindo(a) à Clínica DenteClean\n")

# print("""Quem está acessando? 
# Recepção [1]
# Dentista [2]      
# """)
# user = input(">>> ")
# while user != "1" and user != "2":
#     print("Digite uma opção válida.")
#     user = input(">>> ")
user = "1"

pacientes = [Paciente("123456789", "João Silva", "Dor nos dentes."), Paciente("987654321", "Maria Oliveira")]
sessoes = []
consultas = []
fila_atendimento = []
op = Operacoes(pacientes, sessoes, consultas, fila_atendimento)
contador_sessoes = 3

# Cenário exemplo:
op.adicionar_sessao_clinica("1", "2024-01-28", "14:00", 4, "")
op.adicionar_sessao_clinica("2", "2024-01-28", "18:00", 3, "")
op.marcar_horario_para_paciente("123456789", "1")
op.colocar_paciente_na_fila_atendimento("123456789", "1")  # Exemplo: João Silva na fila de atendimento
op.iniciar_sessao_clinica_recepcao("2023-12-28", "14:00")

continuar = True

while continuar:
    if user == "1":
        print("\nO que deseja fazer?")
        print("""
[1] Adicionar nova sessão clínica
[2] Listar sessões clínicas
[3] Buscar sessão clínica
[4] Iniciar sessão clínica
[5] Adicionar novo paciente
[6] Marcar horário para paciente
[7] Listar horários marcados do paciente
[0] Sair
""")
        action = input(">>> ")

        if action == "1":
            print("Adicionando Sessão Clínica:")
            id = str(contador_sessoes)
            data = input("Data ('dd/mm/aaaa') - ")
            horario = input("Horário ('hh:mm') - ")
            duracao = input("Duração (horas) - ")
            conf_dados_opcionais = input("Deseja acrescentar dados adicionais? [S/N]").lower()
            if conf_dados_opcionais == "s":
                dados_opcionais = input("Informações Adicionais - ")
            else:
                dados_opcionais = ""  
            op.adicionar_sessao_clinica(id, data, horario, duracao, dados_opcionais)
            contador_sessoes += 1
            print("Sessão adicionada com sucesso!")

        elif action == "2":
            print("\nSessões Clínicas:")
            op.exibir_sessoes()
                
        elif action == "3":
            print("\nBuscar sessão clínica:")
            data = input("Data da sessão: ")
            horario = input("Horário da sessão: ")
            op.buscar_sessao_clinica(data, horario)

        elif action == "4":
            print("\nIniciar sessão clínica:")
            data = input("Data da sessão: ")
            horario = input("Horário da sessão: ")
            iniciada_pelo_dentista = input("A sessão está sendo iniciada pelo dentista? [S/N]").lower()
            
            if iniciada_pelo_dentista == "s":
                op.iniciar_sessao_clinica_recepcao(data, horario, iniciada_pelo_dentista=True)
            else:
                op.iniciar_sessao_clinica_recepcao(data, horario)

        elif action == "5":
            print("\nAdicionar novo paciente:")
            rg = input("Número de Identidade (RG): ")
            nome = input("Nome do paciente: ")
            outros_dados = input("Outros dados pessoais (opcional): ")
            op.adicionar_novo_paciente(rg, nome, outros_dados)

        elif action == "6":
            print("\nMarcar horário para paciente:")
            rg_paciente = input("Número de Identidade (RG) do paciente: ")
            id_sessao = input("ID da sessão: ")
            op.marcar_horario_para_paciente(rg_paciente, id_sessao)

        elif action == "7":
            print("\nListar horários marcados do paciente:")
            rg_paciente = input("Número de Identidade (RG) do paciente: ")
            op.listar_horarios_marcados_paciente(rg_paciente)


                
        elif action == "0":
            continuar = False
            print("Saindo do programa.")

        else:
            print("Opção inválida. Tente novamente.")

        sleep(2)
        
    elif user == "2":
        pass
