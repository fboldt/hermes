import tkinter as tk
import pyttsx3

def speak(event):
    text = entry.get()
    if text:  # Check if the text is not empty
        engine.say(text)
        engine.runAndWait()
        entry.delete(0, tk.END)  # Clear the entry after speaking

engine = pyttsx3.init()
portuguese_voice_id = "brazil"  # Replace this with the ID of the Portuguese voice
engine.setProperty('voice', portuguese_voice_id)

root = tk.Tk()
entry = tk.Entry(root)
entry.bind("<Return>", speak)  # Trigger TTS when Enter is pressed
entry.pack()
root.mainloop()
