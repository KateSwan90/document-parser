# **Document Parser**

## **Descrizione del progetto**

Questo progetto è un parser sviluppato in Python che permette di leggere documenti in diversi formati, estrarre le informazioni principali e organizzarle in una knowledge base.

Il programma supporta tre formati:

* TXT  
* Markdown (MD)  
* CSV

## **Funzionalità principali**

* Lettura di file TXT, Markdown e CSV.  
* Estrazione del titolo, della data e del contenuto.  
* Calcolo del numero di parole.  
* Creazione di un breve estratto del documento.  
* Ricerca di documenti tramite parole chiave.  
* Filtraggio dei documenti per formato.  
* Creazione di statistiche.  
* Salvataggio e caricamento dei dati in formato JSON.  
* Gestione degli errori durante la lettura dei file.

## **Struttura del progetto**

* **data/** – contiene i documenti di esempio.  
* **output/** – contiene il file JSON generato.  
* **tests/** – contiene i file per testare il programma.  
* **models.py** – contiene la classe Document.  
* **parsers.py** – contiene i parser per i diversi formati.  
* **index.py** – gestisce la knowledge base e le ricerche.  
* **main.py** – avvia il programma.  
* **pyproject.toml** – contiene le informazioni necessarie per installare il progetto.  
* **README.md** – descrizione e istruzioni del progetto.  
* **requirements.txt** – contiene le eventuali dipendenze esterne.

## **Come installare il progetto**

### **Metodo 1: installazione da GitHub al nostro computer**

Clonare il repository:

```
git clone https://github.com/KateSwan90/document-parser.git
```

Entrare nella cartella del progetto:

```
cd document-parser
```

Creare un ambiente virtuale:

```
python -m venv venv
```

Attivare l'ambiente virtuale su Windows:

```
venv\Scripts\activate
```

Installare il progetto:

```
pip install .
```

### **Metodo 2: installazione direttamente da GitHub**

È possibile installare il progetto anche con un solo comando:

```
pip install git+https://github.com/KateSwan90/document-parser.git
```

## **Come avviare il progetto**

Dopo l'installazione, entrare nella cartella principale del progetto e avviare il programma con il comando:

```
document-parser
```

In alternativa, è possibile avviarlo con:

```
python main.py
```

Il risultato viene salvato nella cartella `output`, nel file `knowledge_base.json`.

## **Dipendenze**

Il progetto utilizza le librerie standard di Python e non richiede librerie esterne.

&nbsp;

&nbsp;

&nbsp;

&nbsp;