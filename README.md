# RAG-assignment
A simple RAG (Retreival Augmented Generation) tool made to ingest and query documents using FAST-API. The sentences are embedded using "sentence-transformers/all-MiniLM-L6-v2" from huggingface and the embeddings are stored in a persistant chromaDB


## Usage
* Clone and run main.py using uvicorn (function name = app)
```
uvicorn main: app --reload
```
* To add documents, I have used Postman
* Queries can be done on /query?query="your-query"

## Why you should hire me at Cybernetyx

I’m excited about the opportunity to contribute as a Generative AI Intern, as my background aligns closely with the role’s demands. My recent internship at IFFCO Tokio GIC equipped me with hands-on experience in developing a Retrieval-Augmented Generation (RAG) pipeline for interactive AI models, where I applied LLaMA and LangChain to build a high-performance conversational bot capable of handling complex document structures. I have strong Python programming skills, deep familiarity with frameworks like LangChain and RAG, and experience in model fine-tuning and optimizing data pipelines. I am also driven by my passion for AI innovation and a proactive approach to learning, making me eager to bring value to your team while contributing to real-world AI applications.

## Do also check out

* doc_talk: https://github.com/ronit1706/doc_talk
Made as my project for the internship at IFFCO Tokio, this tool also incorportates RAG, but uses a llama model for querying. It also handles unselectable/handwritten pdfs using OCR, where it also recognizes tables (essential for the internship, as insurance documents contain a lot of tables) using opencv, and handles their content properly (do check the code)
