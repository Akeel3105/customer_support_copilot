# app/copilot.py
from app.rag_pipeline import retrieve_answer, generate_response
from app.crm_agent import lookup_order
from app.action_agent import suggest_action

def copilot_response(query, index, df_faq, embeddings, df_orders, api_key):
    # Step 1: Check if query contains an order ID
    if any(str(x) in query for x in df_orders["order_id"].astype(str)):
        order_id = [x for x in df_orders["order_id"].astype(str) if x in query][0]
        crm_context = lookup_order(order_id, df_orders)
        final_response = crm_context
    else:
        # Step 2: Use FAQ Agent
        context = retrieve_answer(query, index, df_faq, embeddings)
        final_response = generate_response(query, context, api_key)

    # Step 3: Suggest next action
    action = suggest_action(query, final_response, api_key)

    return final_response, action
