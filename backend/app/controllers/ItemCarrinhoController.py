'''
from backend.app.models.ItemCarrinho import ItemCarrinho
from backend.app.db.config import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend.app.models.Carrinho import Carrinho
import uuid

def listar_item_carrinho(id_carrinho, id_usuario):
    carrinho = Carrinho.query.get(id_carrinho)
    
    if not carrinho or carrinho.id_usuario != id_usuario:
        return {'mensagem': 'Carrinho não encontrado ou não pertence a você'}, 404
    
    itens = ItemCarrinho.query.filter_by(id_carrinho = id_carrinho).all()
    
    return [item.to_dict() for item in itens],200

def criar_item_carrinho(id_usuario, data):
    id_livro = data.get('id_livro')
    id_carrinho = data.get('id_carinho')
    
    if not id_carrinho or not id_livro:
        return {'Mensagem': 'O ID do livros e o ID do carrinho são necessários'}
   
    ItemCarrinho = Carrinho.query.get(id_carrinho)
    
    if not ItemCarrinho or ItemCarrinho.id_usuario != id_usuario:
        return {'mensagem': 'Carrinho não encontrado ou não pertence a você'}, 404
    
    novo_produto = ItemCarrinho(
        id = str(uuid.uuid4()), 
        id_carrinho = id_carrinho,
        id_livro = id_livro
    )
    
    db.session.add(novo_produto)
    db.session.commit()
    return {'mensagem': 'Item carrinho criado com sucesso!', 'carrinho': novo_produto.to_dict()}, 201

@jwt_required()
def buscar_item_por_id(id_usuario, id_item):
    item = ItemCarrinho.query.get(id_item)
    if not item:
        return {'mensagem': 'Item não encontrado.'}, 404

    carrinho = Carrinho.query.get(item.id_carrinho)
    if not carrinho or carrinho.id_usuario != id_usuario:
        return {'mensagem': 'Permissão negada para acessar este item.'}, 403

    return item.to_dict(),200

@jwt_required()
def atualizar_item_carrinho(id_usuario, id_item, data):
    item = ItemCarrinho.query.get(id_item)
    
    if not item:
        return {'mensagem': 'Item não encontrado.'}, 404
    
    carrinho = Carrinho.query.get(item.id_carrinho)
    if not carrinho or carrinho.id_usuario != id_usuario:
        return {'mensagem': 'Permissão negada para acessar este item.'}, 403
    
    novo_id_carrinho = data.get('id_carrinho')
    novo_id_livro = data.get('id_livro')
    
    if novo_id_carrinho
'''