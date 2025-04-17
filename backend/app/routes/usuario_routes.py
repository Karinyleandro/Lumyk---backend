<<<<<<< HEAD
from flask import Blueprint, request, jsonify
=======
# EU COLOQUEI TODO COMITADO PORQUE É SÓ UM EXEMPLO QUE NAO TÁ SEGUINDO 100% COMO DEVE SER CRIADO USUARIO, SE QUISER VER PARA ENTENDER

''' from flask_restx import Namespace, Resource, fields
>>>>>>> feature/kariny
from backend.app.db.config import db
from backend.app.models.Usuario import Usuario
from datetime import datetime

api = Namespace('usuarios', description='Operações relacionadas a usuários')

# Modelo de entrada (para POST e PUT)
usuario_input = api.model('UsuarioInput', {
    'nome': fields.String(required=True),
    'email': fields.String(required=True),
    'senha': fields.String(required=True),
    'data_nascimento': fields.String(required=True, description='Formato: YYYY-MM-DD')
})

# Modelo de saída (para GET)
usuario_output = api.inherit('UsuarioOutput', usuario_input, {
    'id': fields.String(readOnly=True)
})

@api.route('/')
class UsuarioList(Resource):
    @api.marshal_list_with(usuario_output)
    def get(self):
        """Lista todos os usuários"""
        return Usuario.query.all()

    @api.expect(usuario_input)
    def post(self):
        """Cria um novo usuário"""
        data = api.payload
        usuario = Usuario(
            nome=data['nome'],
            email=data['email'],
            senha=data['senha'],
            data_nascimento=datetime.strptime(data['data_nascimento'], '%Y-%m-%d')
        )
        db.session.add(usuario)
        db.session.commit()
        return {'mensagem': 'Usuário criado com sucesso!'}, 201


@api.route('/<string:id>')
@api.param('id', 'ID do usuário')
class UsuarioDetail(Resource):
    @api.expect(usuario_input)
    def put(self, id):
        """Atualiza um usuário existente"""
        usuario = Usuario.query.get_or_404(id)
        data = api.payload
        usuario.nome = data.get('nome', usuario.nome)
        usuario.email = data.get('email', usuario.email)
        usuario.senha = data.get('senha', usuario.senha)

        if 'data_nascimento' in data:
            usuario.data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d')

        db.session.commit()
        return {'mensagem': 'Usuário atualizado com sucesso!'}

    def delete(self, id):
        """Remove um usuário"""
        usuario = Usuario.query.get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return {'mensagem': 'Usuário deletado com sucesso!'} '''
