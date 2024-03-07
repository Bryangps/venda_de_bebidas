
while True:
    try:
        nome_bebida = input('Digite o nome da Bebida: ').strip().title()
    except KeyboardInterrupt:
        print('\nNão foi possivel cancelar')
    else:
        if nome_bebida.isalpha() and not nome_bebida in '':
            print('ok')
            break
        else:
            print('Campo inão pode ficar vazio é não pode conter numéro!')


print('Escolha uma das opções abaixo: ')
print('[1] - Alcoólica\n'
      '[2] - Não Alcoólica')

while True:
    try:
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            tipo_bebida = 'Alcoólica'
            break
        elif opcao == 2:
            tipo_bebida = 'Não Alcoólica'
            break
        else:
            print('Opção invalida')
    except ValueError:
        print('Erro... Campo não pode conter letras é não pode ficar vazio')
    except KeyboardInterrupt:
        print('\nNão foi possivel cancelar')


while True:
    try:
        qtd_caixa = int(input('Digite a quantidade de caixa: '))
    except ValueError:
        print('Erro... Campo não pode conter letras é não pode ficar vazio')
    except KeyboardInterrupt:
        print('\nNão foi possivel cancelar')
    else:
        break

while True:
    try:
        unidade = int(input('Quantas unidade tem uma caixa: '))
    except ValueError:
        print('Erro... Campo não pode conter letras é não pode ficar vazio')
    except KeyboardInterrupt:
        print('\nNão foi possivel cancelar')
    else:
        break

while True:
    try:
        valor_gasto = input('Valor total gasto: R$')
        valor_gasto = valor_gasto.replace(',', '.')
        valor_gasto = float(valor_gasto)
    except ValueError:
        print('Erro... Campo não pode conter letras é não pode ficar vazio')
    except KeyboardInterrupt:
        print('\nNão foi possivel cancelar')
    else:
        break

while True:
    try:
        valor_venda = input('Valor de venda da unidade: R$ ')
        valor_venda = valor_venda.replace(',', '.')
        valor_venda = float(valor_venda)
    except ValueError:
        print('Erro... Campo não pode conter letras é não pode ficar vazio')
    except KeyboardInterrupt:
        print('\nNão foi possivel cancelar')
    else:
        break



