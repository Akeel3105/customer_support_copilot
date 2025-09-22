# run.py
import streamlit as st
import os
from dotenv import load_dotenv
from app.utils import load_faqs, create_vector_store
from app.rag_pipeline import retrieve_answer, generate_response

# Load API key
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

st.title("🛒 GenAI Customer Support Copilot (Phase 1)")

# Load FAQs + Vector Store
df = load_faqs()
index, df, embeddings = create_vector_store(df, API_KEY)

# Chat Interface
query = st.text_input("Ask me something about your order, refund, or delivery:")

if query:
    context = retrieve_answer(query, index, df, embeddings)
    response = generate_response(query, context, API_KEY)

    st.write("🤖 Assistant:", response)
