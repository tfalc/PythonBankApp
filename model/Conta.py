from Historico import Historico


class Conta:
    def __init__(self, numero, cliente):
        self.__saldo = 0
        self.__numero = numero
        self.__agencia = "0001"
        self.__cliente = cliente
        self.__historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def numero(self):
        return self.__numero

    @property
    def agencia(self):
        return self.__agencia

    @property
    def cliente(self):
        return self.__cliente

    @property
    def historico(self):
        return self.__historico

    def sacar(self, valor):
        saldo = self.__saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\nFALHA PONTUAL! Seu saldo não é suficiente. Deposite mais dinheiro!")
        elif valor > 0:
            self.__saldo -= valor
            print("\nBOA! Dinheiro na conta!")
            return True
        else:
            print("\nFALHA GERAL! Impossível sacar {}. Digite um valor plausível!".format(valor))

        return False

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("\nBOA! Dinheiro na mão!")
        else:
            print("\nFALHA GERAL! Impossível depositar {}. Digite um valor plausível!".format(valor))
            return False

        return True