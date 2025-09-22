# app/action_agent.py
import google.generativeai as genai

def suggest_action(query, context, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")

    prompt = f"""
    Customer query: {query}
    Context: {context}

    You are a support assistant. Based on the context:
    - If it's refund related → suggest 'Process Refund'
    - If it's delivery related → suggest 'Track Delivery'
    - If it's escalation → suggest 'Escalate to Support'
    - Otherwise → suggest 'Answer with FAQ'

    Respond with only one clear next action.
    """

    response = model.generate_content(prompt)
    return response.text.strip()
