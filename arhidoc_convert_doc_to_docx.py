from pathlib import Path

import docx
from doc2docx import convert as doc2docx_convert


def _iterdir(path: Path) -> list[Path]:
    """Получение списка файлов"""
    return [x for x in path.iterdir() if x.is_file()]