from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

# Caminho da pasta de PDFs
pdf_dir = BASE_DIR / "files"
persist_dir = str(BASE_DIR / "chroma_shared")

embeddings = OpenAIEmbeddings(
    api_key=os.getenv("OPENAI_API_KEY")
)
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
all_chunks = []

for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        file_path = os.path.join(pdf_dir, filename)
        print(f"Carregando: {file_path}")

        loader = PyMuPDFLoader(file_path)
        docs = loader.load()
        chunks = splitter.split_documents(docs)

        all_chunks.extend(chunks)

print(f"Total de chunks para indexar: {len(all_chunks)}")

# Cria ou atualiza o índice no Chroma
vectorstore = Chroma.from_documents(
    documents=all_chunks,
    embedding=embeddings,
    persist_directory=persist_dir,
    collection_name="efit_treinos"
)

vectorstore.persist()
print("Vetores persistidos com sucesso!")  
