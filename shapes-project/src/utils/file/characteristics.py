import os
from pathlib import Path


def get_file_size(file_path: str) -> int:
    return os.path.getsize(file_path)


def path_exists(path: str) -> bool:
    return Path(path).exists()
