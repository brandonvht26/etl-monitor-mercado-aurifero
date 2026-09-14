import sqlite3 as sql
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Monitor XAU/USD", layout="wide")
st.title("Tendencia del Mercado Aurífero (XAU/USD)")

script = "SELECT datetime, price FROM gold_price_history;"
conn = sql.connect("mercado_aurifero.db")

df = pd.read_sql_query(script, conn)

if not df.empty:
    last_price = df["price"].iloc[-1]
    penultimate_price = df["price"].iloc[-2]

    delta_price = last_price - penultimate_price

    col_a, col_b = st.columns([1, 5])

    with col_a:
        st.metric(
            label="Precio Actual",
            value=f"{last_price:.2f} USD",
            delta=f"{delta_price:.2f} USD"
        )
    
    with col_b:
        df["datetime"] = pd.to_datetime(df["datetime"])
        df["datetime"] = df["datetime"].dt.strftime("%d-%m %H:%M")

        df.set_index("datetime", inplace=True)
        st.line_chart(df)

else:
    st.warning("[SISTEMA] La base de datos está vacía. Inicia el monitor para capturar los precios.")

conn.close()