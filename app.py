import streamlit as st
import tempfile
import os
import google.generativeai as genai
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("GOOGLE_API_KEY not found. Please check your .env file.")

def main():
    st.set_page_config(page_title="UASZ-GPT", page_icon="🤖")
    
    st.title("UASZ-GPT")
    st.write("Welcome to UASZ-GPT, your AI-powered document assistant. Upload your PDFs and start asking questions!")

    # Sidebar for PDF upload
    with st.sidebar:
        st.header("Documents")
        uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

    # User text input
    user_question = st.chat_input("Ask a question about your document...")

    if uploaded_file:
        st.info(f"File uploaded: {uploaded_file.name}")
        
        # Save uploaded file to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.getvalue())
            tmp_path = tmp_file.name

        try:
            # Load PDF using PyPDFLoader
            loader = PyPDFLoader(tmp_path)
            docs = loader.load()
            
            st.success(f"Successfully loaded PDF! Total pages: {len(docs)}")

            # Split document text into chunks
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=100
            )
            chunks = text_splitter.split_documents(docs)
            st.info(f"Document split into {len(chunks)} chunks.")

            # Generate embeddings and store in ChromaDB
            embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
            
            # Use a fixed collection name and handle cleanup via Chroma's own methods
            # This avoids WinError 32 by not deleting the folder manually while files are locked
            vector_db = Chroma.from_documents(
                documents=chunks,
                embedding=embeddings,
                collection_name="current_doc"
            )
            st.success("Embeddings generated and stored in ChromaDB.")
            
            # Save the vector_db in session state for later retrieval
            st.session_state.vector_db = vector_db
        except Exception as e:
            st.error(f"Error loading PDF: {e}")
        finally:
            # Clean up the temporary file
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
    
    if user_question:
        st.write(f"You asked: {user_question}")
        
        if "vector_db" in st.session_state:
            try:
                # Retrieve relevant chunks
                relevant_docs = st.session_state.vector_db.similarity_search(user_question, k=5)
                
                # Prepare context and prompt
                context_text = "\n\n".join([doc.page_content for doc in relevant_docs])
                
                full_prompt = f"""
                Tu es un assistant expert en analyse de documents. 
                Réponds à la question suivante en utilisant UNIQUEMENT le contexte fourni ci-dessous.
                Si la réponse n'est pas dans le contexte, dis explicitement que tu ne trouves pas l'information dans le document.

                CONTEXTE :
                {context_text}
                
                QUESTION :
                {user_question}
                
                RÉPONSE (Sois précis et cite les parties du document si possible) :
                """
                
                # Call Gemini API directly
                model_name = 'models/gemini-flash-latest'
                model = genai.GenerativeModel(model_name)
                response = model.generate_content(full_prompt)
                answer = response.text
                
                st.write("### Answer:")
                st.write(answer)
                
                # Display source documents
                with st.expander("Source Documents"):
                    for i, doc in enumerate(relevant_docs):
                        st.markdown(f"**Source {i+1} (Page {doc.metadata.get('page', 'N/A')}):**")
                        st.write(doc.page_content)
                        st.divider()
                
                # Store answer and sources
                st.session_state.last_answer = answer
                st.session_state.last_sources = relevant_docs
                
            except Exception as e:
                st.error(f"Error during question-answering: {e}")
        else:
            st.warning("Please upload a PDF document first!")

if __name__ == "__main__":
    main()
