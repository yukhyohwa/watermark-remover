import os
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

def read_book(file_path):
    """Reads the content of a .txt or .epub file."""
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return None

    _, extension = os.path.splitext(file_path)
    if extension == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    elif extension == ".epub":
        book = epub.read_epub(file_path)
        content = []
        for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            soup = BeautifulSoup(item.get_content(), "html.parser")
            content.append(soup.get_text())
        return "\n".join(content)
    else:
        print(f"Unsupported file format: {extension}")
        return None
