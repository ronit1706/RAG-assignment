from fastapi import FastAPI, UploadFile, File
from typing import List
import asyncio

app = FastAPI()

@app.post("/ingest/")
async def ingest_document(file: UploadFile = File(...)):
    # Process file, extract text, generate embedding, store in ChromaDB
    content = await file.read()
    # Extract text, generate embeddings, and store
    document_text = extract_text_from_file(content, file.filename)
    embedding = embedding_model.encode(document_text)
    chroma_client.add_text([document_text], embeddings=[embedding])
    return {"message": f"{file.filename} ingested successfully."}

@app.get("/query/")
async def query_document(query: str):
    # Generate query embedding and perform ChromaDB search
    query_embedding = embedding_model.encode(query)
    results = chroma_client.search(query_embedding, top_k=5)
    return {"results": results}