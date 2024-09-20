
# API de E-commerce

Este projeto é uma API de e-commerce desenvolvida como parte de um mini curso de **Python** oferecido pela **Rocketseat**. A API permite a criação e gerenciamento de produtos, carrinho de compras e autenticação de usuários.

## Funcionalidades

- **Autenticação de Usuários**: Login e logout de usuários usando tokens de sessão.
- **Gerenciamento de Produtos**: Adicionar, visualizar, atualizar e excluir produtos.
- **Carrinho de Compras**: Adicionar e remover produtos do carrinho, além de realizar o checkout.
- **Listagem de Produtos**: Exibir todos os produtos cadastrados.

## Tecnologias Utilizadas

- **Flask**: Microframework para construção de APIs.
- **Flask-Login**: Gerenciamento de sessões e autenticação de usuários.
- **Flask-CORS**: Habilitação de Cross-Origin Resource Sharing (CORS).
- **Flask-SQLAlchemy**: ORM para interagir com o banco de dados.
- **SQLite**: Banco de dados utilizado para armazenar informações de usuários, produtos e itens do carrinho.

## Instalação e Execução

1. Clone este repositório:
    ```bash
    git clone https://github.com/italorafaeltavares/FlaskShop.git
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute a aplicação:
    ```bash
    python app.py
    ```

## Endpoints

### Autenticação
- **`POST /login`**: Autentica um usuário.
- **`POST /logout`**: Faz logout do usuário autenticado.

### Produtos
- **`POST /api/products/add`**: Adiciona um novo produto.
- **`GET /api/products/<product_id>`**: Retorna os detalhes de um produto.
- **`PUT /api/products/update/<product_id>`**: Atualiza um produto.
- **`DELETE /api/products/delete/<product_id>`**: Remove um produto.
- **`GET /api/products`**: Retorna a lista de todos os produtos.

### Carrinho de Compras
- **`POST /api/cart/add/<product_id>`**: Adiciona um produto ao carrinho.
- **`DELETE /api/cart/remove/<product_id>`**: Remove um produto do carrinho.
- **`GET /api/cart`**: Retorna o conteúdo do carrinho.
- **`POST /api/cart/checkout`**: Realiza o checkout e limpa o carrinho.

## Estrutura do Banco de Dados

- **User**: Armazena as informações de usuários (ID, nome de usuário, senha).
- **Product**: Armazena os produtos cadastrados (ID, nome, preço, descrição).
- **CartItem**: Relaciona usuários e produtos adicionados ao carrinho (ID, ID do usuário, ID do produto).

## Exemplo de Requisição

### Login
```bash
curl -X POST http://localhost:5000/login -H "Content-Type: application/json" -d '{"username": "user", "password": "pass"}'
```

### Adicionar Produto
```bash
curl -X POST http://localhost:5000/api/products/add -H "Content-Type: application/json" -d '{"name": "Product1", "price": 100, "description": "Description1"}'
```

## Contribuição

Sinta-se à vontade para enviar PRs e contribuir com melhorias e novas funcionalidades.

## Licença

Este projeto está licenciado sob a licença MIT.
