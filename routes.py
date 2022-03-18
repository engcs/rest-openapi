from flask import Flask, request
from main import retorna_tabela

app = Flask("Ampacidade")

@app.route("/pvc", methods=["GET"])
def get_pvc():
    return {"ola": "mundo"}

@app.route("/pvc", methods=["POST"])
def post_pvc():

    body = request.get_json()
    tabela = retorna_tabela()
    return tabela

app.run()