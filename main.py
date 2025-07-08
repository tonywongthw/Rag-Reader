import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv()

def create_rag_system(pdf_path):
    # Step 1: Load PDF and split
    print("Loading PDF...")
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    
    # Split documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    texts = text_splitter.split_documents(documents)
    print(f"Split into {len(texts)} chunks")
    
    # Step 2: Create embeddings and store in vector DB
    print("Creating embeddings...")
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(texts, embeddings)
    print("Vector database created")
    
    # Step 3: Set up RAG chain
    print("Setting up RAG chain...")
    llm = OpenAI(temperature=0)
    
    # Custom prompt template
    prompt_template = """Use the following pieces of context to answer the question at the end.
    If you don't know the answer, just say that you don't know, don't try to make up an answer.

    Context: {context}

    Question: {question}
    Answer:"""
    
    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )
    
    # Create retrieval chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
        chain_type_kwargs={"prompt": PROMPT},
        return_source_documents=True
    )
    
    return qa_chain

def ask_question(qa_chain, question):
    # Step 4: Ask your question
    print(f"\nQuestion: {question}")
    result = qa_chain({"query": question})
    
    print(f"Answer: {result['result']}")
    
    # Show source documents
    print("\nSources:")
    for i, doc in enumerate(result['source_documents']):
        print(f"Source {i+1}: Page {doc.metadata.get('page', 'N/A')}")
        print(f"Content preview: {doc.page_content[:200]}...")
        print("-" * 50)

# Example usage
if __name__ == "__main__":
    
    try:
        # Create RAG system
        qa_chain = create_rag_system(os.path.join(os.path.dirname(__file__), "gasbill.pdf"))
        
        print("\n" + "="*80)
        print("RAG System Ready! Type your questions below.")
        print("Type 'quit' or 'exit' to stop.")
        print("="*80)
        
        # Interactive question loop
        while True:
            question = input("\nYour question: ").strip()
            
            if question.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
                
            if not question:
                print("Please enter a question.")
                continue
                
            ask_question(qa_chain, question)
            print("-" * 80)
            
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure you have:")
        print("1. Created a .env file with OPENAI_API_KEY=your-api-key")
        print("2. Installed required packages: pip install langchain openai faiss-cpu pypdf python-dotenv")
        print("3. Provided a valid PDF path")