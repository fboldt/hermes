import torch
from TTS.api import TTS

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

# List available 🐸TTS models
print(TTS().list_models())

# Init TTS
tts = TTS("tts_models/multilingual/multi-dataset/your_tts").to(device)

text = "A journey os a thousand miles begins with a single step."

# Run TTS
# ❗ Since this model is multi-lingual voice cloning model, we must set the target speaker_wav and language
# Text to speech list of amplitude values as output
# wav = tts.tts(text=text, speaker_wav="input/francisco.wav", language="en")
# Text to speech to a file
tts.tts_to_file(text=text, speaker_wav="input/francisco.wav", language="en", file_path="output/output.wav")

