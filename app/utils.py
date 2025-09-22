# app/utils.py
import pandas as pd
import faiss
import numpy as np
import google.generativeai as genai
#from langchain_community.embeddings import GoogleGenerativeAIEmbeddings
#from langchain.embeddings import GoogleGenerativeAIEmbeddings
#from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings


def load_faqs(path="data/faqs.csv"):
    df = pd.read_csv(path)
    return df

def create_vector_store(df, api_key):
    genai.configure(api_key=api_key)
    #embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Encode all questions
    vectors = [embeddings.embed_query(q) for q in df["question"]]
    dim = len(vectors[0])

    index = faiss.IndexFlatL2(dim)
    index.add(np.array(vectors).astype("float32"))

    return index, df, embeddings
