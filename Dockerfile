FROM python:3.9-slim

WORKDIR /app

# Instalujemy sterowniki systemowe dla Postgresa (wymagane w wersji slim)
RUN apt-get update && apt-get install -y libpq-dev gcc

# Instalujemy biblioteki Pythona
RUN pip install streamlit psycopg2-binary

# Kopiujemy aplikację
COPY app.py .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]