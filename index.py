
import json
from pathlib import Path
from models import Document

# Define the KnowledgeBase class
class KnowledgeBase:
    """Store and manage the document collection."""

    def __init__(self):
        """Initialize an empty knowledge base."""
        self.documents = []

    def add_document(self, document):
        """Add a document to the knowledge base."""
        self.documents.append(document)

    def count_documents(self):
        """Return the number of documents in the knowledge base."""
        return len(self.documents)

    def search(self, query):
        """Search documents by title or content."""
        query = query.lower()

        results = []

        if not query.strip():
          return []

        for document in self.documents:
            if (
                query in document.title.lower()
                or query in document.content.lower()
            ):
                results.append(document)

        return results

    def filter_by_format(self, suffix):
        """Filter documents by their source format."""
        suffix = suffix.lower()

        filtered_documents = []

        for document in self.documents:
            if document.source_format.lower() == suffix:
                filtered_documents.append(document)

        return filtered_documents


    def get_statistics(self):
        """Return statistics about stored documents."""

        total_txt_documents = 0
        total_md_documents = 0
        total_csv_documents = 0

        for document in self.documents:
            if document.source_format == "txt":
                total_txt_documents += 1
            elif document.source_format == "md":
                total_md_documents += 1
            elif document.source_format == "csv":
                total_csv_documents += 1

        longest_documents = sorted(
            self.documents,
            key=lambda document: document.word_count,
            reverse=True
        )[:3]

        longest_documents_data = []

        for document in longest_documents:
            document_data = {
                "title": document.title,
                "word_count": document.word_count
            }

            longest_documents_data.append(document_data)

        statistics = {
            "total_documents": len(self.documents),
            "formats": {
                "txt": total_txt_documents,
                "md": total_md_documents,
                "csv": total_csv_documents
            },
            "longest_documents": longest_documents_data
        }

        return statistics


    def save(self, file_path):
        """Save the knowledge base to a JSON file."""

        data = []

        for document in self.documents:
            document_data = {
                "title": document.title,
                "date": document.date,
                "content": document.content,
                "source_format": document.source_format
            }

            data.append(document_data)

        file_path = Path(file_path)

        with file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)


    def load(self, file_path):
        """Load documents from a JSON file."""

        file_path = Path(file_path)

        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        self.documents = []

        for document_data in data:
            document = Document(
                title=document_data["title"],
                date=document_data["date"],
                content=document_data["content"],
                source_format=document_data["source_format"]
            )

            self.documents.append(document)
