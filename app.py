from flask import Flask, render_template
import mysql.connector
from model.genero import recuperar_generos
from model.musica import recuperar_musicas

app = Flask (__name__)



@app.route("/admin")
def pagina_admin():

    #RECUPERANDO MÚSICAS
    musicas = recuperar_musicas()
    generos = recuperar_generos()

    #MOSTRANDO PÁGINA
    return render_template("administracao.html", musicas = musicas, generos = generos)


@app.route("/home", methods=["GET"])
@app.route("/")
def pagina_principal():

    musicas = recuperar_musicas()
    generos = recuperar_generos()



    return render_template("principal.html", musicas = musicas, generos = generos)

if __name__ == "__main__":
    app.run(debug=True)