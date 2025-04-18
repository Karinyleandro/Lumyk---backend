from backend.app.models.Livro import Livro
from backend.app.db.config import db
import uuid

def listar_livros():
    livros = Livro.query.all()
    return [livro.to_dict() for livro in livros], 200

def buscar_livro_por_id(id):
    livro = Livro.query.get_or_404(id)
    return livro.to_dict(), 200

def criar_livro(data):
    novo_livro = Livro(
        id=str(uuid.uuid4()),
        id_genero=data['id_genero'],
        id_autor=data['id_autor'],
        foto=data['foto'],
        sinopse=data['sinopse'],
        estoque=data['estoque'],
        preco=data['preco'],
        formato=data['formato'],
        tipo=data['tipo'],
        titulo=data['titulo']
    )
    db.session.add(novo_livro)
    db.session.commit()
    return {'mensagem': 'Livro criado com sucesso!', 'livro': novo_livro.to_dict()}, 201

def atualizar_livro(id, data):
    livro = Livro.query.get_or_404(id)

    livro.id_genero = data.get('id_genero', livro.id_genero)
    livro.id_autor = data.get('id_autor', livro.id_autor)
    livro.foto = data.get('foto', livro.foto)
    livro.sinopse = data.get('sinopse', livro.sinopse)
    livro.estoque = data.get('estoque', livro.estoque)
    livro.preco = data.get('preco', livro.preco)
    livro.formato = data.get('formato', livro.formato)
    livro.tipo = data.get('tipo', livro.tipo)
    livro.titulo = data.get('titulo', livro.titulo)

    db.session.commit()
    return {'mensagem': 'Livro atualizado com sucesso!', 'livro': livro.to_dict()}, 200

def deletar_livro(id):
    livro = Livro.query.get_or_404(id)
    db.session.delete(livro)
    db.session.commit()
    return {'mensagem': 'Livro deletado com sucesso!'}, 200
