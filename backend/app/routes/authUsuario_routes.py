from flask_restx import Namespace, Resource, fields
from flask import request
from backend.app.controllers import authUsuario  # seu controller com registrar_usuario e login

api = Namespace('auth', description='Gerenciamento de autenticação (registro e login)')

# Modelo para a entrada do registro
registro_input = api.model('RegistroInput', {
    'nome': fields.String(required=True, description='Nome do usuário'),
    'email': fields.String(required=True, description='Email do usuário'),
    'senha': fields.String(required=True, description='Senha do usuário'),
    'data_nascimento': fields.String(
        required=True,
        description='Data de nascimento no formato YYYY-MM-DD'
    )
})

# Modelo para a entrada do login
login_input = api.model('LoginInput', {
    'email': fields.String(required=True, description='Email do usuário'),
    'senha': fields.String(required=True, description='Senha do usuário')
})

@api.route('/registro')
class Registro(Resource):
    @api.expect(registro_input)
    @api.doc(description="Registrar um novo usuário")
    def post(self):
        data = request.json
        return authUsuario.registrar_usuario(data)

@api.route('/login')
class Login(Resource):
    @api.expect(login_input)
    @api.doc(description="Realizar login e obter token JWT")
    def post(self):
        data = request.json
        return authUsuario.login(data)
