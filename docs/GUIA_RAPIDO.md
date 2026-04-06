

# Guia Rápido de Uso

Este guia mostra como usar o sistema de busca semântica para fazer perguntas sobre o PDF do vestibular da UnB.

---



## 1. Ingerindo o PDF

Coloque o PDF desejado na pasta do projeto (ex: `docs/vestibular_unb_2026.pdf`).

Peça ao responsável técnico para rodar:
```bash
python src/ingest.py docs/vestibular_unb_2026.pdf
```

---


## 2. Fazendo Perguntas (Chat)

Para iniciar o chat, use:
```bash
python src/chat.py
```

Digite sua pergunta e pressione Enter. Para sair, digite `sair`, `exit` ou `quit`.

---


## 3. Exemplos de Perguntas

Você pode perguntar, por exemplo:

- Quantos candidatos foram aprovados no vestibular da UnB?
- Quem foi o primeiro colocado em Medicina?
- Quais cursos tiveram mais aprovados?

---

Se tiver dúvidas ou problemas, procure o responsável técnico ou suporte do sistema.

---


## Dicas e Boas Práticas para Desenvolvedores

- Certifique-se de que o banco de dados está rodando (`docker-compose up -d`).
- O arquivo `.env` deve conter a variável `OPENAI_API_KEY` válida.
- O PDF deve ser ingerido antes de buscar (veja passo 4).
- Para múltiplos PDFs, personalize o nome da coleção no script de ingestão.
- Se ocorrer erro de conexão com o banco, revise as variáveis de conexão (`DB_CONNECTION`).
- O chunking do texto é feito com `RecursiveCharacterTextSplitter` (1000 caracteres, overlap 150).
- O ponto de entrada do chat é `src/chat.py` (não mais `src/search.py`).
- O modelo de embeddings é HuggingFace local (`sentence-transformers/all-MiniLM-L6-v2`).
- O modelo de resposta é OpenAI (`gpt-5-nano`).
- Para depuração, adicione prints ou use breakpoints nos scripts Python.
- Consulte os logs do banco e do Docker em caso de problemas de persistência.

---


## Exemplos de Perguntas para Testes

- Quantos candidatos foram aprovados no vestibular da UnB?
- Quais cursos tiveram mais aprovados?
- Quem foi o primeiro colocado em Medicina?
- Houve aumento no número de aprovados em relação ao ano anterior?
- Quais cidades tiveram mais aprovados?
- Como foi a distribuição de aprovados por escola?
- Qual a nota de corte para Engenharia?
- Houve candidatos aprovados em mais de um curso?
- Quais foram os cursos mais concorridos?
- Qual foi a maior nota do vestibular?

**Dica:** Use perguntas variadas para validar a cobertura do chunking e a precisão dos embeddings.

---


> Siga este guia para levantar, testar e depurar o sistema de busca semântica. Em caso de dúvidas, consulte os scripts-fonte e os arquivos de configuração.
