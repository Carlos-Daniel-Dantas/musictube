from database.conexao import conectar 

def recuperar_musicas():
    
    #passo 1 e 2 já feito
    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero FROM musica;")

    musicas = cursor.fetchall()

    conexao.close()

    return musicas