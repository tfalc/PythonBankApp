import Cliente


class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super.__init__(endereco)
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento
