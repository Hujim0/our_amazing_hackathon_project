from flask import Flask

flask_app = Flask(__name__)
# flask_app.config.from_pyfile('flask_config.py')


@flask_app.route('/')
def main_page():
    return open('index.html', encoding='utf8').read()

@flask_app.route('/request')
def request():
    return open('hello.html', encoding='utf8').read()


def client_ready(*_):
    print(_)
    flask_app.run(host='0.0.0.0', port=80)
    print('running')


if __name__ == '__main__':
    client_ready()
    pass
