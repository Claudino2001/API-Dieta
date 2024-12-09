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


if __name__ == '__main__':
    app.run(debug=True)
