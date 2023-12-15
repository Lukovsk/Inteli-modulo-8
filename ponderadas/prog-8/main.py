from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
import playsound
import sys
from random import randint
import os

class Trans2Rep:
    def __init__(self):
        pass
    
    def transcribe(self, path) -> str:
        recognizer = sr.Recognizer()
        audio_file = sr.AudioFile(path)
        
        with audio_file as f:
            data = recognizer.record(f)

        try: 
            return recognizer.recognize_google(data, language="pt-BR")
        except sr.UnknownValueError:
            return "Áudio incompreensível"
        except sr.RequestError:
            return "Falha na requisição ao serviço de reconhecimento de fala"
        except Exception as e:
            return "Erro: " + str(e)

    def translate(self, text):
        translator = Translator()
        new_text = translator.translate(text, src="pt", dest="en")
        return new_text.text
    
    def reproduce(self, text):
        tts = gTTS(text=text, lang="en")
        
        new_file_name = f"./outputs/output-{randint(0, 100)}.wav"
        
        tts.save(new_file_name)
        try:
            playsound.playsound(new_file_name)
        except Exception as e:
            print("Failed to play sound: " + str(e))
        # os.remove(f"./{new_file_name}")
        
def main():
    TTR = Trans2Rep()
    
    audio_path = sys.argv[1]
    
    transcription = TTR.transcribe(audio_path)
    print(f"Compreendido: '{transcription}'")
    
    translation = TTR.translate(transcription)
    print(f"In english: '{translation}'")
    
    TTR.reproduce(translation)


if __name__ == '__main__':
    main()