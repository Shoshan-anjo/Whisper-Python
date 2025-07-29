import sounddevice as sd
from scipy.io.wavfile import write
import whisper

fs = 44100  # Hz
seconds = 5
print("🎙️ Grabando...")
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()
write("mi_audio.wav", fs, recording)
print("✅ Grabación guardada como 'mi_audio.wav'")

# Transcribir con Whisper
model = whisper.load_model("base")
result = model.transcribe("mi_audio.wav", language="es")
print("📝 Transcripción:", result["text"])
