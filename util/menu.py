import textwrap


class menu:

    def menu(self):
        menuOpcoes = """
    
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

        return input(textwrap.dedent(menuOpcoes))
