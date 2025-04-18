from flask_restx import Namespace, Resource, fields
from flask import request
from backend.app.controllers import LivroController
from backend.app.middlewares.autorizacao_livro import autorizacao_livro
from flask_jwt_extended import jwt_required

api = Namespace('livros', description='Operações relacionadas a Livros')

livro_model = api.model('Livro', {
    'id_genero': fields.String(required=True, description='ID do Gênero'),
    'id_autor': fields.String(required=True, description='ID do Autor'),
    'foto': fields.String(required=True, description='Foto'),
    'sinopse': fields.String(required=True, description='Sinopse'),
    'estoque': fields.Integer(required=True, description='Estoque'),
    'preco': fields.Float(required=True, description='Preço'),
    'formato': fields.String(required=True, description='Formato'),
    'tipo': fields.String(required=True, description='Tipo'),
    'titulo': fields.String(required=True, description='Título'),
})

livro_response = api.model('LivroResponse', {
    'id': fields.String(required=True, description='ID do Livro'),
    'id_genero': fields.String(required=True, description='ID do Gênero'),
    'id_autor': fields.String(required=True, description='ID do Autor'),
    'foto': fields.String(required=True, description='Foto'),
    'sinopse': fields.String(required=True, description='Sinopse'),
    'estoque': fields.Integer(required=True, description='Estoque'),
    'preco': fields.Float(required=True, description='Preço'),
    'formato': fields.String(required=True, description='Formato'),
    'tipo': fields.String(required=True, description='Tipo'),
    'titulo': fields.String(required=True, description='Título'),
})

@api.route('/')
class LivroList(Resource):
    @api.marshal_list_with(livro_response)
    def get(self):
        return LivroController.listar_livros()[0]

    @jwt_required()
    @api.expect(livro_model)
    @api.response(201, 'Livro criado com sucesso!')
    def post(self):
        data = request.get_json()
        return LivroController.criar_livro(data)

@api.route('/<string:id>')
@api.param('id', 'ID do livro')
class LivroResource(Resource):
    @api.marshal_with(livro_response)
    def get(self, id):
        return LivroController.buscar_livro_por_id(id)[0]

    @jwt_required()
    @autorizacao_livro
    @api.expect(livro_model)
    def put(self, id):
        data = request.get_json()
        return LivroController.atualizar_livro(id, data)

    @jwt_required()
    @autorizacao_livro
    def delete(self, id):
        return LivroController.deletar_livro(id)
