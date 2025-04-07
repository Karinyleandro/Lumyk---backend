from flask import Blueprint, request, jsonify
from app.db.database import db
from app.models.livro import Livro

livro_bp = Blueprint('livro_bp', __name__)

@livro_bp.route('/livros', methods=['POST'])
def criar_livro():
    data = request.json
    livro = Livro(**data)
    db.session.add(livro)
    db.session.commit()
    return jsonify({'mensagem': 'Livro criado com sucesso!'}), 201

@livro_bp.route('/livros', methods=['GET'])
def listar_livros():
    livros = Livro.query.all()
    return jsonify([{
        'id': l.id,
        'titulo': l.titulo,
        'preco': l.preco
    } for l in livros])

@livro_bp.route('/livros/<int:id>', methods=['GET'])
def obter_livro(id):
    livro = Livro.query.get_or_404(id)
    return jsonify({
        'id': livro.id,
        'titulo': livro.titulo,
        'preco': livro.preco,
        'estoque': livro.estoque
    })

@livro_bp.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    livro = Livro.query.get_or_404(id)
    data = request.json
    for key, value in data.items():
        setattr(livro, key, value)
    db.session.commit()
    return jsonify({'mensagem': 'Livro atualizado com sucesso!'})

@livro_bp.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    livro = Livro.query.get_or_404(id)
    db.session.delete(livro)
    db.session.commit()
    return jsonify({'mensagem': 'Livro deletado com sucesso!'})
