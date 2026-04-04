from platform import system
from json import load
from faster_whisper import WhisperModel

with open(f"config/{system()}", "r") as os:
    config = load(os)

model = WhisperModel("small", compute_type=config["type"])

segments, info = model.transcribe("song.mp3", beam_size=15)

for segment in segments:
    print(segment.text)