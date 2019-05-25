from flask import Flask


app = Flask(__name__)


@app.route('/')
def prima_pagina():
    return '<Title>Prima Pagina</Title>'


@app.route('/hidden')
def pagina_ascunsa():
    return 'M-ai gasit!'


if __name__=='__main__':
    app.run(port=8080, host='localhost')
