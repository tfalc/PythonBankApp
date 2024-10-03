from abc import ABC


class Transacao(ABC):
    @property
    def valor(self):
        pass

    @classmethod
    def registrar(self, conta):
        pass
