import streamlit as st
from dash import MultiApp
from apps import summary, orders, customers,traffic  # import your app modules here
from toolkit_w.tellme import Tellme

app = MultiApp()

# Add all your application here
app.add_app("Summary stats", summary.app)
app.add_app("Orders data analysis", orders.app)
app.add_app("Customers data analysis", customers.app)
app.add_app('Paid traffic analysis', traffic.app)
# The main app
app.run()