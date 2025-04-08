from flask import Flask
from app.db.database import db
from app.routes.livro_routes import livro_bp


# Modelos
from app.db.migrations.estado import Estado
from app.db.migrations.usuario import Usuario
from app.db.migrations.endereco import Endereco
from app.db.migrations.pagamento import Pagamento
from app.db.migrations.pedido import Pedido
from app.db.migrations.carrinho import Carrinho
from app.db.migrations.assinatura import Assinatura
from app.db.migrations.genero_livro import GeneroLivro
from app.db.migrations.autor import Autor
from app.db.migrations.livro import Livro
from app.db.migrations.item_carrinho import ItemCarrinho  
from app.db.migrations.item_pedido import ItemPedido  #testes