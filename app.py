from flask import Flask, render_template, request, redirect
from model.genero import recuperar_generos
from model.musica import recuperar_musicas, salvar_musica
from model.musica import excluir_musica, ativar_musica
from model.cadastro import cadastrar_usuario 

import mysql.connector

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

    musicas = recuperar_musicas(True)
    generos = recuperar_generos()

    return render_template("principal.html", musicas = musicas, genero = generos)

@app.route("/musica/post", methods=["POST"])
def api_inserir_musica():

    nome_musica = request.form.get("input_nome_musica")
    cantor_musica = request.form.get("input_cantor_musica")
    duracao_musica = request.form.get("input_duracao_musica")
    url_musica = request.form.get("input_url_musica")
    genero_nome = request.form.get("genero_nome")


    if salvar_musica(nome_musica, cantor_musica, duracao_musica, url_musica, genero_nome ):

        return redirect("/admin")
    else:
        return "Erro ao adicionar música"
    
@app.route("/musica/delete/<codigo>")
def apagar_musica (codigo):
    excluir_musica(codigo)
    return redirect("/admin")

@app.route("/musica/ativar/<codigo>/<status>")
def mudar_status_musica (codigo, status):
    ativar_musica(codigo, status)
    return redirect("/admin")

@app.route("/usuario/cadastro", methods=["POST"])
def cadastro_de_usuario():

    senha = request.form.get("input_usuario")
    usuario = request.form.get("input_senha")

    cadastrar_usuario(senha,usuario)
    return redirect("/home")

@app.route("/cadastro", methods=["GET"])

def cadastro_usuario():

    return render_template("cadastro.html")

@app.route("/login")

def login_usuario():
        return render_template("cadastro.html")



if __name__ == "__main__":
    app.run(debug=True)