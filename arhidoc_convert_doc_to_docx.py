from pathlib import Path

import docx
from doc2docx import convert as doc2docx_convert


def _iterdir(path: Path) -> list[Path]:
    """Получение списка файлов"""
    return [x for x in path.iterdir() if x.is_file()]


def validate_docx(path_file: Path, prefix: str, level: int = 1) -> None:
    """Валидация содержимого документов их данным согласно выгрузке из"""
    pass


if __name__ == '__main__':
    validate_docx(Path('D13.csv'), prefix='Л', level=1)