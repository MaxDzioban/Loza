import sqlite3
from app_classes import User

def add_new_user(user):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (user.username, user.email, user.password))
    conn.commit()
    conn.close()


def get_users():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    return c.fetchall()

def update_name(user, new_name):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""UPDATE users SET username = :username WHERE email = :email""", {'username': new_name, 'email': user.email, 'password': user.password})
    conn.commit()
    conn.close()



user1 = User('John Doe', 'johndoe@gmail.com', 'thepassword321')
user2 = User('Caitlyn Smith', 'caitlynsmith@gmail.com', 'thepassword123')

add_new_user(user1)
add_new_user(user2)

print(get_users())

update_name(user1, 'Sally Jo')

print(get_users())
