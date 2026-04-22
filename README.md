# Hears

Real-time speech-to-text desktop application for generating structured, editable notes.

Hears converts spoken conversations into text instantly, enabling faster documentation and reducing manual note-taking effort.

---

## Overview

Capturing information during conversations—especially in professional settings—can be slow and error-prone.

Manual note-taking:
- interrupts focus  
- misses important details  
- adds post-processing overhead  

Hears solves this by transcribing speech in real time into a live, editable document.

---

## Features

- Real-time speech-to-text transcription  
- Live document editing during transcription  
- Persistent storage for saving and revisiting notes  
- Cross-platform support (Linux / Windows)  
- Simple desktop interface with integrated controls  

---

## Example Workflow

```
Start Recording → Speak → Live Transcription Appears → Edit → Save Document
```

---

## How It Works

### 1. Audio Capture
- Records audio input using system microphone  

### 2. Transcription
- Processes audio using Whisper-based speech recognition  

### 3. Live Rendering
- Displays transcribed text inside a GUI document interface  

### 4. Editing & Storage
- Allows real-time editing and saving of notes  

---

## Architecture

```
Microphone Input
        ↓
Audio Capture (PyAudio)
        ↓
Speech Processing (Whisper)
        ↓
Text Output Stream
        ↓
GUI Document Editor
        ↓
File Storage
```

---

## Use Cases

- Medical note-taking  
- Interviews and research  
- Meetings and discussions  
- Personal voice notes  

---

## Challenges

- Real-time processing latency  
- Handling noisy audio environments  
- Balancing transcription speed vs accuracy  

---

## Impact

Hears reduces the friction between **conversation and documentation**, allowing users to focus on interaction while the system handles transcription.
