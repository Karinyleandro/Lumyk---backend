from flask import request
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required
from backend.app.controllers.ItemPedidoController import ItemPedidoController
from backend.app.middlewares.autorizacao_pedido import autorizacao_pedido

api = Namespace('item-pedido', description='Operações relacionadas aos itens de pedido')

item_pedido_model = api.model('ItemPedido', {
    'id': fields.String(readonly=True),
    'id_pedido': fields.String(required=True),
    'id_livro': fields.String(required=True),
    'preco_unitario': fields.Float(required=True),
    'quantidade': fields.Integer(required=True),
})

@api.route('/<string:id_item>')
class ItemPedidoResource(Resource):
    @jwt_required()
    def get(self, id_item):
        return ItemPedidoController.buscar_item_por_id(id_item)

    @jwt_required()
    def delete(self, id_item):
        return ItemPedidoController.deletar_item_do_pedido(id_item)

    @jwt_required()
    @api.expect(item_pedido_model)
    def put(self, id_item):
        data = request.get_json()
        return ItemPedidoController.atualizar_item_pedido(id_item, data)

@api.route('/pedido/<string:id_pedido>')
class ItensDoPedidoResource(Resource):
    @jwt_required()
    @autorizacao_pedido
    def get(self, id_pedido):
        return ItemPedidoController.listar_itens_do_pedido(id_pedido)

@api.route('/')
class ItemPedidoListaResource(Resource):
    @jwt_required()
    @api.expect(item_pedido_model)
    def post(self):
        data = request.get_json()
        return ItemPedidoController.adicionar_item_ao_pedido(data)
