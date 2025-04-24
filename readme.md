 📚 Lumyk Backend

Este é o backend de um sistema de gestão de livros, autores, gêneros e pedidos feito com Flask, utilizando Flask-RESTx para documentação automática e JWT para autenticação. A aplicação utiliza SQLAlchemy como ORM e Flask-Migrate para controle de migrations.

 📥 Como Clonar o Repositório

Para clonar este projeto em sua máquina:
  
  ```bash
  git clone https://github.com/Karinyleandro/Lumyk---backend.git
  ```
Depois, acesse a pasta do projeto:

  ```bash
  cd Lumyk---backend
  ```

📦 Instalação

Clone o repositório (conforme instrução acima).
Navegue até a pasta do projeto.
Instale as dependências:

```bash
pip install -r C:\Users\karin\Lumyk---backend\requirements.txt
```

🚀 Rodando a Aplicação
Para iniciar a aplicação e acessar a documentação da API:
```bash
python run.py
```
Acesse no navegador:
```bash
http://127.0.0.1:5000/docs
```

Executar Seeders (Inserir Dados Iniciais)
Para popular as tabelas com os dados principais:
```bash
PYTHONPATH=backend python -m backend.app.db.seeders.seeder
```

Se tudo ocorrer bem, você verá:

  Autores inseridos com sucesso!
  Gêneros inseridos com sucesso!
  Livros inseridos com sucesso!
