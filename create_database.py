"""creates a databse for further usage"""
import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("""CREATE TABLE users (
          username text,
          email text,
          password text,
          user_id integer,
          friends_id text,
          tasted_wines text,
          quizz_res text
        )""")

c.execute("""CREATE TABLE reviews (
          user_id integer,
          wine_id integer,
          review text
        )""")

c.execute("""CREATE TABLE wines (
          wine_id integer,
          name text,
          attribute text,
          country text,
          color text
        )""")
conn.commit()
conn.close()
