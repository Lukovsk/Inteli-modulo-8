import whisper

model = whisper.load_model("base")
result = model.transcribe("amor_da_minha_vida.opus")