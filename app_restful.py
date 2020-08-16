from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id':0,
     'nome':'Jean',
     'habilidades':['Python', 'Flask']},
    {'id':1,
     'nome':'Carlos',
     'habilidades':['Python', 'Django']}
]
# Devolve um desenvolvedor pelo Id. Também Altera e deleta um desenvolvedor pelo Id.
class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            menssagen = 'Desenvolvedor de id {} não existe.'.format(id)
            response = {'status': 'erro', 'Mensagen': menssagen}
        except Exception:
            menssagem = 'Erro Desconhecido. Procure o administrador da API.'
            response = {'status': 'erro', 'Mensagen': menssagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'Status': 'Sucesso', 'Menssagem':'Registro excluído'}

# Lista todos os desenvolvedores e permite registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]

api.add_resource(Desenvolvedor,'/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores,'/dev/')
api.add_resource(Habilidades,'/habilidades/')

if __name__ == '__main__':
    app.run(debug=True)