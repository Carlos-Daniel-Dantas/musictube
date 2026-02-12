from flask import Flask, render_template
import mysql.connector


app = Flask (__name__)

@app.route("/home", methdots=["GET"])
@app.route("/")

def pagina_principal():

    #conectando no banco de dados
    conexao = mysql.connctor.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="root",
        database="Musicclube"
        
    )

    #Criando o cursor
    cursor = conexao.cursor(dictionary=True)

    #executando a consulta
    cursor.execute("SELECT codigo, cantor, duracao, nome, url_imagem, nome_genero, FROM musica;")

    #recuperando os dados
    musicas = cursor.fetchall()

    #fechando conexão
    conexao.close()

    return render_template("principal.html", musicas = musicas)

if __name__ == "__main__":
    app.run(debug=True)