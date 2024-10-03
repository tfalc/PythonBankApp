"""
Descrição
Você está gerando um relatório de vendas em Power BI e deseja identificar quais produtos foram mais vendidos
durante um dia específico. Os dados dos produtos vendidos são frequentemente armazenados em listas.
Sua tarefa é usar uma lista em Python para contar a frequência de cada produto e determinar o produto mais vendido,
que será usado para destacar produtos populares no relatório do Power BI.

Detalhamento:

Encontre o produto com a maior contagem:

Itere sobre o dicionário contagem, que contém a contagem de cada produto.

Compare a contagem atual com a contagem máxima armazenada em max_count.

Se a contagem atual for maior que max_count, atualize max_count e defina max_produto como o produto atual.

Converter a entrada em uma lista de strings, removendo espaços extras:

Use o método split(',') para dividir a string de entrada em uma lista de strings, separando pelo caractere vírgula.

Utilize uma list comprehension para remover espaços em branco extras ao redor de cada string, usando o método strip().

Entrada
Uma lista de strings onde cada string representa o nome de um produto vendido.

Saída
A string com o nome do produto mais vendido. Se houver empate, retorne qualquer um dos produtos mais vendidos.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas.
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

+------------------------------------------------------------------------+------------+
| Entrada                                                                | Saída      |
+------------------------------------------------------------------------+------------+
| Notebook, Mouse, Teclado, Mouse, Monitor, Mouse, Teclado               | Mouse      |
| Impressora, Teclado, Monitor, Monitor, Teclado, Impressora, Impressora | Impressora |
| Webcam, Webcam, Headset, Monitor, Headset, Headset                     | Headset    |
+------------------------------------------------------------------------+------------+
"""


def produto_mais_vendido(produtos):
    contagem = {}

    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1

    max_produto = None
    max_count = 0

    for produto, count in contagem.items():
    # TODO: Encontre o produto com a maior contagem:

        if count > max_count:
            max_count = count
            max_produto = produto

    return max_produto


def obter_entrada_produtos():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de strings, removendo espaços extras:
    produtos = list(map(str.strip, entrada.split(",")))

    return produtos


produtos = obter_entrada_produtos()
print(produto_mais_vendido(produtos))
