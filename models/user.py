from database import db
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120), nullable=False)

    # Relacionamento com Refeicao
    refeicoes = relationship('refeicoes', backref='user', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }