from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import jsonify
from backend.app.models.Livro import Livro

def autorizacao_livro(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        id = kwargs.get('id')
        livro = Livro.query.get(id)
        if not livro:
            return {'mensagem': 'Livro não encontrado.'}, 404

        # Aqui, a parte da autorização depende da lógica nao sei se quero manter nao
        # usuario_id = get_jwt_identity()
        # if livro.id_usuario != usuario_id:
        #     return {'mensagem': 'Você não tem permissão para acessar este livro.'}, 403

        return func(*args, **kwargs)
    
    return wrapper

