# app/crm_agent.py
import pandas as pd

def load_orders(path="data/crm_orders.csv"):
    return pd.read_csv(path)

def lookup_order(order_id, df):
    try:
        order = df[df["order_id"] == int(order_id)]
        if order.empty:
            return f"No order found with ID {order_id}"
        else:
            rec = order.iloc[0]
            return (
                f"Order {rec['order_id']} for {rec['customer_name']} is currently {rec['status']}. "
                f"Delivery date: {rec['delivery_date']}, Amount: ${rec['amount']}."
            )
    except Exception as e:
        return f"Error: {str(e)}"
