from whisper import load_model
from googletrans import Translator

import sys

def transcribe_and_translate(audio_path, target_lang="en"):
    # Load Whisper model
    model = load_model("small")

    # Check if audio path argument is provided
    if not audio_path:
        print("Error: Please provide an audio path as an argument.")
        return None

    # Transcribe audio
    try:
        result = model.transcribe(audio_path)
        text = result["text"]
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return None

    # Translate text
    translator = Translator()
    try:
        translated = translator.translate(text, dest=target_lang).text
    except Exception as e:
        print(f"Error translating text: {e}")
        return None

    return translated

# Get audio path from sys.argv
audio_path = sys.argv[1] if len(sys.argv) > 1 else None

import os

if os.path.exists(audio_path):
    print(f"Transcribing audio from: {audio_path}")
    translated_text = transcribe_and_translate(audio_path)
else:
    print(f"Error: File not found - {audio_path}")
    exit()

# Print the translated text
if translated_text:
    print(f"Translated text: {translated_text}")
