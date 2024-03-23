from flask import Flask

flask_app = Flask(__name__)
flask_app.config.from_pyfile('flask_config.py')


@flask_app.route('/')
def hello_world():
    return open('index.html', encoding='utf8').read()

def client_ready(*_):
    print(_)
    flask_app.run(host='0.0.0.0')
    print('running')


if __name__ == '__main__':
    client_ready()
    pass
