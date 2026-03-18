# Guia Rápido de Uso

Este guia mostra como levantar o sistema de busca semântica e realizar perguntas sobre o PDF de aprovações no vestibular da UnB.

---


## 1. Preparando o Ambiente Python (VirtualEnv)

Antes de instalar as dependências, crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual:
- **Windows:**
	```bash
	.venv\Scripts\activate
	```
- **Linux/Mac:**
	```bash
	source .venv/bin/activate
	```

Depois, instale as dependências:

```bash
pip install -r requirements.txt
```

---

## 2. Subindo o Banco de Dados (PostgreSQL + pgVector)

Na raiz do projeto, execute:

```bash
docker-compose up -d
```

Aguarde até que o banco esteja pronto (veja docs/PASSO1_DOCKER.md para detalhes de verificação).

---

## 3. Configurando a API Key da OpenAI

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
OPENAI_API_KEY=sk-...
```


### Como criar uma chave da OpenAI

1. Acesse https://platform.openai.com/signup e crie uma conta (ou faça login).
2. No menu lateral, clique em "API Keys" ou "Chaves de API".
3. Clique em "Create new secret key" (Criar nova chave secreta).
4. Copie a chave gerada (começa com `sk-...`).
5. Guarde a chave em local seguro e adicione ao arquivo `.env` conforme instruções acima.

> Atenção: Não compartilhe sua chave publicamente. Ela é pessoal e dá acesso à sua conta OpenAI.

---

## 4. Ingerindo o PDF

Coloque o PDF das aprovações do vestibular da UnB em uma pasta do projeto (ex: `docs/vestibular_unb_2026.pdf`).

Execute:

```bash
python src/ingest.py docs/vestibular_unb_2026.pdf
```

---

## 5. Realizando Perguntas via Terminal (Chat)

Execute:

```bash
python src/search.py
```

O sistema entrará em modo chat. Digite suas perguntas e pressione Enter. Para sair, digite `sair`, `exit` ou `quit`.

Exemplo de uso:

```
Busca semântica - Vestibular UnB
Digite sua pergunta (ou 'sair' para encerrar):

Pergunta: Quantos candidatos foram aprovados no vestibular da UnB?
Resposta: ...

Pergunta: sair
```

---

## Dicas e Boas Práticas

- Certifique-se de que o banco de dados está rodando (`docker-compose up -d`).
- O arquivo `.env` deve conter a variável `OPENAI_API_KEY` válida.
- O PDF deve ter sido ingerido antes de buscar (veja passo 3).
- Caso a resposta seja "Não tenho informações necessárias para responder sua pergunta.", verifique se o PDF realmente contém a informação ou se a pergunta está clara e objetiva.
- Para múltiplos PDFs, cada ingestão sobrescreve a coleção anterior (ajuste o nome da coleção se desejar manter múltiplos documentos).
- Se ocorrer erro de conexão com o banco, revise as variáveis de conexão (`DB_CONNECTION`).
- O modelo utilizado para embeddings é `text-embedding-3-small` e para respostas é `gpt-5-nano` (ajuste no código se necessário).

---

## Exemplos de Perguntas para o PDF da UnB

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

---

> Siga este guia para levantar o sistema e explorar o PDF de aprovações no vestibular da UnB usando busca semântica.
