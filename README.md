# Desafio MBA Engenharia de Software com IA - Full Cycle


# Guia do Desenvolvedor

Este README contém instruções detalhadas para desenvolvedores configurarem, rodarem e depurarem o sistema de busca semântica.

---

## 1. Setup do Ambiente

Crie e ative um ambiente virtual Python:
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
```

Instale as dependências:
```bash
pip install -r requirements.txt
```

## 2. Banco de Dados (PostgreSQL + pgVector)

Suba o banco de dados localmente:
```bash
docker-compose up -d
```
Verifique se está rodando:
```bash
docker-compose ps
```
Veja docs/PASSO1_DOCKER.md para troubleshooting.

## 3. Configuração de Ambiente

Crie um arquivo `.env` na raiz do projeto:
```
OPENAI_API_KEY=sk-...
# (Opcional) DB_CONNECTION=postgresql+psycopg2://postgres:postgres@localhost:5432/rag?client_encoding=utf8
```

## 4. Ingestão de PDF

Coloque o PDF desejado em uma pasta do projeto (ex: `docs/vestibular_unb_2026.pdf`).
Execute:
```bash
python src/ingest.py docs/vestibular_unb_2026.pdf
```

## 5. Chat Interativo

Execute:
```bash
python src/chat.py
```
Digite sua pergunta e pressione Enter. Para sair, digite `sair`, `exit` ou `quit`.

---

## Exemplos de Comandos

```bash
# Ingerir PDF
python src/ingest.py docs/vestibular_unb_2026.pdf
# Rodar o chat
python src/chat.py
```

## Dicas e Troubleshooting

- Certifique-se de que o banco está rodando (`docker-compose up -d`).
- O arquivo `.env` deve conter uma chave válida da OpenAI.
- O PDF deve ser ingerido antes de buscar.
- Para múltiplos PDFs, personalize o nome da coleção no script de ingestão.
- Se ocorrer erro de conexão, revise as variáveis de conexão (`DB_CONNECTION`).
- Para depuração, adicione prints ou use breakpoints nos scripts Python.
- Consulte os logs do banco e do Docker em caso de problemas de persistência.

## Notas Técnicas

- Chunking do texto: `RecursiveCharacterTextSplitter` (1000 caracteres, overlap 150)
- Ponto de entrada do chat: `src/chat.py`
- Embeddings: HuggingFace local (`sentence-transformers/all-MiniLM-L6-v2`)
- LLM de resposta: OpenAI (`gpt-5-nano`)

---

Para instruções simplificadas para o usuário final, consulte `docs/GUIA_RAPIDO.md`.