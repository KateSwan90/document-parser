
from pathlib import Path
import sys

# Individuare la cartella principale del progetto, partendo dalla posizione di questo file.
PROJECT_DIR = Path(__file__).parent.parent

sys.path.insert(0, str(PROJECT_DIR))

from models import Document
from parsers import (
    TxtParser,
    MarkdownParser,
    CsvParser,
    get_parser,
    EmptyDocumentError,
    UnreadableFileError,
    UnsupportedFormatError,
    CorruptedDocumentError
)

data_dir = Path("/content/drive/MyDrive/Parser/data")


# Test 1: parser TXT
txt_parser = TxtParser()
document = txt_parser.parse(data_dir / "procedura_produzione.txt")

print("Documento TXT")
print("Titolo:", document.title)
print("Data:", document.date)
print("Formato originale:", document.source_format)
print("Numero di parole:", document.word_count)
print("Estratto:", document.excerpt)
print()

# Test 2: Parser Markdown
md_parser = MarkdownParser()
document = md_parser.parse(data_dir / "controllo_qualita.md")

print("Documento Markdown")
print("Titolo:", document.title)
print("Data:", document.date)
print("Formato originale:", document.source_format)
print("Numero di parole:", document.word_count)
print("Estratto:", document.excerpt)
print()


# Test 3: Parser CSV
csv_parser = CsvParser()
document = csv_parser.parse(data_dir / "produzione_mensile.csv")

print("Documento CSV")
print("Titolo:", document.title)
print("Data:", document.date)
print("Formato originale:", document.source_format)
print("Numero di parole:", document.word_count)
print("Estratto:", document.excerpt)
print()


# Test 4: File vuoto
try:
    txt_parser.parse(data_dir / "problematico_vuoto.txt")
except EmptyDocumentError as error:
    print("File vuoto gestito correttamente:", error)
print()


# Test 5: File inesistente
try:
    txt_parser.parse(data_dir / "inesistente.txt")
except UnreadableFileError as error:
    print("File inesistente gestito correttamente:", error)

# Test 6: File con caratteri non validi

try:
    txt_parser.parse(data_dir / "caratteri_non_validi.txt")
except UnreadableFileError as error:
    print("File con caratteri non validi gestito correttamente:", error)

# Test 7: Formato non supportato

try:
    get_parser(data_dir / "formato_non_supportato.pdf")
except UnsupportedFormatError as error:
    print("Formato non supportato gestito correttamente:", error)

# Test 8: CSV con struttura non valida

try:
    csv_parser.parse(data_dir / "csv_struttura_irregolare.csv")
except CorruptedDocumentError as error:
    print("File CSV non valido gestito correttamente:", error)
