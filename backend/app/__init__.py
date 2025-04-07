from flask import Flask
from app.db.database import db
from app.routes.livro_routes import livro_bp


# Modelos
from app.models.usuario import Usuario
from app.models.estado import Estado
from app.models.endereco import Endereco
from app.models.livro import Livro
from app.models.autor import Autor
from app.models.genero_livro import GeneroLivro
from app.models.pix import Pix
from app.models.pedido import Pedido
from app.models.carrinho import Carrinho
from app.models.item_carrinho import ItemCarrinho
from app.models.item_pedido import ItemPedido
from app.models.assinatura import Assinatura
