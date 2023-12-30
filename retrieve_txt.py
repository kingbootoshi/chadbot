import shutil
import os

from dotenv import load_dotenv
load_dotenv()
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
 
db_directory = 'db'

embedding = OpenAIEmbeddings()
vectordb = Chroma(persist_directory='db', embedding_function=OpenAIEmbeddings())
# Create retriever
retriever = vectordb.as_retriever(search_kwargs={"k": 3})
docs = retriever.get_relevant_documents("What are Ordinals?")
print(docs)