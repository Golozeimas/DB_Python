import sqlite3

def conectar_no_banco():
    conexao = sqlite3.connect("entretenimento.db")
    return conexao

def inseri_dados(nome, ano, nota):
    conexao = conectar_no_banco()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO filmes(nome_filme, ano_filme, nota_filme) VALUES (?,?,?)",(nome, ano, nota))
    conexao.commit()
    conexao.close()

def ler_dados():
    conexao = conectar_no_banco()
    cursor = conexao.cursor()
    lista = cursor.execute("SELECT * FROM filmes")
    dados = lista.fetchall()
    return dados

def deletar_dados(id):
    conexao = conectar_no_banco()
    cursor = conexao.cursor()
    cursor.execute(f"DELETE FROM filmes WHERE id={id}")
    conexao.commit()
    conexao.close()

def update_dados(id, nome, ano, nota):
    conexao = conectar_no_banco()
    cursor = conexao.cursor()
    cursor.execute(f"UPDATE filmes SET nome_filme=?,ano_filme=?,nota_filme=? WHERE id={id}",(nome, ano, nota))
    conexao.commit()
    conexao.close()