import pandas as pd
import sqlite3
import streamlit as st

# Connect to SQLite database
conn = sqlite3.connect("my_database.db")
table_name = "my_table"  # Replace with your table name

# Query data from the database
query = f"SELECT * FROM {table_name}"
data = pd.read_sql(query, conn)

# Streamlit app to display data
st.title("Shared Database Viewer")
st.write("Below is the data from the database:")
st.dataframe(data)
