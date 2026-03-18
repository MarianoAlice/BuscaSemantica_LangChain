import os
import sys
from dotenv import load_dotenv
from pypdf import PdfReader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores.pgvector import PGVector

load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")
DB_CONNECTION = os.getenv("DB_CONNECTION") or "postgresql+psycopg2://postgres:postgres@localhost:5432/rag?client_encoding=utf8"

def ingest_pdf(pdf_path: str):
    # 1. Ler PDF
    reader = PdfReader(pdf_path)
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    if not text.strip():
        print("[ERRO] Nenhum texto extraído do PDF.")
        return

    # 2. Chunking
    splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150,
        separator="\n"
    )
    chunks = splitter.split_text(text)
    print(f"[INFO] {len(chunks)} chunks gerados.")

    # 3. Embeddings (usando modelo gratuito do Hugging Face)
    print("[INFO] Carregando modelo de embeddings local...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'}
    )

    # 4. Armazenar no banco (pgvector)
    collection_name = os.path.basename(pdf_path)
    db = PGVector.from_texts(
        texts=chunks,
        embedding=embeddings,
        collection_name=collection_name,
        connection_string=DB_CONNECTION,
        pre_delete_collection=True
    )
    print(f"[OK] Ingestão concluída para {pdf_path}.")

if __name__ == "__main__":
    path = PDF_PATH or (sys.argv[1] if len(sys.argv) > 1 else None)
    if not path:
        print("Uso: python ingest.py <caminho_pdf> ou defina PDF_PATH no .env")
        sys.exit(1)
    ingest_pdf(path)