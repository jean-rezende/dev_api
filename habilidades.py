from flask_restful import Resource

lista_habilidades = ['Python', 'Flask', 'Java', 'PHP']

class Habilidades(Resource):
    def get(self):
        return lista_habilidades
