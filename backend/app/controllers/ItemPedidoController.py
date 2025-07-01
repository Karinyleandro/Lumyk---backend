import uuid
from backend.app.models.ItemPedido import ItemPedido
from backend.app.models.Pedido import Pedido
from backend.app.models.Livro import Livro
from backend.app.db.config import db

class ItemPedidoController:
    
    @staticmethod
    def listar_todos_itens():
        itens = ItemPedido.query.all()
        return [item.to_dict() for item in itens], 200

    @staticmethod
    def listar_itens_do_pedido(id_pedido):
        itens = ItemPedido.query.filter_by(id_pedido=id_pedido).all()
        return [item.to_dict() for item in itens], 200

    @staticmethod
    def buscar_item_por_id(id_item):
        item = ItemPedido.query.get(id_item)
        if not item:
            return {'mensagem': 'Item do pedido não encontrado'}, 404
        return item.to_dict(), 200

    @staticmethod
    def adicionar_item_ao_pedido(data):
        id_pedido = data.get('id_pedido')
        id_livro = data.get('id_livro')
        preco_unitario = data.get('preco_unitario')
        quantidade = data.get('quantidade')
        formato = data.get('formato')
        tipo = data.get('tipo')

        pedido = Pedido.query.get(id_pedido)
        livro = Livro.query.get(id_livro)

        if not pedido or not livro:
            return {'mensagem': 'Pedido ou livro não encontrado'}, 404
        
        if quantidade is None or not isinstance(quantidade, int) or quantidade <= 0:
            return {'mensagem': 'Quantidade inválida. Deve ser um número inteiro maior que zero.'}, 400

        if livro.estoque < quantidade:
            return {'mensagem': f'Quantidade solicitada ({quantidade}) excede o estoque disponível ({livro.estoque})'}, 400

        novo_item = ItemPedido(
            id=str(uuid.uuid4()),
            id_pedido=id_pedido,
            id_livro=id_livro,
            preco_unitario=preco_unitario,
            quantidade=quantidade,
            formato=formato,
            tipo=tipo
        )

        db.session.add(novo_item)
        
        livro.estoque -= quantidade
         
        db.session.commit()

        return novo_item.to_dict(), 201

    @staticmethod
    def deletar_item_do_pedido(id_item):
        item = ItemPedido.query.get(id_item)
        if not item:
            return {'mensagem': 'Item do pedido não encontrado'}, 404

        item_dict = item.to_dict()
        db.session.delete(item)
        db.session.commit()

        return {'mensagem': 'Item removido com sucesso!', 'item': item_dict}, 200

    @staticmethod
    
    def atualizar_item_pedido(id_item, data):
        if not isinstance(data, dict):
            data = data.__dict__ if hasattr(data, '__dict__') else {}

        item = ItemPedido.query.get(id_item)
        if not item:
            return {'mensagem': 'Item do pedido não encontrado'}, 404

        novo_id_pedido = data.get('id_pedido')
        novo_id_livro = data.get('id_livro')
        preco_unitario = data.get('preco_unitario')
        quantidade = data.get('quantidade')
        formato = data.get('formato')
        tipo = data.get('tipo')

        if novo_id_pedido:
            pedido = Pedido.query.get(str(novo_id_pedido))
            if not pedido:
                return {'mensagem': 'Pedido não encontrado'}, 404
            item.id_pedido = str(novo_id_pedido)

        livro_atual = Livro.query.get(item.id_livro)

        if novo_id_livro and novo_id_livro != item.id_livro:
            livro_novo = Livro.query.get(str(novo_id_livro))
            if not livro_novo:
                return {'mensagem': 'Novo livro não encontrado'}, 404

            if livro_atual:
                livro_atual.estoque += item.quantidade

            if quantidade is None:
                quantidade = item.quantidade  

            if quantidade > livro_novo.estoque:
                return {'mensagem': f'Quantidade solicitada ({quantidade}) excede o estoque disponível ({livro_novo.estoque})'}, 400

            livro_novo.estoque -= quantidade
            item.id_livro = str(novo_id_livro)

        elif quantidade is not None:
            if not isinstance(quantidade, int) or quantidade <= 0:
                return {'mensagem': 'Quantidade inválida. Deve ser um número inteiro maior que zero.'}, 400

            if livro_atual:
                estoque_disponivel = livro_atual.estoque + item.quantidade
                if quantidade > estoque_disponivel:
                    return {'mensagem': f'Quantidade solicitada ({quantidade}) excede o estoque disponível ({estoque_disponivel})'}, 400

                livro_atual.estoque = estoque_disponivel - quantidade

        if quantidade is not None:
            item.quantidade = quantidade

        if preco_unitario is not None:
            item.preco_unitario = preco_unitario

        if formato is not None:
            item.formato = formato

        if tipo is not None:
            item.tipo = tipo

        db.session.commit()

        return item.to_dict(), 200
