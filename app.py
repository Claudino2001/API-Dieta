from flask import Flask


app = Flask(__name__)


@app.route("/", methods=['GET'])
def welcome():
    return "Welcome! You've been here."


if __name__ == '__main__':
    app.run(debug=True)
