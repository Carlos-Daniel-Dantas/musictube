
create DATABASE IF NOT EXISTS Musicclube;

use Musicclube;

CREATE TABLE IF NOT EXISTS genero (
 nome VARCHAR(30) NOT NULL primary key,
 icone VARCHAR(100),
 cor VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS musica (
 codigo INT NOT NULL primary key auto_increment,
 cantor VARCHAR(50) NOT NULL,
 duracao TIME,
 nome VARCHAR(80),
 url_imagem CHAR(255),
 nome_genero VARCHAR(30),
 constraint fk_musica_genero foreign key (nome_genero) REFERENCES genero (nome)
);



