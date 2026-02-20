from database.conexao import conectar 

def recuperar_musicas():
    
    #passo 1 e 2 já feito
    conexao, cursor = conectar()

    cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero FROM musica;")

    musicas = cursor.fetchall()

    conexao.close()

    return musicas


def salvar_musica(nome_musica:str, cantor:str, duracao:str, url_imagem:str, genero:str) -> bool:
    """
    Esta função ira servir para adicionar as músicas e conferir com o bool se realmente foi adicionada.

    """
    try:

        conexao, cursor = conectar()

        cursor.execute("""
                    
                    insert INTO musica 

                    (cantor, duracao, nome, url_imagem, nome_genero)
                    values (%s, %s, %s, %s,%s);

                    """,

                    [ cantor, duracao, nome_musica, url_imagem, genero ]
                
                    )
        
        conexao.commit()
        conexao.close()

        return True
    except:
        return False

    #def excluir_musica():

    

