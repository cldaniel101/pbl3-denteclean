from time import sleep
import re

from entidades import *
from operacoes import Operacoes

print("Seja bem-vindo(a) à Clínica DenteClean\n")

print("""Quem está acessando? 
Recepção [1]
Dentista [2]
""")
user = input(">>> ")
while user != "1" and user != "2":
    print("Digite uma opção válida.")
    user = input(">>> ")

pacientes, sessoes, consultas, fila_atendimento = [], [], [], []
op = Operacoes(pacientes, sessoes, consultas, fila_atendimento)

padrao_data = re.compile(r'^\d{2}-\d{2}-\d{4}$')
padrao_horario = re.compile(r'^([01]\d|2[0-3]):[0-5]\d$')

# Cenário exemplo:
# op.salvar_pacientes_json('pacientes.json')
# op.salvar_sessoes_json('sessoes.json')
op.marcar_horario_para_paciente("123456789", "1")
op.salvar_consultas_json('consultas.json')
op.iniciar_sessao_clinica_recepcao("28-09-2024", "14:00")
op.colocar_paciente_na_fila_atendimento("123456789", "1")

continuar = True

while continuar:
    op.carregar_sessoes_json('sessoes.json')
    op.carregar_pacientes_json('pacientes.json')
    op.carregar_consultas_json('consultas.json')
    contador_sessoes = int(op.obter_maior_id_sessao()) + 1

    if user == "1":
        print("\n\033[1;36;107mO que deseja fazer?\033[0m")
        print("""\033[36m
[1]  Adicionar nova sessão clínica
[2]  Listar sessões clínicas
[3]  Buscar sessão clínica
[4]  Iniciar sessão clínica
[5]  Adicionar novo paciente
[6]  Marcar horário para paciente
[7]  Listar horários marcados do paciente
[8]  Confirmar se paciente está marcado para sessão atual
[9]  Colocar paciente na fila de atendimento
[10] Listar próximo paciente da fila de atendimento
[11] Atender próximo paciente
[12] Listar consultas realizadas numa sessão clínica
[0]  Sair
[T]  Trocar para Dentista
\033[0m""")
        action = input(">>> ")
        print()

        if action == "1":
            print("Adicionando Sessão Clínica:")
            id = str(contador_sessoes)
            data = input("Data ('dd-mm-aaaa') - ")
            if not padrao_data.match(data):
                print(f'{data} não é uma data válida.')
            else:
                horario = input("Horário ('hh:mm') - ")
                if not padrao_horario.match(horario):
                    print(f'{horario} não é um horário válido.')
                else:
                    duracao = input("Duração (horas) - ")
                    if int(duracao) <= 0 or int(duracao) > 6:
                        print("A duração precisa ser maior do que 0 e menor 6 horas.")
                    else:
                        conf_dados_opcionais = input("Deseja acrescentar dados adicionais? [S/N]").lower()
                        if conf_dados_opcionais == "s":
                            dados_opcionais = input("Informações Adicionais - ")
                        else:
                            dados_opcionais = ""  
                        op.adicionar_sessao_clinica(id, data, horario, duracao, dados_opcionais)
                        op.salvar_sessoes_json('sessoes.json')
                        contador_sessoes += 1
                        print("\033[30;42mSessão adicionada com sucesso!\033[0m")

        elif action == "2":
            print("\033[1;37;43mSessões Clínicas:\033[0m")
            op.exibir_sessoes()
                
        elif action == "3":
            print("\033[1;37;43mBuscar sessão clínica:\033[0m")
            data = input("Data da sessão: ")
            horario = input("Horário da sessão: ")
            op.buscar_sessao_clinica(data, horario)

        elif action == "4":
            print("\033[1;37;43mIniciar sessão clínica:\033[0m")
            data = input("Data da sessão: ")
            horario = input("Horário da sessão: ")
            op.iniciar_sessao_clinica_recepcao(data, horario)

        elif action == "5":
            print("\033[1;37;43mAdicionar novo paciente:\033[0m")
            rg = input("Número de Identidade (RG): ")
            nome = input("Nome do paciente: ")
            outros_dados = input("Outros dados pessoais (opcional): ")
            op.adicionar_novo_paciente(rg, nome, outros_dados)
            op.salvar_pacientes_json('pacientes.json')

        elif action == "6":
            print("\033[1;37;43mMarcar horário para paciente:\033[0m")
            rg_paciente = input("Número de Identidade (RG) do paciente: ")
            id_sessao = input("ID da sessão: ")
            op.marcar_horario_para_paciente(rg_paciente, id_sessao)
            op.salvar_consultas_json('consultas.json')

        elif action == "7":
            print("\033[1;37;43mListar horários marcados do paciente:\033[0m")
            rg_paciente = input("Número de Identidade (RG) do paciente: ")
            op.listar_horarios_marcados_paciente(rg_paciente)

        elif action == "8":
            try:
                print("\033[1;37;43mConfirmar se paciente está marcado para sessão atual:\033[0m")
                print("DICA: Lembre-se de iniciar a sessão antes!")
                rg_paciente = input("Número de Identidade (RG) do paciente: ")
                op.confirmar_paciente_marcado_sessao_atual(rg_paciente, op.id_da_sessao_atual())
            except:
                print("\n\033[1;30;41mERRO! TENTE NOVAMENTE.\033[0m \nPossíveis soluções:\n1. Verifique se o RG do paciente está correto\n2. Inicie uma sessão antes de colocar pacientes na fila de atendimento.")

        elif action == "9":
            try:
                print("\033[1;37;43mColocar paciente na fila de atendimento:\033[0m")
                print("DICA: Lembre-se de iniciar a sessão antes de colocar pacientes na fila de atendimento.")
                rg_paciente = input("Número de Identidade (RG) do paciente: ")
                op.colocar_paciente_na_fila_atendimento(rg_paciente, op.id_da_sessao_atual())
            except:
                print("\n\033[1;30;41mERRO! TENTE NOVAMENTE.\033[0m \nPossíveis soluções:\n1. Verifique se o RG do paciente está correto\n2. Inicie uma sessão antes de colocar pacientes na fila de atendimento.")

        elif action == "10":
            print("\033[1;37;43mListar próximo paciente da fila de atendimento:\033[0m")
            op.listar_proximo_paciente_fila_atendimento()

        elif action == "11":
            if op.fila_atendimento:
                consulta = op.fila_atendimento[0]
                paciente = consulta.paciente
                rg = paciente.rg   
            op.atender_proximo_paciente_fila_atendimento()                

        elif action == "12":
            print("DICA: Se preciso, liste as sessões clínicas [2] para verificar seu Id.\n")
            id_sessao = input("Digite o ID da sessão clínica: ")
            op.listar_consultas_sessao_clinica(id_sessao)
                
        elif action == "0":
            continuar = False
            print("Saindo do programa.")
        
        elif action.upper() == "T":
            print("Trocando para DENTISTA.")
            user = "2"

        else:
            print("\033[1;30;41mOpção inválida. Tente novamente.\033[0m")

        sleep(2)
        
    elif user == "2":
        print("\n\033[1;36;107mO que deseja fazer?\033[0m")
        print("""\033[36m
[1] Buscar sessão clínica
[2] Iniciar sessão clínica
[3] Atender próximo paciente
[4] Ler prontuário completo do paciente atual
[5] Ler primeira anotação do paciente atual
[6] Ler última anotação do paciente atual
[7] Anotar prontuário do paciente atual
[0] Sair
[T] Trocar para Recepção
\033[0m""")
        action = input(">>> ")

        if action == "1":
            print("\n\033[1;37;43mBuscar sessão clínica:\033[0m")
            data = input("Data da sessão: ")
            horario = input("Horário da sessão: ")
            op.buscar_sessao_clinica(data, horario)

        elif action == "2":
            print("\n\033[1;37;43mIniciar sessão clínica:\033[0m")
            data = input("Data da sessão: ")
            horario = input("Horário da sessão: ")
            
            op.iniciar_sessao_clinica_recepcao(data, horario, True)

        elif action == "3":
            if op.fila_atendimento:
                consulta = op.fila_atendimento[0]
                paciente = consulta.paciente
                rg = paciente.rg   
            op.atender_proximo_paciente_fila_atendimento()

        elif action == "4":
            print("\nDICA 1: Atenda um paciente da fila de atendimento antes.")
            print("\nDICA 2: Anote o prontuário do paciente [7]. \n")
            op.ler_prontuario_completo_paciente_atual()

        elif action == "5":
            op.ler_primeira_anotacao_paciente_atual()

        elif action == "6":
            op.ler_ultima_anotacao_paciente_atual()

        elif action == "7":
            prontuario = input("Digite a anotação do prontuário: ")
            op.anotar_prontuario_paciente_atual(prontuario)
            op.salvar_pacientes_json('pacientes.json')

        elif action == "0":
            continuar = False
            print("Saindo do programa.")

        elif action.upper() == "T":
            print("Trocando para RECEPÇÃO.")
            user = "1"

        else:
            print("\033[1;30;41mOpção inválida. Tente novamente.\033[0m")

        sleep(2)
