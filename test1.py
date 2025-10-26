import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="root"
)
cur = conn.cursor()
cur.execute("SELECT datname FROM pg_database;")
databases = cur.fetchall()
print("Databases:", databases)
cur.close()
conn.close()
