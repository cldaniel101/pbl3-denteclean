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

pacientes = []
sessoes = []
operacao = Operacoes(pacientes, sessoes)
contador_sessoes = 1

operacao.adicionar_sessao_clinica(1, "25/12/2023", "14:00", "3")
operacao.adicionar_sessao_clinica(2, "10/10/2023", "16:00", "1", "Sessão Cancelada")

continuar = True

while continuar:
    if user == "1":
        print("\nO que deseja fazer?")
        print("""
[1] Adicionar nova sessão clínica
[2] Listar sessões clínicas
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
            operacao.adicionar_sessao_clinica(id, data, horario, duracao, dados_opcionais)
            contador_sessoes += 1
            print("Sessão adicionada com sucesso!")

        elif action == "2":
            print("\nSessões Clínicas:")
            operacao.exibir_sessoes()
                
        elif action == "3":
            print("\nBuscar sessão clínica:")
            data = input("Data da sessão: ")
            horario = input("Horário da sessão: ")
            operacao.buscar_sessao_clinica(data, horario)
