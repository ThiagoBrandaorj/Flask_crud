from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pesquisa(db.Model):
    __tablename__ = 'pesquisa'
    pesquisa_id = db.Column(db.Integer, primary_key=True)
    pesquisa_nome = db.Column(db.String(128), nullable=False)
    data_inicio = db.Column(db.DateTime, nullable=False)
    data_fim = db.Column(db.DateTime, nullable=False)
    data_cadastro = db.Column(db.DateTime, default=db.func.current_timestamp())
    ativo = db.Column(db.Boolean, default=True)

