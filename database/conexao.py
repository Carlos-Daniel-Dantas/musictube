
import mysql.connector


def conectar():

    tipo_conexao = "NUVEM"

    if tipo_conexao == "LOCAL":
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            port="3306",
            user="root",
            password="root",
            database="MusicClube"
            
        )
    else:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            port="3306",
            user="root",
            password="root",
            database="MusicClube"
                
        )

    #Criando o cursor

    cursor = conexao.cursor(dictionary=True)

    return conexao, cursor 