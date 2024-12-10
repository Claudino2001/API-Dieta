from flask import Flask, request, jsonify
from database import db
from models import user, refeicao
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app=app)


# Rota teste
@app.route("/", methods=['GET'])
def welcome():
    return "Welcome! You've been here."


# Registrar uma refeição feita
@app.route("/refeicao", methods=['POST'])
def criar_refeicao():
    ''' Precisará receber Nome, Descrição e Dentro_da_dieta como parametro
    para criar um objeto do tipo refeição no banco de dados. '''
    data = request.json
    nome = data.get("nome")
    descricao = data.get("descricao")
    dentro_da_dieta = data.get("dentro_da_dieta")

    if nome and descricao and dentro_da_dieta:
        r = Refeicao(nome=nome, descricao=descricao, dentro_da_dieta=dentro_da_dieta)
        db.session.add(r)
        db.session.commit()
        return jsonify({'message': 'Refeição cadastrada com sucesso.'})
    
    return jsonify({'message': 'Parâmetros inválidos.'}), 400


# Listar todas as refeições
@app.route("/refeicao", methods=['GET'])
def listar_refeicoes():
    dict = []
    todas_as_refeicoes = Refeicao.query.all()
    for refeicao in todas_as_refeicoes:
        dict.append(refeicao.to_dict())
    return jsonify({"todas_refeicoes": dict})


# Visualizar uma única refeição
@app.route("/refeicao/<int:id_refeicao>", methods=['GET'])
def listar_uma_refeicao(id_refeicao):
    refeicao = Refeicao.query.get(id_refeicao)
    if refeicao:
        return jsonify({f"refeicao-{id_refeicao}": refeicao.to_dict()})
    
    return jsonify({"message": f"Refeição {id_refeicao} não encontrada."}), 404


# Editar uma refeição
@app.route("/refeicao/<int:id_refeicao>", methods=['PUT'])
def editar_refeicao(id_refeicao):
    data = request.json 
    refeicao = Refeicao.query.get(id_refeicao)

    if refeicao and data.get("nome") and data.get("descricao") and data.get("data_hora") and data.get("dentro_da_dieta"):

        refeicao.nome = data.get("nome")
        refeicao.descricao = data.get("descricao")
        refeicao.dentro_da_dieta = data.get("dentro_da_dieta")
        refeicao.data_hora = datetime.fromisoformat(data.get("data_hora").replace("Z", "+00:00"))

        db.session.commit()

        return jsonify({"message": f"Refeição {id_refeicao} atualizada."})
    
    return jsonify({"message": f"Não foi possível atualizar a refeição {id_refeicao}."}), 404


# Apagar uma refeição
@app.route("/refeicao/<int:id_refeicao>", methods=['DELETE'])
def deletar_refeicao(id_refeicao):
    refeicao = Refeicao.query.get(id_refeicao)
    
    if refeicao:
        db.session.delete(refeicao)
        db.session.commit()
        return jsonify({'message': f'Refeição {id_refeicao} deletada com sucesso.'}), 404

    return jsonify({'message': f'Refeição {id_refeicao} não encontrada.'}), 404


if __name__ == '__main__':
    app.run(debug=True)
