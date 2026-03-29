from platform import system
from json import load
from faster_whisper import WhisperModel

with open(f"config/{system()}", "r") as os:
    config = load(os)

model = WhisperModel(config["model"], compute_type=config["type"])

segments, info = model.transcribe("audio.mp3", beam_size=7)

for segment in segments:
    print(segment.text)