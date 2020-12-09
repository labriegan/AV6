import os
from models import Filme, Review, Espectador
from config import db, db_file


if __name__ == '__main__':
    if os.path.exists(db_file):
        os.remove(db_file)

    db.create_all()

    f1 = Filme(nome ='O Poderoso Chefão',
                genero ='Drama',
                distribuidora ='Paramount',
                diretores ='Francis Ford Coppola')
    f2 = Filme(nome ='O Mágico de Oz',
                genero ='Musical/Fantasia',
                distribuidora ='Metro-Goldwyn-Mayer',
                diretores ='Victor Fleming')
    f3 = Filme(nome ='Cidadão Kane',
                genero ='Drama/Suspense',
                distribuidora ='RKO Rádio Pictures',
                diretores ='Orson Welles')
    f4 = Filme(nome ='Um Sonho de Liberdade',
                genero ='Drama',
                distribuidora ='Columbia Pictures',
                diretores ='Frank Darabont')
    f5 = Filme(nome ='Pulp Fiction – Tempo de Violência',
                genero ='Drama Policial',
                distribuidora ='Miramax Films',
                diretores ='Quentin Tarantino')
    


    db.session.add(f1)
    db.session.add(f2)
    db.session.commit()
    
    print(f1)
    print(f2)
    print(f2.json())

    espect1 = Espectador(nome = "Gabrielen",
                        idade = "17",
                        profissao = "Estudiante"
    )

    review1 = Review(nota = "10000",
                    data = "31/10/1507",
                    opiniao = "Muito bom",
                    filme = f2,
                    espectador = espect1
    )

    db.session.add(espect1)
    db.session.add(review1)
    db.session.commit()

    print(espect1)
    print(review1)