
from pathlib import Path
import csv
from models import Document
from datetime import datetime

#Definizione delle nostre eccezioni

class UnsupportedFormatError(Exception):
    """Viene sollevata quando il formato di un file non è supportato"""


class UnreadableFileError(Exception):
    """Viene sollevata quando non è possibile leggere un file"""


class EmptyDocumentError(Exception):
    """Viene sollevata quando un documento non contiene testo"""


class CorruptedDocumentError(Exception):
    """Viene sollevata quando un documento contiene dati non validi"""


def extract_date(content):
    """Cerca una data nel contenuto e la restituisce nel formato DD/MM/YYYY."""

    date_formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%d-%m-%Y"
    ]

    words = content.split()

    for word in words:
        for date_format in date_formats:
            try:
                date = datetime.strptime(word, date_format)
                return date.strftime("%d/%m/%Y")
            except ValueError:
                continue

    return None

# Definizione della classe base

class BaseParser:
    """Definisce il comportamento comune dei parser."""

    def read_content(self, file_path):
        """Legge il contenuto di un file e gestisce errori più comuni"""

        file_path = Path(file_path)

        if not file_path.exists():
            raise UnreadableFileError(f"Il file non esiste: {file_path}")

        if not file_path.is_file():
            raise UnreadableFileError(f"Il percorso non corrisponde a un file{file_path}")

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

        except (OSError, UnicodeDecodeError) as error:
            raise UnreadableFileError(f"Impossibile leggere il file {file_path}: {error}")

        if not content:
            raise EmptyDocumentError(f"Il documento è vuoto: {file_path}")

        return content

    def parse(self, file_path):
        """Legge un file e restituisce un documento normalizzato"""
        raise NotImplementedError("Subclasses devono implementare il metodo parse()")

#Creare subclasses

class TxtParser(BaseParser):
    """Gestisce la lettura dei file di testo."""

    def parse(self, file_path):
        """Legge un file di testo e crea un oggetto Document."""

        file_path = Path(file_path)
        content = self.read_content(file_path)

        title = file_path.stem

        return Document(
            title=title,
            date=extract_date(content),
            content=content,
            source_format="txt"
        )


class MarkdownParser(BaseParser):
    """Gestisce la lettura dei file Markdown."""

    def parse(self, file_path):
        """Legge un file Markdown e crea un oggetto Document."""

        file_path = Path(file_path)
        content = self.read_content(file_path)

        title = file_path.stem

        return Document(
            title=title,
            date=extract_date(content),
            content=content,
            source_format="md"
        )


class CsvParser(BaseParser):
    """Gestisce la lettura dei file CSV."""

    def parse(self, file_path):
        """Legge un file CSV, verifica la struttura e crea un oggetto Document."""

        file_path = Path(file_path)
        self.read_content(file_path)

        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            rows = list(reader)

        expected_columns = len(rows[0])

        for row_number, row in enumerate(rows[1:], start=2):
            if len(row) != expected_columns:
                raise CorruptedDocumentError(
                    f"Struttura CSV non valida alla riga {row_number}: {file_path}"
                )

        content = ""
        for row in rows:
            content += " ".join(row) + "\n"

        title = file_path.stem

        return Document(
            title=title,
            date=extract_date(content),
            content=content,
            source_format="csv"
        )

def get_parser(file_path):
    """Restituisce il parser appropriato in base al formato del file."""

    file_path = Path(file_path)
    suffix = file_path.suffix.lower()

    if suffix == ".txt":
        return TxtParser()

    elif suffix == ".md":
        return MarkdownParser()

    elif suffix == ".csv":
        return CsvParser()

    else:
        raise UnsupportedFormatError(f"Formato di file non supportato: {suffix}")
