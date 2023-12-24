from help_sistema.base import *

#Programa principal
arq = 'produtos.csv'
if not arquivo_exist(arq):
    criar_arquivo(arq)

cabecalho('VENDAS DE BEBIDAS')
cabecalho('CADASTRO DAS BEBIDAS')
produto = Produto()
while True:
    try:
        produto.name_produto()
        produto.quantidade_produto()
        produto.valor_produto()
        produto.cadastrando_produto(arq)
    except KeyboardInterrupt:
        print('\nVolte sempre')
        break
    else:
        linha()
        continuar = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
        if continuar in 'N':
            print('Vonte sempre!')
            break

'''
while True:
produto = str(input('Nome do produto: {coca, heniken, shoop_vinho} ->')).strip().upper()
if produto != 'COCA' and produto != 'HENIKEN' and produto != 'SHOPP_VINHO':
print('ERRO! Digite o nome que está entre parentes.')
else:
break
'''