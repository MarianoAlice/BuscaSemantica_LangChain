# Passo 1: Configuração do Docker Compose para PostgreSQL + pgVector

O arquivo `docker-compose.yml` já está configurado para subir um container PostgreSQL com a extensão pgVector habilitada. Siga as instruções abaixo para garantir que o banco está pronto para uso:

## 1.1. Subir o banco de dados

Execute o comando abaixo na raiz do projeto para iniciar o PostgreSQL com pgVector:

```bash
docker-compose up -d
```

- O serviço `postgres` será iniciado na porta 5432.
- O volume `postgres_data` garante persistência dos dados.
- O serviço `bootstrap_vector_ext` garante que a extensão `vector` será criada automaticamente no banco `rag`.

## 1.2. Verificar se o banco está rodando

Para checar se o banco está ativo e a extensão instalada, execute:

```bash
docker-compose ps
```

Você pode acessar o banco via psql ou ferramentas como DBeaver, usando:
- Host: localhost
- Porta: 5432
- Usuário: postgres
- Senha: postgres
- Banco: rag

Para listar as extensões instaladas:

```bash
docker exec -it postgres_rag psql -U postgres -d rag -c "\dx"
```

A extensão `vector` deve aparecer na lista.

---

> Após validar o banco, prossiga para o passo 2: implementação do script de ingestão (`src/ingest.py`).
