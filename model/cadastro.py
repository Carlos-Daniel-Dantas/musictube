from database.conexao import conectar 

def cadastrar_usuario(login:str, senha:str):
    
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

def autenticar_usuario(login:str, senha:str) -> list:

    """ Função que Verifica se o úsuario esta cadastrado, 
    se estiver retorna todos os dados do usuário, se não
      estiver etorna None"""

    conexao, cursor = conectar()

    cursor.execute("""

                    select usuario, senha From cadastro WHERE usuario = %s and senha = %s
                
                """, 
                [login, senha]
                
                )
    
    usuario = cursor.fetchone()

    if usuario is not None:
        try:
            return True
        except Exception as erro:
            print(erro)
            return False

