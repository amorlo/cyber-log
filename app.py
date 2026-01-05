import streamlit as st
import os
from datetime import datetime

# Ustawienia strony
st.set_page_config(page_title="Cyber-Log", page_icon="📓", layout="centered")

st.title("📓 Dziennik Pokładowy: Dell 3350")
st.subheader("Zapiszpostępy w nauce")

# Ścieżka do pliku (wewnątrz kontenera)
LOG_FILE = "data/mission_logs.txt"

# Formularz wprowadzenia
with st.form("log_form", clear_on_submit=True):
    log_entry = st.text_area("Wpis do dziennika:")
    submitted = st.form_submit_button("Zapisz w bazie")

    if submitted and log_entry:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] {log_entry}\n")
        st.success("Wpis zapisany!")

st.markdown("---")
st.subheader("📜 Archiwum wpisów:")

# Odczyt pliku (jeśli istnieje)
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r") as f:
        logs = f.readlines()
        # Pokaż najnowsze na górze
        for log in reversed(logs):
            st.code(log.strip(), language="markdown")
else:
    st.info("Brak wpisów. Rozpocznij nową misję.")