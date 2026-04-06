#!/usr/bin/env python3
"""
Teste simples do modelo local de embeddings
"""
import sys
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

def test_local_model():
    print("🚀 Testando modelo local de embeddings...")
    
    # 1. Ler PDF
    pdf_path = "docs/vestibular_unb_2026.pdf"
    reader = PdfReader(pdf_path)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    print(f"✅ PDF lido: {len(text)} caracteres")
    
    # 2. Chunking
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n"]
    )
    chunks = splitter.split_text(text)
    print(f"✅ Chunks criados: {len(chunks)}")
    
    # 3. Modelo local
    print("📥 Carregando modelo local...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'}
    )
    print("✅ Modelo carregado!")
    
    # 4. Testar embedding
    print("🔍 Testando embedding de uma pergunta...")
    question = "Quantos candidatos foram aprovados?"
    question_embedding = embeddings.embed_query(question)
    print(f"✅ Embedding gerado: {len(question_embedding)} dimensões")
    
    # 5. Testar embeddings dos chunks (apenas os primeiros 3)
    print("📊 Testando embeddings de chunks...")
    chunk_embeddings = embeddings.embed_documents(chunks[:3])
    print(f"✅ {len(chunk_embeddings)} embeddings gerados")
    
    print("\n🎉 SUCESSO! Modelo local funcionando perfeitamente!")
    print("✅ PDF processar pode fazer")
    print("✅ Embeddings locais funcionando") 
    print("✅ Sem custos OpenAI!")
    
    return True

if __name__ == "__main__":
    try:
        test_local_model()
    except Exception as e:
        print(f"❌ Erro: {e}")
        sys.exit(1)