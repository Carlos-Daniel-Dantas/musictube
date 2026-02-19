from database.conexao import conectar 

def recuperar_generos():
    
    #passo 1 e 2 já feito
    conexao, cursor = conectar()

    cursor.execute("SELECT nome, icone, cor FROM genero;")

    generos = cursor.fetchall()

    conexao.close()

    return generos