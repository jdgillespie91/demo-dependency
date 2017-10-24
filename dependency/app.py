from flask import Flask, current_app


app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    with app.app_context():
        try:
            current_app.count += 1
        except AttributeError:
            current_app.count = 1

    return 'Hello, world!' if current_app.count < 5 else '¡Hola, mundo!'

