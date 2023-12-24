def linha(tot=40):
    print('-' * tot)


def cabecalho(msg):
    linha()
    print(f'{msg}'.center(40))
    linha()


def arquivo_exist(nome):
    try:
        with open(nome, 'r', encoding='utf-8') as produtos:
            produtos.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    with open(nome, 'w', encoding='utf-8') as arquivo:
        arquivo.close()
        print('Arquivo criado com sucesso')


def cadastro(arq, produto='<desconhecido>', quantidade=0, preco=0):
    with open(arq, 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{produto}; {quantidade}; {preco:.2f}\n')
        print(f'Novo registro de {produto} adicionado')


class Produto:
    def __init__(self):
        self.produto = []

    def name_produto(self):
        while True:
            nome = str(input('Nome do produto: {coca, heniken, shopp_vinho}: ')).strip().upper()
            if nome != 'COCA' and nome != 'HENIKEN' and nome != 'SHOPP_VINHO':
                print('ERRO! Digite o nome que está entre parentes.')
            else:
                self.produto.append(nome)
                break

    def quantidade_produto(self):
        while True:
            try:
                quantidade = int(input('Quantidade: '))
            except (ValueError, TypeError):
                print('ERRO! Digite um valor inteirio.')
            else:
                print('Cadastrado com sucesso')
                self.produto.append(quantidade)
                break

    def valor_produto(self):
        while True:
            try:
                valor = float(input('Preço: R$'))
            except (ValueError, TypeError):
                print('ERRO! Digite um valor real.')
            else:
                print('Cadastrado com sucesso')
                self.produto.append(valor)
                break

    def cadastrando_produto(self, arq):
        with open(arq, 'a', encoding='utf-8') as arquivo:
            arquivo.write(f'{self.produto[0]}; {self.produto[1]}; {self.produto[2]:.2f}\n')
            print(f'{self.produto[0]} adicionado')
        del self.produto[:3]



