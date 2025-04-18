from flask_restx import Namespace, Resource, fields
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.app.controllers import CarrinhoController

api = Namespace('carrinhos', description='Operações relacionadas a Carrinhos')

# Modelo de entrada (sem ID)
carrinho_model = api.model('Carrinho', {
    'data_criacao': fields.String(required=True, description='Data de criação no formato YYYY-MM-DD'),
})

# Modelo de resposta (com ID e ID do usuário)
carrinho_response = api.clone('CarrinhoResponse', carrinho_model, {
    'id': fields.String(required=True, description='ID do carrinho'),
    'id_usuario': fields.String(required=True, description='ID do usuário dono do carrinho'),
})

@api.route('/')
class CarrinhoList(Resource):
    @jwt_required()
    @api.marshal_list_with(carrinho_response)
    def get(self):
        id_usuario = get_jwt_identity()
        return CarrinhoController.listar_carrinhos(id_usuario)[0]

    @jwt_required()
    @api.expect(carrinho_model)
    @api.response(201, 'Carrinho criado com sucesso!')
    def post(self):
        id_usuario = get_jwt_identity()
        data = request.get_json()
        return CarrinhoController.criar_carrinho(id_usuario, data)

@api.route('/<string:id_carrinho>')
@api.param('id_carrinho', 'ID do carrinho')
class CarrinhoResource(Resource):
    @jwt_required()
    @api.marshal_with(carrinho_response)
    def get(self, id_carrinho):
        id_usuario = get_jwt_identity()
        return CarrinhoController.buscar_por_id(id_usuario, id_carrinho)[0]

    @jwt_required()
    @api.expect(carrinho_model)
    @api.response(200, 'Carrinho atualizado com sucesso!')
    def put(self, id_carrinho):
        id_usuario = get_jwt_identity()
        data = request.get_json()
        return CarrinhoController.atualizar_carrinho(id_carrinho, id_usuario, data)

    @jwt_required()
    @api.response(200, 'Carrinho deletado com sucesso!')
    def delete(self, id_carrinho):
        id_usuario = get_jwt_identity()
        return CarrinhoController.deletar_carrinho(id_carrinho, id_usuario)