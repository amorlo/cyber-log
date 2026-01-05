FROM python:3.9-slim

WORKDIR /app

# Instalujemy streamlit
RUN pip install streamlit

# Kopiujemy aplikację
COPY app.py .

# Ważne: Tworzymy folder data w kontenerze, aby aplikacja się nie wywaliła
RUN mkdir data

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]