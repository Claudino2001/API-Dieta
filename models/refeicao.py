from database import db
from datetime import datetime


class Refeicao(db.Model):
    __tablename__ = 'refeicoes'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    nome = db.Column(db.String(80), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False, default=datetime.now)
    dentro_da_dieta = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "data_hora": self.data_hora.isoformat() if self.data_hora else None,
            "dentro_da_dieta": self.dentro_da_dieta,
        }
