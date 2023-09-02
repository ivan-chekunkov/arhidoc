import sqlite3


conn = sqlite3.connect('arhidoc\\db.sqlite3')
cur = conn.cursor()


def create_db():
    cur.execute("""CREATE TABLE IF NOT EXISTS cat(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT);
    """)
    cur.execute("""CREATE TABLE IF NOT EXISTS docs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date datetime,
    name TEXT,
    number TEXT,
    category TEXT,
    file_path TEXT,
    cat_id INTEGER,
    FOREIGN KEY (cat_id) REFERENCES cat(id));
    """)
    conn.commit()

if __name__ == '__main__':
    create_db()
