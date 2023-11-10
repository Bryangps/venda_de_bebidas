def linha(tot=40):
    print('-' * tot)


def cabecalho(msg):
    linha()
    print(f'{msg}'.center(40))
    linha()


def arquivoExist(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print('Arquivo criado com sucesso')


def cadastro(arq, produto='<desconhecido>', quantidade=0, preço=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{produto}; {quantidade}; {preço}\n')
        except:
            print('Houve um erro na hora de escrver os dados')
        else:
            print(f'Novo registro de {produto} adicionado')
            a.close

