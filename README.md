# PDF to Audiobook Converter

Converts PDF files into audiobooks using **Python** and **Google Cloud Text-to-Speech API**.  
This project reads PDFs, cleans the text, splits it into manageable chunks, and generates MP3 audio files.

---
## How to use:
	Place your PDF file in data/input_pdfs/.
	Set the environment variable for your Google Cloud credentials: export GOOGLE_APPLICATION_CREDENTIALS=”/path/to/credentials.json”
	Run the script: python main.py
	The audio files will be saved in data/output_audio/.

##Tech Stack:
	•	Python 3
	•	Google Cloud Text-to-Speech API
	•	pdfplumber
	•	Regex (for text cleaning and chunking)

##Project Structure:

app/
pdf_reader.py
text_cleaner.py
text_chunker.py
data/
input_pdfs/
output_audio/
credentials/  (do NOT push to GitHub)
main.py
README.txt
