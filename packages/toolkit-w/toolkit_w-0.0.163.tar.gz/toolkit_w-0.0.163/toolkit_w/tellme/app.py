import streamlit as st
from dash import MultiApp
from apps import summary, orders, customers,traffic,discounts # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Summary stats", summary.app)
app.add_app("Orders data analysis", orders.app)
app.add_app("Customers data analysis", customers.app)
app.add_app('Paid traffic analysis', traffic.app)
app.add_app('Discount Analysis', discounts.app)
# The main app
app.run()