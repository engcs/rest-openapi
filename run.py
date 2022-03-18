from flask import Flask, request, render_template, send_file, url_for, send_from_directory
from main import retorna_tabela_pvc

app = Flask(__name__, static_folder='static')

@app.route('/get_image', methods=["GET"])
def get_image():
    # if request.args.get('type') == '1':
    #    filename = 'static\\img\\nbr5410_tabela_36.png'
    # else:
    #    filename = 'static\\img\\error.png'
    # return send_from_directory("static", 'img/error.png', mimetype='image/png')
    return render_template('imagem.html', caminho=url_for("static", filename='img/nbr5410_tabela_36.png'))

@app.route("/pvc", methods=["GET"])
def get_pvc():
    return {"ola": "mundo"}

@app.route("/pvc", methods=["POST"])
def post_pvc():

    body = request.get_json()

    # if("nome" not in body):
    #     return {"status": 400, "mensagem": "O parâmetro 'nome' é obrigatório"}
    #
    # if ("email" not in body):
    #     return {"status": 400, "mensagem": "O parâmetro 'email' é obrigatório"}

    # nome = body["nome"]
    # email = body["email"]

    tabela = retorna_tabela_pvc()

    titulo = "Cabos com isolação PVC/70ºC"
    titulo_body = "Cabos com isolação PVC/70ºC (ABNT NBRNM247-3 de 02/2002)"
    descricao = "Cabos isolados com policloreto de vinila (PVC) para tensões nominais até 450/750V, inclusive - Parte 3: Condutores isolados (sem cobertura) para instalações fixas (IEC 60227-3, MOD)"

    return render_template('template.html',
                           titulo=titulo,
                           titulo_body=titulo_body,
                           descricao=descricao,
                           tabela=tabela)

def gerar_response(status, mensagem, nome_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem
    if(nome_conteudo and conteudo):
        response[nome_conteudo] = conteudo
    return response


app.config['JSON_AS_ASCII'] = False
if __name__ == '__main__':
    app.run(debug=True)