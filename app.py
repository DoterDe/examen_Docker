from flask import Flask
import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

DB_NAME = os.getenv("POSTGRES_DB")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = os.getenv("POSTGRES_HOST", "db")  
DB_PORT = os.getenv("POSTGRES_PORT", 5432)


@app.route("/")
def index():
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        connection.close()
        return "✅ Успешное подключение к PostgreSQL!"
    except OperationalError as e:
        return f"❌ Ошибка подключения: {e}"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
