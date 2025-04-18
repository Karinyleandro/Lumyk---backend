from flask_restx import Namespace, Resource, fields
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.app.controllers import PedidoController
from backend.app.middlewares.autorizacao_pedido import autorizacao_pedido

api = Namespace('pedidos', description='Operações relacionadas a pedidos')

pedido_model = api.model('Pedido', {
    'id_endereco': fields.String(required=True),
    'id_pagamento': fields.String(required=False),
    'total': fields.Float(required=True),
    'data_compra': fields.String(required=True, description='Data no formato YYYY-MM-DD'),
    'taxa_frete': fields.Float(required=True),
})

pedido_response = api.clone('PedidoResponse', pedido_model, {
    'id': fields.String(required=True),
    'id_usuario': fields.String(required=True)
})

@api.route('/')
class PedidoList(Resource):
    @jwt_required()
    @api.marshal_list_with(pedido_response)
    def get(self):
        return PedidoController.listar_pedidos()[0]

    @jwt_required()
    @api.expect(pedido_model)
    def post(self):
        data = request.get_json()
        id_usuario = get_jwt_identity()
        return PedidoController.criar_pedido(data, id_usuario)

@api.route('/<string:id_pedido>')
@api.param('id_pedido', 'ID do pedido')
class PedidoResource(Resource):
    @jwt_required()
    @autorizacao_pedido
    @api.marshal_with(pedido_response)
    def get(self, id_pedido):
        return PedidoController.buscar_pedido_por_id(id_pedido)[0]

    @jwt_required()
    @autorizacao_pedido
    @api.expect(pedido_model)
    def put(self, id_pedido):
        data = request.get_json()
        return PedidoController.atualizar_pedido(id_pedido, data)

    @jwt_required()
    @autorizacao_pedido
    def delete(self, id_pedido):
        return PedidoController.deletar_pedido(id_pedido)