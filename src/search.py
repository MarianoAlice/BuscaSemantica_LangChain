PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""


import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI
from langchain_community.vectorstores.pgvector import PGVector

load_dotenv()

DB_CONNECTION = os.getenv("DB_CONNECTION") or "postgresql+psycopg2://postgres:postgres@localhost:5432/rag"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def search_prompt(question=None):
  if not question:
    return "Pergunta não informada."

  # 1. Embedding da pergunta (modelo local gratuito)
  embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'}
  )

  # 2. Conectar ao banco vetorial
  db = PGVector(
    connection_string=DB_CONNECTION,
    embedding_function=embeddings
  )

  # 3. Buscar os 10 chunks mais relevantes
  results = db.similarity_search(question, k=10)
  contexto = "\n---\n".join([doc.page_content for doc in results])

  # 4. Montar prompt
  prompt = PROMPT_TEMPLATE.format(contexto=contexto, pergunta=question)

  # 5. Chamar LLM
  llm = ChatOpenAI(
    model="gpt-5-nano",
    openai_api_key=OPENAI_API_KEY,
    temperature=0.0
  )
  resposta = llm.invoke(prompt)
  return resposta.content if hasattr(resposta, 'content') else resposta


def main():
  print("\nBusca semântica - Vestibular UnB\nDigite sua pergunta (ou 'sair' para encerrar):\n")
  while True:
    question = input("Pergunta: ").strip()
    if question.lower() in ("sair", "exit", "quit"): break
    resposta = search_prompt(question)
    print(f"\nResposta: {resposta}\n")


if __name__ == "__main__":
  main()