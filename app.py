import streamlit as st
import psycopg2
import os
from datetime import datetime

# Konfiguracja strony
st.set_page_config(page_title="Cyber-Log SQL", page_icon="🐘", layout="centered")

st.title("🐘 Cyber-Log: PostgreSQL Edition")

# Pobieranie danych logowania ze zmiennych środowiskowych to co wpisaliśmy w compose
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# Funkcja do łączenia z bazą (z prostym mechaniznem ponawiania)
def get_connection():
    try:
        return psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
    except Exception as e:
        return None
    
# Inicjalizacja tabeli (jeśli nie istnieje)
conn = get_connection()
if conn:
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
    st.success("Połączono z bazą danych!")
else:
    st.error("Błąd połączenia z bazą danych!")

# Formularz
with st.form("log_form", clear_on_submit=True):
    log_entry = st.text_area("Wpis do bazy SQL:")
    submitted = st.form_submit_button("Zapisz")

    if submitted and log_entry:
        conn = get_connection()
        if conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO logs (content) VALUES (%s)", (log_entry,))
            conn.commit()
            conn.close()
            st.success("Zapisano w PostreSQL!")

st.markdown("---")
st.subheader("📜 Historia z Bazy:")

# Odczyt danych
conn = get_connection()
if conn:
    cur = conn.cursor()
    cur.execute("SELECT content, created_at FROM logs ORDER BY created_at DESC")
    rows = cur.fetchall()

    for row in rows:
        st.info(f"[{row[1]}] {row[0]}")
            
    conn.close()