
#Definizione della classe Document

class Document:
    """Rappresenta un documento normalizzato."""

    def __init__(
        self,
        title,
        date,
        content,
        source_format
    ):

        self.title = title
        self.date = date
        self.source_format = source_format
        self.content = content
        words = content.split()
        self.word_count = len(words)
        self.excerpt = " ".join(words[:30]) #Breve estratto del documento
