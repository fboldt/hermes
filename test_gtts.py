from tkinter import *
from gtts import gTTS
from playsound import playsound
 
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('data.mp3')
    playsound('data.mp3')
 
def Exit():
    window.destroy()
 
def Reset():
    Msg.set("")
     
window = Tk()
window.geometry("350x300") 
window.configure(bg='#FAD7A0')
window.title("TEXT TO SPEECH")
  
Label(window, text = "        TEXT TO SPEECH        ", font = "arial 20 bold", bg='black',fg="white").pack()
Msg = StringVar()
Label(window,text ="Enter Your Text Here: ", font = 'arial 20 bold', fg ='darkgreen').place(x=5,y=60)
 
entry_field = Entry(window, textvariable = Msg ,width ='30',font = 'arial 15 bold',bg="lightgreen")
entry_field.place(x=5,y=100)
 
Button(window, text = "PLAY TEXT", font = 'arial 15 bold' , command = Text_to_speech ,width = '20',bg = 'orchid',fg="white").place(x=35,y=140)
Button(window, font = 'arial 15 bold',text = 'RESET APPLICATION', width = '20' , command = Reset,bg = 'darkgreen',fg="white").place(x=35 , y = 190)
Button(window, font = 'arial 15 bold',text = 'EXIT APPLICATION', width = '20' , command = Exit, bg = 'red',fg="white").place(x=35 , y = 240)
 
window.mainloop()