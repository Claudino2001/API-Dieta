from flask import Flask, request, jsonify
from database import db
from models.user import User
from models.refeicao import Refeicao
from datetime import datetime
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

login_manager = LoginManager()
db.init_app(app=app)
login_manager.init_app(app=app)

# Definindo a view de login (quando o usuário não está autenticado)
login_manager.login_view = 'login'

# Rota teste
@app.route("/", methods=['GET'])
def welcome():
    return "Welcome! You've been here."

######################### ROTAS DE USUÁRIO #########################

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/whoim", methods=['GET'])
@login_required
def whoim():
    return jsonify({"Who I'm":f"I'm: [{current_user.id}] - {current_user.name}"})


@app.route("/user", methods=['POST'])
def criar_usuario():
    ''' Precisará receber Nome e Senha como parametro para criar um objeto do tipo
    usuário no banco de dados. '''
    data = request.json
    name = data.get("name")
    password = data.get("password")

    if name and password:
        u = User(name=name, password=password)
        db.session.add(u)
        db.session.commit()
        return jsonify({'message': 'Usuário cadastrado com sucesso.'})
    
    return jsonify({'message': 'Parâmetros inválidos.'}), 400

@app.route("/login", methods=['POST'])
def login():
    ''' Precisará receber Nome e Senha como parametro 
    para autenticar o usuário no sistema. '''
    data = request.json
    name = data.get("name")
    password = data.get("password")

    if name and password:
        u = User.query.filter_by(name=name).first()
        if u and u.password == password:
            login_user(u)
            print(current_user.is_authenticated)
            return jsonify({'message': 'Usuário logado com sucesso.'})
        return jsonify({'message': 'Usuário não encontrado.'}), 404
    
    return jsonify({'message': 'Parâmetros inválidos.'}), 400

@app.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Usuário deslogado com sucesso.'})

######################### ROTAS DE REFEIÇÃO #########################

# Registrar uma refeição feita
@app.route("/refeicao", methods=['POST'])
@login_required
def criar_refeicao():
    ''' Precisará receber Nome, Descrição e Dentro_da_dieta como parametro
    para criar um objeto do tipo refeição no banco de dados. '''
    data = request.json
    nome = data.get("nome")
    descricao = data.get("descricao")
    dentro_da_dieta = data.get("dentro_da_dieta")

    if nome and descricao and dentro_da_dieta is not None:
        u = User.query.get(current_user.id)
        r = Refeicao(nome=nome, descricao=descricao, dentro_da_dieta=dentro_da_dieta)
        u.refeicoes.append(r)
        db.session.add(r)
        db.session.commit()
        return jsonify({'message': 'Refeição cadastrada com sucesso.'})
    
    return jsonify({'message': 'Parâmetros inválidos.'}), 400


# Listar todas as refeições
@app.route("/refeicao", methods=['GET'])
@login_required
def listar_refeicoes():
    dict = []
    todas_as_refeicoes = current_user.refeicoes
    for refeicao in todas_as_refeicoes:
        dict.append(refeicao.to_dict())
    return jsonify({"todas_refeicoes": dict})


# Visualizar uma única refeição
@app.route("/refeicao/<int:id_refeicao>", methods=['GET'])
@login_required
def listar_uma_refeicao(id_refeicao):
    refeicao = Refeicao.query.filter_by(id=id_refeicao, id_usuario=current_user.id).first()
    if refeicao:
        return jsonify({f"refeicao-{id_refeicao}": refeicao.to_dict()})
    
    return jsonify({"message": f"Refeição {id_refeicao} não encontrada."}), 404


# Editar uma refeição
@app.route("/refeicao/<int:id_refeicao>", methods=['PUT'])
@login_required
def editar_refeicao(id_refeicao):
    data = request.json 
    refeicao = Refeicao.query.filter_by(id=id_refeicao, id_usuario=current_user.id).first()

    if refeicao and data.get("nome") and data.get("descricao") and data.get("data_hora") and data.get("dentro_da_dieta") is not None:

        refeicao.nome = data.get("nome")
        refeicao.descricao = data.get("descricao")
        refeicao.dentro_da_dieta = data.get("dentro_da_dieta")
        refeicao.data_hora = datetime.fromisoformat(data.get("data_hora").replace("Z", "+00:00"))

        db.session.commit()

        return jsonify({"message": f"Refeição {id_refeicao} atualizada."})
    
    return jsonify({"message": f"Não foi possível atualizar a refeição {id_refeicao}."}), 404


# Apagar uma refeição
@app.route("/refeicao/<int:id_refeicao>", methods=['DELETE'])
@login_required
def deletar_refeicao(id_refeicao):
    refeicao = Refeicao.query.filter_by(id=id_refeicao, id_usuario=current_user.id).first()
    
    if refeicao:
        db.session.delete(refeicao)
        db.session.commit()
        return jsonify({'message': f'Refeição {id_refeicao} deletada com sucesso.'})

    return jsonify({'message': f'Refeição {id_refeicao} não encontrada.'}), 404


if __name__ == '__main__':
    app.run(debug=True)
