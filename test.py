from faster_whisper import WhisperModel


model = WhisperModel("small", compute_type="int8")

segments, info = model.transcribe("audio.mp3", beam_size=7)

for segment in segments:
    print(segment.text)