import torch
from TTS.api import TTS
import os

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

texts = [
    "Claro! Vou pegar o fardo um no corredor cinco. Deseja que o comando seja executado?",
    # "Sem problemas, estou aqui para ajudar. Se precisar de alguma coisa, é só me avisar.",
    # "Sim, entendi! Você deseja que eu pegue o fardo dois do corredor quatro, certo?",
    # "Desculpe, mas o armazém só possui corredores numerados de um a cinco. Por favor, forneça um número de corredor válido.",
    # "Desculpe, mas não posso executar essa ação. As pilhas de carga são numeradas de um a dez. Não existe a pilha onze. Por favor, forneça um número de pilha válido.",
    # "Por favor, forneça mais informações sobre o local onde o caminhão está e qual é o fardo que você deseja entregar.",
    ]
text = ""
for t in texts:
    text += t + " "
    
def get_file_path():
    output_dir = "output"
    id = len(os.listdir(output_dir))+1
    file_path = os.path.join(output_dir, f"output_{id}.wav")
    return file_path

'''
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
'''
tts = TTS("tts_models/multilingual/multi-dataset/your_tts").to(device)
#'''
tts.tts_to_file(text=text, 
                speaker_wav="input/francisco.wav", 
                language="pt-br", 
                file_path=get_file_path())

