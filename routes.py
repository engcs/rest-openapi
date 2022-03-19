from flask import Flask, request
from main import retorna_tabela

app = Flask("Ampacidade")

@app.route("/pvc", methods=["GET"])
def get_pvc():
    return {"ola": "mundo"}

@app.route("/pvc", methods=["POST"])
def post_pvc():

    body = request.get_json()

    if("nome" not in body):
        return {"status": 400, "mensagem": "O parâmetro 'nome' é obrigatório"}

    if ("email" not in body):
        return {"status": 400, "mensagem": "O parâmetro 'email' é obrigatório"}

    nome = body["nome"]
    email = body["email"]
    tabela = retorna_tabela(nome, email)

    return gerar_response(200, "Usuário criado", "nome", nome)

def gerar_response(status, mensagem, nome_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem
    if(nome_conteudo and conteudo):
        response[nome_conteudo] = conteudo
    return response


app.config['JSON_AS_ASCII'] = False
app.run()