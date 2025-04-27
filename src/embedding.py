# TODO - pesquisar a melhor estratégia de splitter para o tipo de documentos que queremos (manuais e estudos científicos)
# TODO - encontrar uma maneira de aumentar o score do similarity search
# TODO - melhorar conversão do PDF para Texto e criar um pipeline de limpeza do .txt (remover nome de pessoas, formatação de links etc
# TODO - melhor qualidade dos materiais para serem embedados
# TODO - criar classes para melhorar padrão de projeto
# TODO - adicionar client para o Chroma (possivelmente Docker)

import os
from pathlib import Path

from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyMuPDFLoader, TextLoader
from langchain_openai import OpenAIEmbeddings

load_dotenv()

# Configurações
BASE_DIR = Path(__file__).resolve().parent.parent
pdf_dir = BASE_DIR / "files"
text_file = BASE_DIR / "files" / "pdf_txt.txt"
persist_directory = BASE_DIR / "chroma_db"
persist_directory.mkdir(parents=True, exist_ok=True)

def convert_pdf_to_txt(pdf_dir):
    with open(str(pdf_dir / "pdf_txt_2.txt"), "w") as f:
        for pdf_file in pdf_dir.glob("*.pdf"):
            loader = PyMuPDFLoader(str(pdf_file))
            pages = loader.load()
            f.write(f"Arquivo: {pdf_file.name}\n")
            for page in pages:
                f.write(f"Página {page.metadata['page'] + 1}:\n")
                f.write(page.page_content)
                f.write("\n\n")

def load_text_file(text_file):
    if not text_file.exists():
        raise FileNotFoundError(f"Arquivo {text_file} não encontrado.")
    loader = TextLoader(str(text_file))
    data = loader.load()
    return data

def splitter(data):
    if not data:
        return []
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500 , chunk_overlap=50)
    splits = text_splitter.split_documents(data)
    return splits

def embedding(api_key=os.getenv("OPENAI_API_KEY")):
    return OpenAIEmbeddings(api_key=api_key)

def create_vector_store():
    return Chroma.from_documents(
        documents=splitter(
            load_text_file(text_file)
        ),
        embedding=embedding(),
        persist_directory=str(persist_directory),
        collection_name="efit_manuals"
    )

def load_vector_store(collection_name="efit_manuals"):
    return Chroma(
        embedding_function=embedding(),
        persist_directory=str(persist_directory),
        collection_name=collection_name
    )


if __name__ == "__main__":
    # Pode apagar depois
    vector_db = load_vector_store(collection_name="efit_manuals")
    retriever = vector_db.as_retriever()
    print(retriever.invoke("Monte um treino de musculação dividido em upper/lower")[0].page_content)