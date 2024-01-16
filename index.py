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

while True:
    produto = nomeproduto()
    if produto == 'stop':
        break
    else:
        qtd = quatidade()
        if qtd == 'stop':
            break
    while True:
        resp = str(input('Efetuar cadastrar [S/N]: '))[0]
        if resp in 'Ss':
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO produto(nome, quantidade)
                VALEUS(? , ?);
            
            """, (produto, qtd))
            break
        elif resp in 'Nn':
            break
        else:
            print('ERRO, Valor invalido, informe "S ou N" ')





# 3 - Criar a tabela de clientes

# 4 - Fazer a venda do produto para o cliente


# 5 - Valor total da conta do cliente



# 6 - Iformar o status do cliente, se está pago ou não.