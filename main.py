menu = """

 __-| Banco do Falcão |-__
 
Selecione a opção abaixo:
[D] Depositar
[S] Sacar
[E] Extrato
[X] Sair

#########################
::>_"""

saldo = 0
limite = 3000
limite_saques = 5

print("Seja bem-vindo(a) ao seu banco. O saldo inicial é de R$ 0.00")

while True:

    opcao = input(menu).upper()

    if opcao == "D":
        valor = float(input("Digite o valor a ser depositado somente com números: "))
        if valor > 0:
            saldo += valor
            print("Deposito realizado com sucesso! Seu novo saldo é de R$ {0:.2f}.".format(saldo))
        else:
            print("ERRO FATAL! Não é possível depositar valores negativos ou zero!.")

    elif opcao == "S":
        saque = float(input("Digite o valor que deseja sacar: "))
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = limite_saques <= 0
        if excedeu_saldo:
            print("ERRO FATAL! Impossível sacar R${0}. Saldo insuficiente. Você tem R$ {1}.".format(saque, saldo))
        elif excedeu_limite:
            print("ERRO FATAL! Limite de saques excedido. Seu limite de saque é de R${0}.".format(limite))
        elif excedeu_saques:
            print("### \nERRO FATAL! Número de saques excedido. Você pode fazer até {0} saques.".format(limite_saques))
        else:
            saldo -= saque
            print(f"Saque de R$ {saque:.2f} realizado com sucesso!\nSeu saldo agora é de R$ {saldo:.2f}.\n")
            limite_saques -= 1

    elif opcao == "E":
        # Inicialização de texto de extrato
        texto_saldo_atual = "Saldo atual: "
        texto_limite_saque = "Limite de saque: "
        texto_saque_restante = "Quantidade de saques restantes: "
        comprimento_texto_saldo = len(texto_saldo_atual)
        comprimento_texto_limite = len(texto_limite_saque)
        comprimento_saque_restante = len(texto_saque_restante)

        # Cálculo de pontos para tabulação
        num_pontos = 45 - comprimento_texto_saldo - len(f"R${saldo:.2f}")
        num_pontos_limite = 45 - comprimento_texto_limite - len(f"R${limite:.2f}")
        num_pontos_saque_restante = 45 - comprimento_saque_restante - 1

        # String editada com o recuo e tabulação
        recuo = '.' * num_pontos
        recuo_limite = '.' * num_pontos_limite
        recuo_saque_restante = '.' * num_pontos_saque_restante

        # Texto final com a formatação
        print(f"""
        #################### Extrato ################
        {texto_saldo_atual}{recuo}R${saldo:.2f}
        {texto_limite_saque}{recuo_limite}R${limite:.2f}
        {texto_saque_restante}{recuo_saque_restante}{limite_saques}
        #############################################
        """)

    elif opcao == "X":
        break

    else:
        print("Opcão inválida, tente novamente")
