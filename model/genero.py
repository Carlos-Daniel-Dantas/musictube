from database.conexao import conectar 

def recuperar_generos():

    conexao, cursor = conectar()

    cursor.execute("SELECT nome, icone, cor FROM genero;")

    generos = cursor.fetchall()

    conexao.close()

    return generos