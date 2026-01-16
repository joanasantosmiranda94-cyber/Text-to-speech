import os
from google.cloud import texttospeech
from app.pdf_reader import extract_text_from_pdf
from app.text_cleaner import clean_text
from app.text_chunker import chunk_text

credentials_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
if not credentials_path:
    raise ValueError("Por favor define a variável de ambiente GOOGLE_APPLICATION_CREDENTIALS")
# -------------------------------
# 2️⃣ Inicializa cliente TTS
# -------------------------------
client = texttospeech.TextToSpeechClient()

# -------------------------------
# 3️⃣ Lê e limpa PDF
# -------------------------------
pdf_path = "data/input_pdfs/sample.pdf"
raw_text = extract_text_from_pdf(pdf_path)
cleaned_text = clean_text(raw_text)

# -------------------------------
# 4️⃣ Divide em chunks
# -------------------------------
chunks = chunk_text(cleaned_text)

# -------------------------------
# 5️⃣ Converte cada chunk em áudio
# -------------------------------
output_folder = "data/output_audio/"
os.makedirs(output_folder, exist_ok=True)

for i, chunk in enumerate(chunks, start=1):
    synthesis_input = texttospeech.SynthesisInput(text=chunk)

    voice = texttospeech.VoiceSelectionParams(
        language_code="pt-PT",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    # salva cada chunk como mp3
    out_path = os.path.join(output_folder, f"chunk_{i}.mp3")
    with open(out_path, "wb") as out_file:
        out_file.write(response.audio_content)

    print(f"[✓] Saved: {out_path}")

print("\n✅ All chunks converted to audio!")