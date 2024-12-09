from flask import Flask
from database import db
from models.refeicao import Refeicao


app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app=app)


@app.route("/", methods=['GET'])
def welcome():
    return "Welcome! You've been here."


@app.route("/refeicao", methods=['POST'])  # Registrar uma refeição feita
def criar_refeicao():
    pass


@app.route("/refeicao", methods=['GET'])  # Listar todas as refeições
def listar_refeicoes():
    pass


# Visualizar uma única refeição
@app.route("/refeicao/<int:id_refeicao>", methods=['GET'])
def listar_uma_refeicao():
    pass


# Editar uma refeição
@app.route("/refeicao/<int:id_refeicao>", methods=['PUT'])
def editar_refeicao():
    pass


# Apagar uma refeição
@app.route("/refeicao/<int:id_refeicao>", methods=['DELETE'])
def deletar_refeicao():
    pass


if __name__ == '__main__':
    app.run(debug=True)
