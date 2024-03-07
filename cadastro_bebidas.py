import locale

# class CadastrarBebidas:
#
#     def __init__(self, qtd_pacote='', qtd_unidade=''):
#         self.nome =
#         self.tipo = str(input('Tipo de bebida (Alcoólica, Não Alcoólica): ')).strip().title()
#         self.qtd_pacote = None
#         self.qtd_unidade = None
#         self.valor_gasto = None
#         self.valor_vendas = None
#
#     def tratar_nome(self):
#         if self.nome.isalpha():
#             print('ok')
#         elif self.nome in string.punctuation:
#             print('Não pode ter caractere especial')
#         else:
#             print('Campo não pode ter numero')


# while True:
#     nome_bebida = input('Digite o nome da Bebida: ').strip().title()
#     if nome_bebida.isalpha() and not nome_bebida in '':
#         print('ok')
#         break
#     else:
#         print('Campo inão pode ficar vazio é não pode conter numéro!')




# print('Escolha uma das opções abaixo: ')
# print('[1] - Alcoólica\n'
#       '[2] - Não Alcoólica')
#
# while True:
#     try:
#         opcao = int(input('Escolha uma opção: '))
#         if opcao == 1:
#             tipo_bebida = 'Alcoólica'
#             break
#         elif opcao == 2:
#             tipo_bebida = 'Não Alcoólica'
#             break
#         else:
#             print('Opção invalida')
#     except ValueError:
#         print('Erro... Campo não pode conter letras é não pode ficar vazio')

# while True:
#     try:
#         qtd_caixa = int(input('Digite a quantidade de caixa: '))
#     except ValueError:
#         print('Erro... Campo não pode conter letras é não pode ficar vazio')
#     else:
#         break
#
# while True:
#     try:
#         qtd_unidade = int(input('Digite a quantidade da unidade de uma caixa: '))
#     except ValueError:
#         print('Erro... Campo não pode conter letras é não pode ficar vazio')
#     else:
#         break



# while True:
#     try:
#         valor_gasto = input('Valor total gasto: R$')
#         valor_gasto = valor_gasto.replace(',', '.')
#         valor_gasto = float(valor_gasto)
#     except ValueError:
#         print('Erro... Campo não pode conter letras é não pode ficar vazio')
#     else:
#         break

while True:
    try:
        valor_venda = input('Valor de venda da unidade: R$')
        valor_venda = valor_venda.replace(',', '.')
        valor_venda = float(valor_venda)
    except ValueError:
        print('Erro... Campo não pode conter letras é não pode ficar vazio')
    else:
        break


