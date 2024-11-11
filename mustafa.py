# https://www.youtube.com/watch?v=EyzRixV8s54

import torch
from TTS.api import TTS
import gradio as gr
import os

devide = "cuda" if torch.cuda.is_available() else "cpu"
output_dir = "output"
id = len([name for name in os.listdir('.') if os.path.isfile(name)])+1

def generate_audio(text):
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
    file_path = os.path.join(output_dir, f"output_{id}.wav")
    tts.tts_to_file(text=text, file_path=file_path)
    return file_path

# print(generate_audio("Hello world!"))

demo =  gr.Interface(fn=generate_audio, 
                     inputs=[gr.Text(label="text"),], 
                     outputs=[gr.Audio(label="audio"),], 
                     title="Text to Speech") 

