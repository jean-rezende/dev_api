import json

from flask import Flask, jsonify, request

app = Flask(__name__)

desenvolvedores = [
    {'id':0,
     'nome':'Jean',
     'habilidades':['Python', 'Flask']},
    {'id':1,
     'nome':'Carlos',
     'habilidades':['Python', 'Django']}
]
# Devolve um desenvolvedor pelo Id. Também Altera e deleta um desenvolvedor pelo Id.
@app.route('/dev/<int:id>/', methods = ['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method =='GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            menssagen = 'Desenvolvedor de id {} não existe.' .format(id)
            response = {'status':'erro', 'Mensagen': menssagen}
        except Exception:
            menssagem = 'Erro Desconhecido. Procure o administrador da API.'
            response = {'status': 'erro', 'Mensagen': menssagem}
        return jsonify(response)
    elif request.method =='PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'Status': 'Sucesso', 'Menssagem':'Registro excluído'})

# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
@app.route('/dev/', methods = ['POST', 'GET'])
def lista_desencolvedor():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method =='GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run(debug = True)