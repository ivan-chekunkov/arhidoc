from typing import Generator
import sqlite3
from datetime import datetime
from pathlib import Path
import json

conn = sqlite3.connect("arhidoc\\db.sqlite3")
cur = conn.cursor()


def create_db():
    cur.execute(
        """CREATE TABLE IF NOT EXISTS cat(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT);
    """
    )
    cur.execute(
        """CREATE TABLE IF NOT EXISTS docs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date datetime,
    name TEXT,
    number TEXT,
    category TEXT,
    file_path TEXT,
    cat_id INTEGER,
    FOREIGN KEY (cat_id) REFERENCES cat(id));
    """
    )
    conn.commit()


def _iterdir(path: Path) -> list[Path]:
    """Получение списка файлов"""
    return [x for x in path.iterdir() if x.is_file()]


def get_base_dir():
    return Path(__file__).parent.joinpath("DOCS_FOR_DOWNLOAD")


def get_data(files: list[Path]) -> Generator:
    with open("D12.json", "r", encoding="utf-8") as json_file:
        D12 = json.load(json_file)
    with open("D13.json", "r", encoding="utf-8") as json_file:
        D13 = json.load(json_file)
    json_data = {"Л": D12, "К": D13}
    for file in files:
        cat = file.name.split("=")[0]
        index = file.name.split("=")[1][1:].lstrip("0")
        data = json_data[cat][index]
        data_doc = str(datetime.strptime(data[0], "%Y-%m-%d"))
        cat_num = {"Л": 1, "К": 2}[cat]
        yield (data[2], data[1], data_doc, cat_num, data_doc, str(file))


def add_line(data_tuple):
    sqlite_insert_with_param = """INSERT INTO 'docbase_doc'
                          ('name', 'number', 'pub_create', 'category_id', 'data_doc', 'file_path')
                          VALUES (?, ?, ?, ?, ?, ?);"""

    cur.execute(sqlite_insert_with_param, data_tuple)
    conn.commit()


def check_db():
    sqlite_insert_with_param = """SELECT dd.* 
                                FROM docbase_doc dd """
    cur.execute(sqlite_insert_with_param)
    conn.commit()


if __name__ == "__main__":
    # create_db()
    files = _iterdir(get_base_dir())

    for data_tuple in get_data(files):
        add_line(data_tuple)

    # check_db()
