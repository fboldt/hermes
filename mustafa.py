# https://www.youtube.com/watch?v=EyzRixV8s54

import torch
from TTS.api import TTS
import gradio as gr
import os

device = "cuda" if torch.cuda.is_available() else "cpu"
output_dir = "output"

def get_file_path():
    id = len([name for name in os.listdir('./output/') if os.path.isfile(name)])+1
    file_path = os.path.join(output_dir, f"output_{id}.wav")
    return file_path

def generate_audio(text, model_name):
    tts = TTS(model_name).to(device)
    file_path=get_file_path()
    tts.tts_to_file(text=text, speaker_wav="input/francisco.wav", language="pt-br", file_path=file_path)
    return file_path

text = "Uma jornada de mil milhas começa com um único passo."
model_name = "tts_models/multilingual/multi-dataset/your_tts"
print(generate_audio(text, model_name))

# demo =  gr.Interface(fn=generate_audio, 
#                      inputs=[gr.Text(label="text"),], 
#                      outputs=[gr.Audio(label="audio"),], 
#                      title="Text to Speech") 

