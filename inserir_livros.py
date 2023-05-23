from conexao import conexao, cursor


def limpa():
    cursor = conexao.cursor()
    cursor.execute("TRUNCATE tabela")
    conexao.commit()


def listar_livros():
    sql = 'SELECT * from tabela'
    cursor.execute(sql)
    return cursor.fetchall()


def inserir(editora, nome, preco):
    inserir_usuarios = f"""INSERT INTO tabela(editora, nome, preco)
        values
        ("{editora}", "{nome}", {preco});"""
    cursor = conexao.cursor()

    cursor.execute(inserir_usuarios)
    conexao.commit()


