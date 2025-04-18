import uuid
from flask_jwt_extended import get_jwt_identity
from backend.app.models.Pedido import Pedido
from backend.app.db.config import db

def listar_pedidos():
    id_usuario = get_jwt_identity()
    pedidos = Pedido.query.filter_by(id_usuario=id_usuario).all()
    return [p.to_dict() for p in pedidos], 200

def buscar_pedido_por_id(id_pedido):
    id_usuario = get_jwt_identity()
    pedido = Pedido.query.get(id_pedido)
    if not pedido:
        return {'mensagem': 'Pedido não encontrado.'}, 404
    if pedido.id_usuario != id_usuario:
        return {'mensagem': 'Acesso negado: este pedido não pertence a você.'}, 403
    return pedido.to_dict(), 200

def criar_pedido(data, id_usuario):
    campos_obrigatorios = ['id_endereco', 'total', 'data_compra', 'taxa_frete']
    faltando = [campo for campo in campos_obrigatorios if not data.get(campo)]
    if faltando:
        return {'mensagem': f'Campos obrigatórios ausentes: {", ".join(faltando)}'}, 400

    try:
        novo_pedido = Pedido(
            id=str(uuid.uuid4()),
            id_usuario=id_usuario,
            id_endereco=data.get('id_endereco'),
            id_pagamento=data.get('id_pagamento'),  # pode ser null
            total=data.get('total'),
            data_compra=data.get('data_compra'),
            taxa_frete=data.get('taxa_frete')
        )
        db.session.add(novo_pedido)
        db.session.commit()
        return {'mensagem': 'Pedido criado com sucesso!', 'pedido': novo_pedido.to_dict()}, 201
    except Exception as e:
        db.session.rollback()
        return {'mensagem': f'Erro ao criar pedido: {str(e)}'}, 500

def atualizar_pedido(id_pedido, data):
    id_usuario = get_jwt_identity()
    pedido = Pedido.query.get(id_pedido)
    if not pedido:
        return {'mensagem': 'Pedido não encontrado.'}, 404
    if pedido.id_usuario != id_usuario:
        return {'mensagem': 'Acesso negado: este pedido não pertence a você.'}, 403

    if not any(data.get(campo) is not None for campo in ['id_endereco', 'id_pagamento', 'total', 'data_compra', 'taxa_frete']):
        return {'mensagem': 'Nenhum dado fornecido para atualizar.'}, 400

    pedido.id_endereco = data.get('id_endereco', pedido.id_endereco)
    pedido.id_pagamento = data.get('id_pagamento', pedido.id_pagamento)
    pedido.total = data.get('total', pedido.total)
    pedido.data_compra = data.get('data_compra', pedido.data_compra)
    pedido.taxa_frete = data.get('taxa_frete', pedido.taxa_frete)

    db.session.commit()
    return {'mensagem': 'Pedido atualizado com sucesso!', 'pedido': pedido.to_dict()}, 200

def deletar_pedido(id_pedido):
    id_usuario = get_jwt_identity()
    pedido = Pedido.query.get(id_pedido)
    if not pedido:
        return {'mensagem': 'Pedido não encontrado.'}, 404
    if pedido.id_usuario != id_usuario:
        return {'mensagem': 'Acesso negado: este pedido não pertence a você.'}, 403

    db.session.delete(pedido)
    db.session.commit()
    return {'mensagem': 'Pedido deletado com sucesso!'}, 200