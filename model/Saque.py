import Transacao

class Saque(Transacao):
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.__valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)