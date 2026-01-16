# PDF to Audiobook Converter

Converts PDF files into audiobooks using **Python** and **Google Cloud Text-to-Speech API**.  
This project reads PDFs, cleans the text, splits it into manageable chunks, and generates MP3 audio files.

---

## Features

- Extract text from PDFs (`pdfplumber`)  
- Clean text from line breaks, hyphens, URLs, and references  
- Split text intelligently into chunks to respect TTS limits  
- Convert each chunk to audio using Google Cloud Text-to-Speech  
- Save audio files as MP3  

---

## Demo