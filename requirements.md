# UASZ-GPT – Application Requirements

## Objective
Build a Retrieval-Augmented Generation (RAG) application using:
- Streamlit
- LangChain
- Google Gemini API
- Chroma Vector Database

The application allows users to upload PDF documents and interact with them through an AI-powered chat interface.

## Workflow (Step by Step)

1. Create a virtual environment and install dependencies
2. Set up a basic Streamlit application skeleton
3. Add PDF upload UI and user text input
4. Load PDF using PyPDFLoader and display number of pages
5. Split document text into chunks
6. Generate embeddings using Gemini and store them in ChromaDB
7. Implement retrieval and question-answering using Gemini chat model
8. Display answers in Streamlit, including source documents

⚠️ Constraint:  
Do not generate the full application code at once.  
Each step must be implemented incrementally.
