import whisper

model = whisper.load_model("tiny")
result = model.transcribe("transcript.mp3", language="es")
print(result["text"])
