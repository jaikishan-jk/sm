import streamlit as st
import pyodbc
import pandas as pd

# Define your connection parameters
server = '10.10.200.207'  
database = 'ADFTrainingDB' 
username = 'adftraining'  
password = 'adftraining@123'  

# Create a connection string
conn_str = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'

# Establish the connection
conn = pyodbc.connect(conn_str)

# Create a cursor object
cursor = conn.cursor()

# Example query
query = 'SELECT * FROM dbo.DimAccount'

# Fetch results into a DataFrame
df = pd.read_sql(query, conn)

# Close the connection
cursor.close()
conn.close()

# Streamlit app
st.title("SQL Server Data Display")
st.write("Data from dbo.DimAccount table:")

# Display the DataFrame
st.dataframe(df)