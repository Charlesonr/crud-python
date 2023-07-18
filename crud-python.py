import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='bdcrud',
)

cursor = conexao.cursor() #executa as operações na conexão 

#CRUD

#comando = '' #comando sql
#cursor.execute(comando) #manda esse comando sql ser executado
#conexao.commit() # edita o banco de dados
# resultado = cursor.fetchall() #ler o banco de dados


#CREATE

nome_produto = "Computadores"
valor = 20
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conexao.commit()


#READ
"""
comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)
"""

#UPDATE

"""
nome_produto = "tod"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}" '
cursor.execute(comando)
conexao.commit()
"""

#DELETE

"""
nome_produto = "tod"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}" '
cursor.execute(comando)
conexao.commit()
"""

cursor.close()
conexao.close()