import shutil
import os

# Delete the 'db' directory if it exists
db_directory = 'db'
if os.path.exists(db_directory):
    shutil.rmtree(db_directory)

from dotenv import load_dotenv
load_dotenv()
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import DirectoryLoader

# Print number of txt files in directory
loader = DirectoryLoader('texts', glob="./*.txt")
doc = loader.load()
print(len(doc))  # Fixed missing print statement
# Splitting the text into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(doc)
print(len(texts))  # Fixed missing print statement
# OpenAI embeddings
embedding = OpenAIEmbeddings()
vectordb = Chroma.from_documents(
    documents=texts,
    embedding=embedding,  # Reuse the embedding object created earlier
    persist_directory=db_directory
)
# Create retriever
retriever = vectordb.as_retriever(search_kwargs={"k": 5})
docs = retriever.get_relevant_documents("What are Ordinals?")
print(docs)

vectordb = Chroma(persist_directory='db', embedding_function=OpenAIEmbeddings())
# Create retriever
retriever = vectordb.as_retriever(search_kwargs={"k": 5})
docs = retriever.get_relevant_documents("What are Ordinals?")
print(docs)