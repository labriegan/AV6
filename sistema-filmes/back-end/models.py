from config import *
import os

class Filme(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    genero = db.Column(db.String(254))
    distribuidora = db.Column(db.String(254))
    diretores = db.Column(db.String(254))    

    def __str__(self):
        return f'''
                - id: ({self.id}) 
                - nome: {self.nome} 
                - genero: {self.genero} 
                - distribuidora: {self.distribuidora}
                - diretores: {self.diretores}
                '''
    
    def json(self):
        return ({
            "id": self.id,
            "nome": self.nome,
            "genero": self.genero,
            "distribuidora": self.distribuidora,
            "diretores": self.diretores,
        })

class Espectador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    idade = db.Column(db.String(254))
    profissao = db.Column(db.String(254))

    def __str__(self):
        s = f'''
                * Espectador({self.id})
                * nome: {self.nome}
                * idade: {self.idade}
                * profissao: {self.profissao}'''
        return s

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "profissao": self.profissao,
        }


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nota = db.Column(db.String(254))
    data = db.Column(db.String(254))
    opiniao = db.Column(db.String(254))
    filme_id = db.Column(db.Integer, db.ForeignKey(Filme.id), nullable=False)
    filme = db.relationship("Filme")
    espectador_id = db.Column(db.Integer, db.ForeignKey(Espectador.id), nullable=False)
    espectador = db.relationship("Espectador")

    def __str__(self):
        return f'''
        # Review({self.id})
        # nota: {self.nota}
        # data: {self.data}
        # opiniao: {self.opiniao}
        # filme do review: {self.filme}
        # assistido por: {self.espectador}
        '''
        
    def json(self):
        return {
            "id": self.id,
            "nota": self.nota,
            "data": self.data,
            "opiniao": self.opiniao,
            "filme_id": self.filme_id,
            "filme": self.filme.json(),
            "espectador_id": self.espectador_id,
            "espectador": self.espectador.json()
        }