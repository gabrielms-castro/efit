from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
import pandas as pd
import tabula
import os
from pathlib import Path
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHROMA_DIR = os.getenv("CHROMA_DIR")

# Diretório dos PDFs
BASE_DIR = Path(__file__).resolve().parent.parent
pdf_dir = BASE_DIR / "files"
persist_dir = CHROMA_DIR or str(BASE_DIR / "chroma_shared")

# Inicializa estrutura
all_chunks = []
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
embedding = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

def extract_tables_from_pdf(pdf_path):
    tables = tabula.read_pdf(str(pdf_path), pages='all', multiple_tables=True)
    formatted_tables = []

    for i, table in enumerate(tables):
        markdown_table = table.to_markdown(index=False)
        formatted_tables.append(f"## Tabela {i+1}\n\n{markdown_table}\n\n")

    return "\n".join(formatted_tables)

# Itera pelos PDFs
for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        file_path = pdf_dir / filename
        print(f"Processando: {file_path}")

        # Extrair texto
        loader = PyMuPDFLoader(str(file_path))
        docs = loader.load()

        # Extrair tabelas
        tables_md = extract_tables_from_pdf(file_path)

        # Juntar tudo
        combined_content = "\n\n".join([doc.page_content for doc in docs] + [tables_md])
        doc_obj = Document(page_content=combined_content)

        # Split
        chunks = splitter.split_documents([doc_obj])
        all_chunks.extend(chunks)

print(f"Total de chunks: {len(all_chunks)}")

# Cria vetor
vectorstore = Chroma.from_documents(
    documents=all_chunks,
    embedding=embedding,
    persist_directory=persist_dir,
    collection_name="efit_treinos"
)
vectorstore.persist()
print("Embedding salvo com sucesso.")
