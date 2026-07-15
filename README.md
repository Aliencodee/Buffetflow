# BuffetFlow

Sistema de gestão para buffets de eventos, desenvolvido para 
resolver problemas reais do dia a dia de um buffet familiar,
e como projeto de portfólio.

## Status atual: v0.2 — Cadastro de clientes

## Tecnologias
- Python
- FastAPI
- Pydantic

## Como rodar o projeto

1. Clone o repositório
2. Crie o ambiente virtual: `python -m venv venv`
3. Ative o ambiente: `.\venv\Scripts\Activate` (Windows)
4. Instale as dependências: `pip install -r requirements.txt`
5. Rode o servidor: `uvicorn app.main:app --reload`
6. Acesse a documentação interativa: `http://127.0.0.1:8000/docs`

## Endpoints disponíveis

### GET /
Verifica se a API está no ar.

### POST /clientes
Cadastra um novo cliente. Impede telefones duplicados.

### GET /clientes
Lista todos os clientes cadastrados.

## Roadmap
- [x] v0.1 — Estrutura inicial
- [x] v0.2 — Cadastro de clientes
- [ ] v0.3 — Cadastro de eventos
- [ ] v0.6 — Banco de dados

## Observações
Os dados atualmente são armazenados em memória (lista Python) 
e são perdidos ao reiniciar o servidor. Isso será resolvido 
na v0.6 com a implementação de banco de dados.
