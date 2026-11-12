
from pathlib import Path
import sys
import parsers

PROJECT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_DIR))

data_dir = PROJECT_DIR / "data"

from parsers import extract_date

# Test TXT
txt_document = parsers.TxtParser().parse(
    data_dir / "procedura_produzione.txt"
)

# Test Markdown
md_document = parsers.MarkdownParser().parse(
    data_dir / "controllo_qualita.md"
)

# Test CSV
csv_document = parsers.CsvParser().parse(
    data_dir / "produzione_mensile.csv"
)

print("TXT:", txt_document.date)
print("Markdown:", md_document.date)
print("CSV:", csv_document.date)
