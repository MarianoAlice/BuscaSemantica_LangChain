#!/usr/bin/env python3
"""
Sistema de busca semântica SEM PostgreSQL
Usa arquivos locais para armazenar embeddings
"""
import os
import json
import pickle
from typing import List
from dotenv import load_dotenv
from pypdf import PdfReader
from langchain_text_splitters import CharacterTextSplitter 
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
import numpy as np

load_dotenv()

PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
EMBEDDINGS_FILE = "embeddings_local.pkl"
CHUNKS_FILE = "chunks_local.json"

def ingest_pdf_local(pdf_path: str):
    """Ingere PDF e salva embeddings localmente"""
    
    print("📖 Lendo PDF...")
    reader = PdfReader(pdf_path)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    
    print("✂️ Dividindo em chunks...")
    splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        separator="\n"
    )
    chunks = splitter.split_text(text)
    print(f"✅ {len(chunks)} chunks criados")
    
    print("🤖 Carregando modelo de embeddings...")
    embeddings_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'}
    )
    
    print("🔢 Gerando embeddings...")
    embeddings = embeddings_model.embed_documents(chunks)
    
    print("💾 Salvando dados localmente...")
    # Salvar chunks
    with open(CHUNKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)
    
    # Salvar embeddings
    with open(EMBEDDINGS_FILE, 'wb') as f:
        pickle.dump(embeddings, f)
    
    print(f"✅ Dados salvos: {CHUNKS_FILE} e {EMBEDDINGS_FILE}")
    return True

def cosine_similarity(a, b):
    """Calcula similaridade coseno entre dois vetores"""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def search_local(question: str, top_k: int = 4):
    """Busca local usando similaridade coseno"""
    
    if not os.path.exists(CHUNKS_FILE) or not os.path.exists(EMBEDDINGS_FILE):
        return "❌ Dados não encontrados. Execute primeiro: python search_local.py --ingest"
    
    if not GOOGLE_API_KEY:
        return "❌ GOOGLE_API_KEY não configurada no .env"
    
    print("🔍 Gerando embedding da pergunta...")
    embeddings_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'}
    )
    
    question_embedding = embeddings_model.embed_query(question)
    
    print("📂 Carregando dados locais...")
    # Carregar chunks
    with open(CHUNKS_FILE, 'r', encoding='utf-8') as f:
        chunks = json.load(f)
    
    # Carregar embeddings
    with open(EMBEDDINGS_FILE, 'rb') as f:
        embeddings = pickle.load(f)
    
    print("📊 Calculando similaridades...")
    similarities = []
    for i, chunk_embedding in enumerate(embeddings):
        sim = cosine_similarity(question_embedding, chunk_embedding)
        similarities.append((i, sim, chunks[i]))
    
    # Ordenar por similaridade
    similarities.sort(key=lambda x: x[1], reverse=True)
    
    # Pegar top_k mais similares
    top_chunks = [chunk for _, _, chunk in similarities[:top_k]]
    contexto = "\n\n".join(top_chunks)
    
    print(f"📄 Usando {len(top_chunks)} chunks mais relevantes")
    
    print("🤖 Gerando resposta com Gemini...")
    try:
        llm = ChatGoogleGenerativeAI(
            model="gemini-flash-latest",
            google_api_key=GOOGLE_API_KEY,
            temperature=0.1,
            max_tokens=500
        )
        
        prompt = PROMPT_TEMPLATE.format(
            contexto=contexto,
            pergunta=question
        )
        
        response = llm.invoke(prompt)
        
        # Extrair apenas o texto limpo da resposta
        if hasattr(response, 'content'):
            if isinstance(response.content, list):
                # Se for lista, extrair texto do primeiro item
                for item in response.content:
                    if isinstance(item, dict) and 'text' in item:
                        return item['text']
                    elif hasattr(item, 'text'):
                        return item.text
                return str(response.content[0]) if response.content else "Sem resposta"
            else:
                return response.content
        else:
            return str(response)
        
    except Exception as e:
        return f"❌ Erro no Gemini: {str(e)}"

def chat_loop_local():
    """Chat interativo com sistema local"""
    print("🎯 Busca Semântica LOCAL - Vestibular UnB")
    print("💡 Embeddings: HuggingFace (local) + Gemini (chat)")
    print("💾 Armazenamento: Arquivos locais (sem PostgreSQL)")
    print("💰 Custo: $0.00 - 100% gratuito!")
    print("-" * 50)
    
    if not os.path.exists(CHUNKS_FILE):
        print("⚠️  Dados não encontrados!")
        print("📖 Execute primeiro: python search_local.py --ingest")
        return
    
    print("Digite sua pergunta (ou 'sair' para encerrar):")
    print()

    while True:
        try:
            pergunta = input("Pergunta: ").strip()
            
            if pergunta.lower() in ['sair', 'exit', 'quit', '']:
                print("👋 Até logo!")
                break
                
            print()
            resposta = search_local(pergunta)
            print(f"Resposta: {resposta}")
            print()
            print("-" * 50)
            
        except KeyboardInterrupt:
            print("\n👋 Até logo!")
            break
        except Exception as e:
            print(f"❌ Erro: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--ingest":
        print("🚀 INGESTÃO PDF -> Sistema Local")
        print("="*40)
        ingest_pdf_local("docs/vestibular_unb_2026.pdf")
    else:
        chat_loop_local()