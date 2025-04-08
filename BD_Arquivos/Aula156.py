import sqlite3

from Aula152 import exp_sql

con = sqlite3.connect("empresa.db")
cur = con.cursor()

exp_sql = """
SELECT matricula, nome FROM funcionarios
    WHERE nome LIKE :args
"""
nome = input("Funcionário a localizar: ")
args = (f'%{nome}%',)

cur.execute(exp_sql, args)
dados = cur.fetchall()
for linha in dados:
    print(f'Matricula: {linha[0]}, Nome: {linha[1]}')


con.close()
