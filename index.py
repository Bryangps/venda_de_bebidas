from suporte import *
from conexao import conn
# 1 - Criar a tabela de produto
'''
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE produto(
    id SERIAL PRIMARY KEY, 
    nome TEXT NOT NULL,
    quantidade INTEGER
    );
""")
print('Tabela criada com sucesso')

conn.commit()
cursor.close()
conn.close()
'''

# 2 - Cadastras produtos
print('-' * 45)
print('CADASTRO DE BEBIDAS'.center(45))
print('-' * 45)

ok = True
while ok:
    produto = nomeproduto()
    if produto == 'stop':
        break
    else:
        qtd = quatidade()
        if qtd == 'stop':
            break

    while True:
        confimacao = str(input('Confirma cadrasto [S/N]: '))[0]
        if confimacao.isdigit():
            print('Erro!! O campo não pode ser preenchido com número')
        elif confimacao in 'Ss':
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO produto(nome, quantidade)
                VALUES(%s, %s)
            
            """, (produto, qtd))
            conn.commit()
            cursor.close()
            print('Cadastrado com sucesso!!!')
            break
        elif confimacao in 'Nn':
            break
        else:
            print('ERRO!!! Valor invalido, informe "S ou N"')

    while True:
        resp = str(input('Deseja continuar cadastrando [S/N]: '))[0]
        if resp.isdigit():
            print('Erro!!! O campo não pode ser preenchido com número')

        elif resp in 'Nn':
            ok = False
            break
        elif resp in 'Ss':
            break
        else:
            print('ERRO, Valor invalido, informe "S ou N" ')





# 3 - Criar a tabela de clientes

# 4 - Fazer a venda do produto para o cliente


# 5 - Valor total da conta do cliente



# 6 - Iformar o status do cliente, se está pago ou não.