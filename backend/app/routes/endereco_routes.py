from flask_restx import Namespace, Resource, fields
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.app.controllers import EnderecoController
from backend.app.models.Endereco import Endereco

api = Namespace('enderecos', description='Operações relacionadas a Endereços')

endereco_model = api.model('Endereco', {
    'id_usuario': fields.String(required=True, description='ID do Usuário'),
    'id_estado': fields.String(required=True, description='ID do Estado'),
    'numero': fields.Integer(required=True, description='Número'),
    'bairro': fields.String(required=True, description='Bairro'),
    'rua': fields.String(required=True, description='Rua'),
})

endereco_response = api.model('EnderecoResponse', {
    'id': fields.String(required=True, description='ID do Endereço'),
    'id_usuario': fields.String(required=True, description='ID do Usuário'),
    'id_estado': fields.String(required=True, description='ID do Estado'),
    'numero': fields.Integer(required=True, description='Número'),
    'bairro': fields.String(required=True, description='Bairro'),
    'rua': fields.String(required=True, description='Rua'),
})

@api.route('/')
class EnderecoList(Resource):
    @api.marshal_list_with(endereco_response)
    def get(self):
        return EnderecoController.listar_enderecos()[0]

    @api.expect(endereco_model)
    @api.doc(security='Bearer Auth')
    @jwt_required()
    @api.response(201, 'Endereço criado com sucesso!')
    def post(self):
        data = request.get_json()
        return EnderecoController.criar_endereco(data)

@api.route('/<string:id>')
@api.param('id', 'ID do endereço')
class EnderecoResource(Resource):
    @api.marshal_with(endereco_response)
    def get(self, id):
        return EnderecoController.buscar_endereco_por_id(id)[0]

    @api.expect(endereco_model)
    @api.doc(security='Bearer Auth')
    @jwt_required()
    @api.response(200, 'Endereço atualizado com sucesso!')
    def put(self, id):
        endereco = Endereco.query.get_or_404(id)
        if endereco.id_usuario != get_jwt_identity():
            return {'mensagem': 'Você não tem permissão para alterar este endereço.'}, 403
        data = request.get_json()
        return EnderecoController.atualizar_endereco(id, data)

    @api.doc(security='Bearer Auth')
    @jwt_required()
    @api.response(200, 'Endereço deletado com sucesso!')
    def delete(self, id):
        endereco = Endereco.query.get_or_404(id)
        if endereco.id_usuario != get_jwt_identity():
            return {'mensagem': 'Você não tem permissão para deletar este endereço.'}, 403
        return EnderecoController.deletar_endereco(id)
