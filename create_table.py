import psycopg 

DB_NAME = "bilingual_chatbot"
DB_HOST = "localhost"

pgdb = psycopg.connect(dbname = DB_NAME, host = DB_HOST)

pgcursor = pgdb.cursor()

pgcursor.execute("CREATE TABLE user_queries (id SERIAL, query TEXT, detected_language VARCHAR(70));")
pgdb.commit()

