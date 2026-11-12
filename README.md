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
* **README.md** – descrizione del progetto.  
* **requirements.txt** – contiene le dipendenze del progetto.

## **Come avviare il progetto**

1. Installare Python.  
2. Aprire il terminale nella cartella del progetto.  
3. Creare un ambiente virtuale:  
   `python -m venv venv`  
4. Attivare l'ambiente virtuale su Windows:  
   `venv\Scripts\activate`  
5. Avviare il programma:  
   `python main.py`

Il risultato viene salvato nella cartella `output`, nel file `knowledge_base.json`.

## **Dipendenze**

Il progetto utilizza le librerie standard di Python e non richiede librerie esterne.

&nbsp;

&nbsp;

&nbsp;