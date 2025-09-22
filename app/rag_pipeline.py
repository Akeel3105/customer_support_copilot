# app/rag_pipeline.py
import google.generativeai as genai
import numpy as np

def retrieve_answer(query, index, df, embeddings, top_k=1):
    query_vec = embeddings.embed_query(query)
    _, I = index.search(np.array([query_vec]).astype("float32"), top_k)

    # Get best match FAQ
    match_idx = I[0][0]
    faq_answer = df.iloc[match_idx]["answer"]

    return faq_answer

def generate_response(query, context, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    Customer asked: {query}
    Context from FAQ: {context}
    Provide a helpful response.
    """

    response = model.generate_content(prompt)
    return response.text
