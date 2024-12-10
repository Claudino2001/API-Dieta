from database import db
from sqlalchemy.orm import relationship
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    # Relacionamento com Refeicao
    refeicoes = relationship('Refeicao', backref='user', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }