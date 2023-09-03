import sqlite3
from pathlib import Path


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

def _iterdir(path: Path) -> list[Path]:
    """Получение списка файлов"""
    return [x for x in path.iterdir() if x.is_file()]


def get_base_dir():
    return Path(__file__).parent.joinpath('DOCS_FOR_DOWNLOAD')

def check_db():
    sqlite_insert_with_param = """SELECT dd.* 
                                FROM docbase_doc dd """
    cur.execute(sqlite_insert_with_param)
    conn.commit()

if __name__ == '__main__':
    create_db()
    check_db()
