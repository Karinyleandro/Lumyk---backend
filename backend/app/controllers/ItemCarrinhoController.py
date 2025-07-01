import uuid
from backend.app.models.ItemCarrinho import ItemCarrinho
from backend.app.models.Carrinho import Carrinho
from backend.app.models.Livro import Livro
from backend.app.db.config import db

class ItemCarrinhoController:

    @staticmethod
    def listar_itens_do_carrinho(id_carrinho):
        itens = ItemCarrinho.query.filter_by(id_carrinho=id_carrinho).all()
        return [item.to_dict(incluir_detalhes=True) for item in itens], 200
    
    @staticmethod
    def listar_todos_itens():
        itens = ItemCarrinho.query.all()
        return [item.to_dict(incluir_detalhes=True) for item in itens], 200

    @staticmethod
    def buscar_item_por_id(id_item):
        item = ItemCarrinho.query.get(id_item)
        if not item:
            return {'mensagem': 'Item do carrinho não encontrado'}, 404
        return item.to_dict(incluir_detalhes=True), 200

    @staticmethod

    def adicionar_item_ao_carrinho(data):
        id_carrinho = data.get('id_carrinho')
        id_livro = data.get('id_livro')
        quantidade = data.get('quantidade')
        preco_unitario = data.get('preco_unitario')
        formato = data.get('formato') 
        tipo = data.get('tipo')  

        carrinho = Carrinho.query.get(id_carrinho)
        livro = Livro.query.get(id_livro)

        if not carrinho or not livro:
            return {'mensagem': 'Carrinho ou livro não encontrado'}, 404
        
        if quantidade is None or not isinstance(quantidade, int) or quantidade <= 0:
            return {'mensagem': 'Quantidade inválida. Deve ser um número inteiro maior que zero.'}, 400

        if livro.estoque < quantidade:
            return {'mensagem': f'Quantidade solicitada ({quantidade}) excede o estoque disponível ({livro.estoque})'}, 400

        livro.estoque -= quantidade
        db.session.add(livro)

        novo_item = ItemCarrinho(
            id=str(uuid.uuid4()),
            id_carrinho=id_carrinho,
            id_livro=id_livro,
            quantidade=quantidade,
            preco_unitario=preco_unitario,
            formato=formato,  
            tipo=tipo  
        )

        db.session.add(novo_item)
        db.session.commit()

        # Recarregar para garantir dados atualizados
        db.session.refresh(novo_item)
        db.session.refresh(livro)

        item_dict = novo_item.to_dict(incluir_detalhes=True)
        item_dict['livro']['estoque'] = livro.estoque  # Atualiza estoque na resposta

        return item_dict, 201

    @staticmethod
    def deletar_item_do_carrinho(id_item):
        item = ItemCarrinho.query.get(id_item)
        if not item:
            return {'mensagem': 'Item do carrinho não encontrado'}, 404

        item_dict = item.to_dict(incluir_detalhes=True)
        db.session.delete(item)
        db.session.commit()

        return {
            'mensagem': 'Item removido com sucesso!',
            'item': item_dict
        }, 200
 
    @staticmethod
   
    @staticmethod
    def atualizar_item_carrinho(id_item, data):
        if not isinstance(data, dict):
            data = data.__dict__ if hasattr(data, '__dict__') else {}

        item = ItemCarrinho.query.get(id_item)
        if not item:
            return {'mensagem': 'Item do carrinho não encontrado'}, 404

        novo_id_livro = data.get('id_livro')
        novo_id_carrinho = data.get('id_carrinho')
        nova_quantidade = data.get('quantidade')
        novo_preco = data.get('preco_unitario')
        novo_formato = data.get('formato')
        novo_tipo = data.get('tipo')

        if novo_id_carrinho:
            carrinho = Carrinho.query.get(str(novo_id_carrinho))
            if not carrinho:
                return {'mensagem': 'Carrinho não encontrado'}, 404
            item.id_carrinho = str(novo_id_carrinho)

        livro_atual = Livro.query.get(item.id_livro)

        if novo_id_livro and novo_id_livro != item.id_livro:
            livro_novo = Livro.query.get(str(novo_id_livro))
            if not livro_novo:
                return {'mensagem': 'Livro novo não encontrado'}, 404

            if livro_atual:
                livro_atual.estoque += item.quantidade
                db.session.add(livro_atual)

            # Se quantidade não foi passada, mantém a atual
            if nova_quantidade is None:
                nova_quantidade = item.quantidade  

            if nova_quantidade > livro_novo.estoque:
                return {'mensagem': f'Quantidade solicitada ({nova_quantidade}) excede o estoque disponível ({livro_novo.estoque})'}, 400

            # Deduz estoque do livro novo
            livro_novo.estoque -= nova_quantidade
            db.session.add(livro_novo)

            item.id_livro = str(novo_id_livro)

        elif nova_quantidade is not None:
            if not isinstance(nova_quantidade, int) or nova_quantidade <= 0:
                return {'mensagem': 'Quantidade inválida. Deve ser um número inteiro maior que zero.'}, 400

            if livro_atual:
                estoque_disponivel = livro_atual.estoque + item.quantidade
                if nova_quantidade > estoque_disponivel:
                    return {'mensagem': f'Quantidade solicitada ({nova_quantidade}) excede o estoque disponível ({estoque_disponivel})'}, 400

                livro_atual.estoque = estoque_disponivel - nova_quantidade
                db.session.add(livro_atual)

        if nova_quantidade is not None:
            item.quantidade = nova_quantidade

        if novo_preco is not None:
            item.preco_unitario = novo_preco

        if novo_formato is not None:
            item.formato = novo_formato

        if novo_tipo is not None:
            item.tipo = novo_tipo

        db.session.commit()

        return item.to_dict(incluir_detalhes=True), 200