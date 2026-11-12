
from pathlib import Path
import sys

# Individua la cartella principale del progetto, partendo dalla posizione di questo file.
PROJECT_DIR = Path(__file__).parent.parent

sys.path.insert(0, str(PROJECT_DIR))

from parsers import TxtParser
from index import KnowledgeBase


data_dir = PROJECT_DIR / "data"

# Crea un documento utilizzando il parser TXT
parser = TxtParser()
document = parser.parse(data_dir / "procedura_produzione.txt")

# Crea una knowledge base
knowledge_base = KnowledgeBase()

# Aggiunge il documento alla knowledge base
knowledge_base.add_document(document)

# Verifica il numero di documenti
print("Numero di documenti:", knowledge_base.count_documents())

# Verifica la ricerca
results = knowledge_base.search("produzione")
print("Risultati della ricerca:", len(results))

# Verifica il filtro per formato
txt_documents = knowledge_base.filter_by_format("txt")
print("Documenti TXT:", len(txt_documents))

# Verifica le statistiche
print("Statistiche:", knowledge_base.get_statistics())

# Verifica il salvataggio e il caricamento del file JSON

json_path = PROJECT_DIR / "output" / "test_index.json"

# Salva la knowledge base
knowledge_base.save(json_path)

print("File JSON salvato:", json_path.exists())

# Crea una nuova knowledge base
loaded_knowledge_base = KnowledgeBase()

# Carica i documenti dal file JSON
loaded_knowledge_base.load(json_path)

print("Documenti caricati:", loaded_knowledge_base.count_documents())
print("Titolo del documento caricato:", loaded_knowledge_base.documents[0].title)
