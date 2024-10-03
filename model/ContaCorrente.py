from PythonBankApp.model import Saque
from Conta import Conta


class ContaCorrente:
    def __init__(self, numero, cliente, limite=3000, limite_saques=5):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.agencia = Conta.agencia
        self.numero = Conta.numero
        self.cliente = Conta.cliente
        self.historico = Conta.historico
        self.saldo = Conta.saldo

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__])

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques
        excedeu_saldo = self.saldo < valor

        if excedeu_limite:
            print(f"\nPARE! Limite de saque excedido. Impossível realizar saque de {valor}.")
        elif excedeu_saques:
            print(f"\nOPA! Vai com calma... Quantidade de saques excedida. Tente novamente outro dia.")
        elif excedeu_saldo:
            print(f"\nFALHA GERAL! Saldo insuficiente. Impossível realizar saque de {valor}.")
        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""
        Agencia:\t{self.agencia}
        C/C:\t\t{self.numero}
        Titular:\t{self.cliente.nome}
        """

    @property
    def transacoes(self):
        return self._transacoes