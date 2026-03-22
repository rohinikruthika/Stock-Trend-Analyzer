import os
import streamlit as st
import pickle
import time
from langchain_openai import OpenAI, OpenAIEmbeddings
from langchain_classic.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env (especially openai api key)

print("env read completed")

st.title("News Research Tool 📈")
st.sidebar.title("News Article URLs")

print("sidebare and title set")



if "num_urls" not in st.session_state:
    st.session_state.num_urls = 1

urls = []
for i in range(st.session_state.num_urls):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

if st.session_state.num_urls < 10:
    if st.sidebar.button("+ Add URL", key="add_url_btn"):
        st.session_state.num_urls += 1
        st.rerun()
else:
    st.sidebar.warning("⚠️ Maximum 10 URLs reached!")

print("url completed")

process_url_clicked = st.sidebar.button("Process URLs")  # Button to initiate processing of entered URLs
file_path = "faiss_store_openai.pkl"  # File path for storing serialized FAISS index 

print("button is okay too")

main_placeholder = st.empty()  # Placeholder for main content area
llm = OpenAI(temperature=0.5, max_tokens=500)  # Initializing OpenAI language model 

print("llm connection established")

if process_url_clicked: 
    print("entered button clicked section")
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading...Started...✅✅✅")  # Display loading message
    data = loader.load()

    print("Data Loading...Started")
    
    # Split data into smaller documents
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    
    main_placeholder.text("Text Splitter...Started...✅✅✅")  # Display text splitting message
    docs = text_splitter.split_documents(data)
    print("Text Splitter...Started..")
    
    # Create embeddings from documents and build FAISS index
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    pkl = vectorstore_openai.serialize_to_bytes()
    main_placeholder.text("Embedding Vector Started Building...✅✅✅")  # Display embedding vector building message
    time.sleep(2)  # Simulate processing time
    print("Embedding Vector Started Building")

    # Save the FAISS index to a pickle file
    with open(file_path, "wb") as f:
        pickle.dump(pkl, f)


# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Initialize query key for clearing input
if "query_key" not in st.session_state:
    st.session_state.query_key = 0

# Question box
query = st.text_input("Question: ", key=f"question_{st.session_state.query_key}")

if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            pkl = pickle.load(f)
            vectorstore = FAISS.deserialize_from_bytes(
                embeddings=OpenAIEmbeddings(),
                serialized=pkl,
                allow_dangerous_deserialization=True
            )
            chain = RetrievalQAWithSourcesChain.from_llm(
                llm=llm,
                retriever=vectorstore.as_retriever()
            )
            result = chain.invoke({"question": query})

            # Save to chat history
            st.session_state.chat_history.append({
                "question": query,
                "answer": result["answer"],
                "sources": result.get("sources", "")
            })

            # Clear question box
            st.session_state.query_key += 1
            st.rerun()

# Display answers below
if st.session_state.chat_history:
  
    for chat in reversed(st.session_state.chat_history):
        st.markdown(f"**Q: {chat['question']}**")
        st.write(f"A: {chat['answer']}")
        if chat['sources']:
            st.subheader("Sources:")
            sources_list = chat['sources'].split("\n")
            for source in sources_list:
                st.write(source)
        st.divider()