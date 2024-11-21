import os

SOURCE_FILE = os.path.realpath(__file__)
SOURCE_DIR = os.path.dirname(SOURCE_FILE)
ROOT_DIR = os.path.dirname(SOURCE_DIR)
DATA_DIR = os.path.join(SOURCE_DIR, "DATA")


from pathlib import Path

SOURCE_FILE = Path(__file__).resolve()
SOURCE_DIR = SOURCE_FILE.parent
ROOT_DIR = SOURCE_DIR.parent
DATA_DIR = SOURCE_DIR / "DATA"