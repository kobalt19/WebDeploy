import os
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def index():
    return 'Привет от приложения Степана'


def main():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()
