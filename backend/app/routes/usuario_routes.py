from flask import Blueprint, request, jsonify
from app.db.database import db
from app.models.Usuario import Usuario
from datetime import datetime

usuario_bp = Blueprint('usuario_bp', __name__)

@usuario_bp.route('/usuarios', methods=['POST'])
def criar_usuario():
    data = request.json
    usuario = Usuario(
        nome=data['nome'],
        email=data['email'],
        senha=data['senha'],
        data_nascimento=datetime.strptime(data['data_nascimento'], '%Y-%m-%d')
    )
    db.session.add(usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário criado com sucesso!'}), 201

@usuario_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return jsonify([
        {
            'id': u.id,
            'nome': u.nome,
            'email': u.email,
            'data_nascimento': u.data_nascimento.strftime('%Y-%m-%d')
        } for u in usuarios
    ])

@usuario_bp.route('/usuarios/<string:id>', methods=['PUT'])
def atualizar_usuario(id):
    data = request.json
    usuario = Usuario.query.get_or_404(id)

    usuario.nome = data.get('nome', usuario.nome)
    usuario.email = data.get('email', usuario.email)
    usuario.senha = data.get('senha', usuario.senha)

    if 'data_nascimento' in data:
        usuario.data_nascimento = datetime.strptime(data['data_nascimento'], '%Y-%m-%d')

    db.session.commit()
    return jsonify({'mensagem': 'Usuário atualizado com sucesso!'})

@usuario_bp.route('/usuarios/<string:id>', methods=['DELETE'])
def deletar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'mensagem': 'Usuário deletado com sucesso!'})
