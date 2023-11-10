from help_sistema.base import *

#Programa principal
arq = 'produtos'
if not arquivoExist(arq):
    criarArquivo(arq)

cabecalho('VENDAS DE BEBIDAS')
cabecalho('CADASTRO DAS BEBIDAS')
while True:
    while True:
        produto = str(input('Nome do produto: (coca, heniken, shoop_vinho) ->')).strip().upper()
        if produto != 'COCA' and produto != 'HENIKEN' and produto != 'SHOPP_VINHO':
            print('ERRO! Digite o nome que está entre parentes.')
        else:
            break
    try:
        quantidade = int(input('Quantidade: '))
    except (ValueError, TypeError):
        print('ERRO! Digite um valor inteirio.')
    else:
        print('ok')
    try:
        preço = float(input('Preço: R$'))
    except (ValueError, TypeError):
        print('ERRO! Digite um valor real.')
    else:
        print('ok')
    cadastro(arq, produto, quantidade, preço)
    continuar = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if continuar in 'N':
        print('Vonte sempre!')
        break




