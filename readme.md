
# Projeto Flask - Gerenciamento de Usuários e Refeições

Este projeto é uma aplicação Flask que implementa um sistema de gerenciamento de usuários e refeições, utilizando autenticação com `flask-login` e banco de dados SQLAlchemy.

## Funcionalidades

- **Gerenciamento de Usuários:**
  - Criação de usuários.
  - Login e autenticação.
  - Logout seguro.

- **Gerenciamento de Refeições:**
  - Criação, listagem, visualização, edição e exclusão de refeições associadas a um usuário autenticado.

## Configuração e Execução

1. **Instalar dependências:**
   Certifique-se de que todas as dependências necessárias estão instaladas, como `Flask`, `Flask-Login` e `SQLAlchemy`.

2. **Configurar o banco de dados:**
   O projeto utiliza SQLite como banco de dados padrão. O arquivo do banco será gerado automaticamente na raiz do projeto.

3. **Executar o servidor:**
   ```bash
   python app.py
   ```

4. **Testar as rotas:**
   Use ferramentas como Postman ou Insomnia para interagir com a API.

## Rotas Principais

- **Usuários:**
  - `POST /user`: Criação de usuário.
  - `POST /login`: Autenticação de usuário.
  - `GET /logout`: Logout do usuário autenticado.
  - `GET /whoim`: Informações sobre o usuário autenticado.

- **Refeições:**
  - `POST /refeicao`: Criação de refeição.
  - `GET /refeicao`: Listar todas as refeições do usuário.
  - `GET /refeicao/<id>`: Detalhes de uma refeição específica.
  - `PUT /refeicao/<id>`: Atualização de uma refeição.
  - `DELETE /refeicao/<id>`: Exclusão de uma refeição.

## Notas

- Certifique-se de substituir `your_secret_key` no código pela sua chave secreta personalizada para segurança.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou novas funcionalidades. Fork o repositório e envie um pull request com suas alterações.

---

**Autor:** Desenvolvido como exemplo de aplicação Flask.
