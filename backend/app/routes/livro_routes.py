from flask_restx import Namespace, Resource, fields
from flask import request
from backend.app.controllers import LivroController
from backend.app.middlewares.autorizacao_livro import autorizacao_livro
from flask_jwt_extended import jwt_required

api = Namespace('livros', description='Operações relacionadas a Livros')

# Models de relacionamento
autor_model = api.model('AutorInput', {
    'nome': fields.String(required=True, description='Nome do Autor'),
    'biografia': fields.String(required=True, description='Biografia do Autor'),
    'foto': fields.String(required=True, description='URL da foto do Autor')
})

genero_model = api.model('Genero', {
    'id': fields.String(description='ID do Gênero'),
    'nome': fields.String(description='Nome do Gênero'),
})

# Model de entrada
livro_model = api.model('Livro', {
    'id_genero': fields.String(required=True, description='ID do Gênero'),
    'id_autor': fields.String(required=True, description='ID do Autor'),
    'foto': fields.String(required=True, description='Foto do Livro'),
    'sinopse': fields.String(required=True, description='Sinopse do Livro'),
    'estoque': fields.Integer(required=True, description='Quantidade em Estoque'),
    'preco': fields.Float(required=True, description='Preço do Livro'),
    'formato': fields.String(required=True, description='Formato do Livro'),
    'tipo': fields.String(required=True, description='Tipo do Livro'),
    'titulo': fields.String(required=True, description='Título do Livro'),
})

# Model de resposta
livro_response = api.model('LivroResponse', {
    'id': fields.String(description='ID do Livro'),
    'id_genero': fields.String(description='ID do Gênero'),
    'genero': fields.Nested(genero_model, description='Informações do Gênero'),
    'id_autor': fields.String(description='ID do Autor'),
    'autor': fields.Nested(autor_model, description='Informações do Autor'),
    'foto': fields.String(description='Foto do Livro'),
    'sinopse': fields.String(description='Sinopse do Livro'),
    'estoque': fields.Integer(description='Quantidade em Estoque'),
    'preco': fields.Float(description='Preço do Livro'),
    'formato': fields.String(description='Formato do Livro'),
    'tipo': fields.String(description='Tipo do Livro'),
    'titulo': fields.String(description='Título do Livro'),
})

# Rotas
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
    @api.response(200, 'Livro atualizado com sucesso!')
    def put(self, id):
        data = request.get_json()
        return LivroController.atualizar_livro(id, data)

    @jwt_required()
    @autorizacao_livro
    @api.response(200, 'Livro deletado com sucesso!')
    def delete(self, id):
        return LivroController.deletar_livro(id)
