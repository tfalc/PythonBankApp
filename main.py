import textwrap


def menu():
    menu = """

     __-| Banco do Falcão |-__

    Selecione a opção desejada:
    [D]\tDepositar
    [S]\tSacar
    [E]\tExtrato
    [C]\tCriar conta
    [L]\tListar contas
    [U]\tCriar usuário
    [Q]\tSair

    #########################
    ::>_"""

    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito: R${valor:.2f}\n"
        print("\nDeposito realizado com sucesso!\nSeu novo saldo é de R${0:.2f}.".format(saldo))
    else:
        print("ERRO FATAL! Impossível depositar R${0}. Valor inválido.".format(valor))
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saque
    if excedeu_saldo:
        print("\nSaldo insuficiente. Impossível realizar saque de {0}.".format(valor))
    elif excedeu_limite:
        print("\nLimite de saque excedido. Impossível realizar saque de {0}.".format(valor))
    elif excedeu_saques:
        print("\nQuantidade de saques excedida. Tente novamente outro dia.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!\nSeu novo saldo é de R${0:.2f}.".format(saldo))
    else:
        print("ERRO FATAL! Impossível sacar R${0}. Valor inválido.".format(valor))
    return saldo, extrato


def exibir_extrato(saldo, limite_saque, saques_restantes, /, *, extrato):
    print(f"Seja bem-vindo(a) ao Banco do Falcão. \n\tO saldo inicial é de R${saldo:.2f}")
    print(f"#################### Extrato ################")
    print(f"Saldo atual: {'.' * (45 - 13 - len(f'R${saldo:.2f}'))}R${saldo:.2f}")
    print(f"Limite de saque: {'.' * (45 - 17 - len(f'R${limite_saque:.2f}'))}R${limite_saque:.2f}")
    print(f"Quantidade de saques restantes: {'.' * (45 - 32 - len(str(saques_restantes)))}{saques_restantes}")
    print(f"#############################################")


def criar_usuario(usuarios):
    cpf = input("Digite seu CPF(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("ERRO FATAL! Usuario com cpf \"{}\" ja existe.".format(cpf))

    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    logradouro = input("Informe o seu logradouro: ")
    numero_casa = input("Numero da sua casa: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado(sigla): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": logradouro + ", " + numero_casa + " - " + bairro + " - " + cidade + "/" + estado
    })

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, num_conta, usuarios):
    cpf = input("Digite seu CPF(somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("ERRO FATAL! Usurário com cpf \"{}\" nao encontrado.".format(cpf))
        return None

    print("Conta criada com sucesso!")
    return {"agencia": agencia, "numero": num_conta, "usuario": usuario}


def listar_conta(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero']}
        Titular:\t{conta['usuario']['nome']}
        """
        print("#" * 45)
        print(textwrap.dedent(linha))


def menu_principal(opcao, saldo, limite, limite_saques):
    switch = {
        'D': lambda: depositar(saldo),
        'S': lambda: sacar(saldo, limite, limite_saques),
        'E': lambda: extrato(saldo, limite, limite_saques),
        'Q': lambda: False
    }

    func = switch.get(opcao, lambda: print("Opção inválida. Tente novamente."))
    return func()


def main():
    LIMITE_SAQUES = 5
    AGENCIA = "0001"

    saldo = 0
    limite = 8000
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if not opcao or opcao.upper() not in "DSECLUQ":
            print("Opção inválida. Tente novamente.")
            continue

        if opcao in ["d", "D"]:
            valor = float(input("Digite o valor a ser depositado: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao in ["s", "S"]:
            valor = float(input("Digite o valor a ser sacado: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saque=LIMITE_SAQUES
            )
        elif opcao in ["e", "E"]:
            exibir_extrato(saldo, limite, LIMITE_SAQUES, extrato=extrato)

        elif opcao in ["c", "C"]:
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao in ["l", "L"]:
            listar_conta(contas)

        elif opcao in ["u", "U"]:
            criar_usuario(usuarios)

        elif opcao in ["q", "Q"]:
            break


if __name__ == "__main__":
    main()
