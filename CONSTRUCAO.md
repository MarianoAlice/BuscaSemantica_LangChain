# Guia de Construção do Projeto: Busca Semântica com LangChain, PostgreSQL e pgVector

Este documento serve como roteiro para a construção ordenada do sistema de ingestão e busca semântica em PDFs, utilizando Python, LangChain, PostgreSQL com pgVector e Docker Compose.

---

## Passos do Projeto

### 1. Configurar o Docker Compose para PostgreSQL + pgVector
- Criar/ajustar o arquivo `docker-compose.yml` para subir um container PostgreSQL com a extensão pgVector habilitada.
- Garantir persistência dos dados via volumes.
- Expor a porta padrão (5432) para acesso local.
- Validar a criação do banco e da extensão pgVector.

### 2. Implementar o script de ingestão (`src/ingest.py`)
- Ler um arquivo PDF e extrair seu texto.
- Dividir o texto em chunks de 1000 caracteres com overlap de 150.
- Gerar embeddings para cada chunk usando o modelo `text-embedding-3-small` da OpenAI.
- Salvar os vetores e metadados no banco PostgreSQL com pgVector.
- Validar a persistência dos dados.

### 3. Implementar o script de busca/chat (`src/search.py`)
- Receber perguntas do usuário via CLI.
- Gerar embedding da pergunta.
- Buscar os 10 chunks mais relevantes (k=10) no banco vetorial.
- Montar o prompt com os chunks e a pergunta.
- Chamar o modelo `gpt-5-nano` da OpenAI para gerar a resposta.
- Exibir a resposta ao usuário.

### 4. Documentar o uso no `README.md`
- Instruções para subir o banco com Docker Compose.
- Como configurar a API Key da OpenAI.
- Como executar a ingestão de PDFs.
- Como rodar o chat/busca via terminal.
- Exemplos de comandos.

---

## Recomendações Gerais
- Implementar e testar cada etapa antes de avançar para a próxima.
- Versionar todos os artefatos no repositório.
- Manter este guia atualizado conforme o progresso.

---

## Checklist de Artefatos
- [ ] docker-compose.yml
- [ ] src/ingest.py
- [ ] src/search.py
- [ ] requirements.txt
- [ ] README.md

---

> Siga este roteiro para garantir uma construção ordenada, modular e rastreável do sistema.
