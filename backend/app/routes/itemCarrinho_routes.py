from flask_restx import Namespace, Resource, fields, marshal
from flask import request
from flask_jwt_extended import jwt_required
from backend.app.controllers import ItemCarrinhoController
from backend.app.middlewares.autorizacao_item_carrinho import autorizacao_carrinho

api = Namespace('item-carrinho', description='Operações relacionadas a Itens do Carrinho')

# Modelo de entrada (espera id_carrinho, id_livro, quantidade e preco_unitario)
item_model = api.model('ItemCarrinho', {
    'id_carrinho': fields.String(required=True, description='ID do carrinho'),
    'id_livro': fields.String(required=True, description='ID do livro'),
    'quantidade': fields.Integer(required=True, description='Quantidade do item'),
    'preco_unitario': fields.Float(required=True, description='Preço unitário do item'),
})

# Modelo de resposta com detalhes (inclui id, carrinho, livro, quantidade e preco_unitario)
item_response = api.clone('ItemCarrinhoResponse', item_model, {
    'id': fields.String(required=True, description='ID do item'),
    'livro': fields.Raw(description='Detalhes do livro'),
    'carrinho': fields.Raw(description='Detalhes do carrinho')
})

@api.route('/')
class AdicionarItem(Resource):
    @jwt_required()
    @api.expect(item_model)
    @api.response(201, 'Item adicionado com sucesso')
    @api.response(400, 'Estoque insuficiente ou dados inválidos')
    @api.response(404, 'Carrinho ou livro não encontrado')
    @autorizacao_carrinho
    def post(self):
        data = request.get_json()
        resposta, status = ItemCarrinhoController.adicionar_item_ao_carrinho(data)
        if status == 201:
            return marshal(resposta, item_response), 201
        return resposta, status

@api.route('/<string:id_item>')
@api.param('id_item', 'ID do item do carrinho')
class ItemCarrinhoResource(Resource):
    @jwt_required()
    @api.marshal_with(item_response)
    @api.response(404, 'Item do carrinho não encontrado')
    def get(self, id_item):
        resposta, status = ItemCarrinhoController.buscar_item_por_id(id_item)
        if status != 200:
            api.abort(status, resposta.get('mensagem'))
        return resposta

    @jwt_required()
    @api.expect(item_model)
    @api.marshal_with(item_response)
    @api.response(200, 'Item atualizado com sucesso!')
    @api.response(400, 'Dados inválidos')
    @api.response(404, 'Item, carrinho ou livro não encontrado')
    @autorizacao_carrinho
    def put(self, id_item):
        data = request.get_json()
        resposta, status = ItemCarrinhoController.atualizar_item_carrinho(id_item, data)
        if status != 200:
            api.abort(status, resposta.get('mensagem'))
        return resposta

    @jwt_required()
    @api.response(200, 'Item removido com sucesso!')
    @api.response(404, 'Item do carrinho não encontrado')
    @autorizacao_carrinho
    def delete(self, id_item):
        resposta, status = ItemCarrinhoController.deletar_item_do_carrinho(id_item)
        if status != 200:
            api.abort(status, resposta.get('mensagem'))
        return resposta

@api.route('/carrinho/<string:id_carrinho>')
@api.param('id_carrinho', 'ID do carrinho')
class ItensPorCarrinho(Resource):
    @jwt_required()
    @api.marshal_list_with(item_response)
    def get(self, id_carrinho):
        resposta, status = ItemCarrinhoController.listar_itens_do_carrinho(id_carrinho)
        if status != 200:
            api.abort(status, "Erro ao listar itens do carrinho")
        return resposta

@api.route('/todos')
class TodosItens(Resource):
    @jwt_required()
    @api.marshal_list_with(item_response)
    def get(self):
        resposta, status = ItemCarrinhoController.listar_todos_itens()
        if status != 200:
            api.abort(status, "Erro ao listar todos os itens do carrinho")
        return resposta
