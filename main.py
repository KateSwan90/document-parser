
from pathlib import Path

from parsers import (
    get_parser,
    UnsupportedFormatError,
    UnreadableFileError,
    EmptyDocumentError,
    CorruptedDocumentError
)
from index import KnowledgeBase


# Definizione delle cartelle del progetto
PROJECT_DIR = Path(__file__).parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "output"


def main():
    """Avvia il processo di lettura e indicizzazione dei documenti."""

    # Recupera i file presenti nella cartella data
    files = list(DATA_DIR.iterdir())

    # Crea la knowledge base
    knowledge_base = KnowledgeBase()

    # Inizializza il contatore dei file non elaborati
    skipped_files = 0
    skipped_details = []

    # Elabora i file e aggiunge i documenti alla knowledge base
    for file_path in files:
        if file_path.is_file():
            try:
                parser = get_parser(file_path)
                document = parser.parse(file_path)
                knowledge_base.add_document(document)

            except UnsupportedFormatError as error:
                print(f"Formato non supportato: {error}")
                skipped_files += 1
                skipped_details.append({
                    "file": file_path.name,
                    "reason": str(error)
                })

            except (
                UnreadableFileError,
                EmptyDocumentError,
                CorruptedDocumentError
            ) as error:
                print(f"Impossibile elaborare il file: {error}")
                skipped_files += 1
                skipped_details.append({
                    "file": file_path.name,
                    "reason": str(error)
                })

    print(f"Documenti elaborati correttamente: {knowledge_base.count_documents()}")

    # Salva la knowledge base
    output_file = OUTPUT_DIR / "knowledge_base.json"
    knowledge_base.save(output_file)

    print(f"Knowledge base salvata in: {output_file}")
    print(f"File non elaborati: {skipped_files}")

    if skipped_details:
        print("\nDettagli dei file non elaborati:")

        for item in skipped_details:
            print(f"File: {item['file']}")
            print(f"Motivo: {item['reason']}")


if __name__ == "__main__":
    main()
