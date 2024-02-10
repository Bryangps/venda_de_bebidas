def tratar_istrig(nome):
    nome = nome.strip()
    nome = nome.title()
    if nome:
        if nome.isdigit():
            print('ERRO, O campo não pode ser preechido com número!!')
        else:
            return nome
    else:
        print('Campo não pode ficar vazio !!')




def nomeproduto(name):
    while True:
        try:
            if name.isdigit():
                print('ERRO, O campo não pode ser preechido com número!!')
            else:
                if name == '':
                    print('Campo não pode ficar vazio !!')
                else:
                    return name
        except KeyboardInterrupt:
            print('\nVolte sempre')
            return 'stop'


def quatidade():
    while True:
        try:
            qtd = int(input('QTD: '))
        except (ValueError, TypeError):
            print('Informe um número interio')
        except KeyboardInterrupt:
            print('\nVolte sempre')
            return 'stop'
        else:
            return qtd





