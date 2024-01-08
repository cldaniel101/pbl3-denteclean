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
contador_sessoes = 1

# Cenário exemplo:
op.adicionar_sessao_clinica(1, "2024-01-28", "14:00", 4, "")
op.adicionar_sessao_clinica(2, "2024-01-28", "18:00", 3, "")
op.marcar_horario_para_paciente("123456789", 1)
op.colocar_paciente_na_fila_atendimento("123456789", 1)  # Exemplo: João Silva na fila de atendimento
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
[0] Sair
""")
        action = input(">>> ")

        if action == "1":
            print("Adicionando Sessão Clínica:")
            id = contador_sessoes
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
                
        elif action == "0":
            continuar = False
            print("Saindo do programa.")

        else:
            print("Opção inválida. Tente novamente.")
