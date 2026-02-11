from fastapi import FastAPI
import psycopg2, os

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/goal")
def add_goal(goal: dict):
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        dbname=os.getenv("DB_NAME")
    )
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO goals (goal_name) VALUES (%s)",
        (goal["goal"],)
    )
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Goal added"}

