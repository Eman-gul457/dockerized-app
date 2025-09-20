import os
from flask import Flask, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

APP_PORT = int(os.environ.get("APP_PORT", 5000))
DB_HOST = os.environ.get("DB_HOST", "db")
DB_PORT = int(os.environ.get("DB_PORT", "5432"))
DB_NAME = os.environ.get("POSTGRES_DB", "appdb")
DB_USER = os.environ.get("POSTGRES_USER", "appuser")
DB_PASS = os.environ.get("POSTGRES_PASSWORD", "apppassword")

app = Flask(__name__)

def get_db_conn():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        cursor_factory=RealDictCursor,
        connect_timeout=2,
    )

@app.route("/healthz")
def healthz():
    return jsonify({"status": "ok"}), 200

@app.route("/")
def index():
    try:
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS visits (
                id SERIAL PRIMARY KEY,
                ts TIMESTAMPTZ DEFAULT NOW()
            )
        """)
        cur.execute("INSERT INTO visits DEFAULT VALUES RETURNING id, ts;")
        conn.commit()
        cur.execute("SELECT COUNT(*) AS total FROM visits;")
        total = cur.fetchone()["total"]
        cur.close()
        conn.close()
        return f"Hello from Flask! Total visits recorded in DB: {total}\n", 200
    except Exception:
        return (
            "Hello from Flask! Database is not available yet. "
            "Once we run docker-compose, this will show a visit counter.\n"
        ), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=APP_PORT)
