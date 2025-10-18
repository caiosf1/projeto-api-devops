from config import db

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    descricao = db.Column(db.String(200))

    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
