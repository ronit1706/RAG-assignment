import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import List
from sentence_transformers import SentenceTransformer

import chromadb

from io import BytesIO

app = FastAPI()

# Initialize ChromaDB and embedding model
chroma_client = chromadb.PersistentClient(path="chromadb")
embedding_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Initialize collection name
collection_name = "documents"


# Now create the collection again
collection = chroma_client.get_or_create_collection(name=collection_name)
def extract_text_from_file(file_content: bytes, filename: str) -> str:
    """Extract text from supported file types."""
    if filename.endswith('.txt'):
        return file_content.decode("utf-8")

@app.get("/")
def read_root():
    return {"message": "Welcome to the home page!"}

@app.post("/ingest/")
async def ingest_document(file: UploadFile = File(...)):
    content = await file.read()
    document_text = extract_text_from_file(content, file.filename)
    embedding = embedding_model.encode([document_text])
    embedding_list = embedding[0].tolist()
    collection.add([document_text], embeddings=[embedding_list])
    return {"message": f"{file.filename} ingested successfully."}

@app.get("/query/")
async def query_document(query: str):
    query_embedding = embedding_model.encode(query)
    results = collection.query(query_embedding,n_results=5)
    return {"results": results}