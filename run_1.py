# run.py
import streamlit as st
import os
from dotenv import load_dotenv
import pandas as pd
from app.utils import load_faqs, create_vector_store
from app.crm_agent import load_orders
from app.copilot import copilot_response

# Load API key
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

st.title("🛒 GenAI Customer Support Copilot (Phase 2)")

# Load Data
df_faq = load_faqs()
df_orders = load_orders()
index, df_faq, embeddings = create_vector_store(df_faq, "distilbert-base-uncased")  # HuggingFace

# Input
query = st.text_input("Ask me about your order, refund, or delivery:")

if query:
    final_response, action = copilot_response(query, index, df_faq, embeddings, df_orders, API_KEY)

    st.write("🤖 Assistant:", final_response)
    st.write("👉 Suggested Next Action:", action)
