# RAG-assignment
A simple RAG (Retreival Augmented Generation) tool made to ingest and query documents using FAST-API. The sentences are embedded using "sentence-transformers/all-MiniLM-L6-v2" from huggingface


## Usage
* Clone and run main.py using uvicorn (function name = app)
```
uvicorn main: app --reload
```
* To add documents, I have used Postman
* Queries can be done on /query?query="your-query"
