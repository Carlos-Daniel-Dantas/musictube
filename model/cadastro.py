from database.conexao import conectar 

def cadastrar_usuario(login:str, senha:str):
    
    #passo 1 e 2 já feito

    try:
        conexao, cursor = conectar()

        cursor.execute("""

                        insert INTO cadastro
        
                        (usuario, senha)
                        values (%s, %s);
                    
                    """, 
                    [login, senha]
                    
                    )

        conexao.commit()
        conexao.close()

        return True
    except:
        return False

