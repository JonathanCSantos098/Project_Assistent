print('''Olá, tudo bem?
Sou seu novo Assistente e estou aqui para te ajudar no que precisar!
Em que posso te ajudar nesse momento?''')
print("[1] - Cadastrar Lembrete\n[2] - Verificar Lembretes Salvos\n[3] - Editar Lembretes\n[4] - Tutorial\n[5] - Configurações\n[6] - Central de Ajuda")
opção=int(input("DIGITE A OPÇÃO DESEJADA: "))
if (opção==1):
    print("que tipo de atividade deseja Cadastrar?")
    print("[1] - atividade de casa\n[2] - atividade do trabalho\n[3] - atividade de laser\n[4] - atividade extra")
    atividade=int(input())
    if (atividade==1):
        print("Qual a hora e minutos que deseja realizar a atividade?")
        hora=int(input())
        minutos=int(input())
        print("O que deseja fazer nesse horário?")
        atv=str(input())
        print("Voce irá {} as {}:{}".format(atv,hora,minutos))
        print("deseja confirmar? [1] - Sim [2] - Não")
        confirmacao=int(input())
        if (confirmacao==1):
            print("dados salvos com sucesso")
            
        else:
            print("seus dados não foram salvos!")
    



