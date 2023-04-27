import time
import pyautogui
from tkinter import*
from tkinter import ttk
import webbrowser
import pygame

def youtube():
    webbrowser.open("https://youtube.com")
    time.sleep(3)
    pyautogui.click(x=1748, y=93)
    time.sleep(1)
    pyautogui.click(x=1658, y=136)


def instagram():
    webbrowser.open("https://instagram.com")
    time.sleep(2)
    pyautogui.click(x=39, y=525)
    time.sleep(1)
    pyautogui.click(x=943, y=636)


Janela = Tk()
Janela.configure(bg='#333333')
Janela.title("automatizar insta e shorts")
Janela.geometry("250x100")
Texto = Label(Janela, text="Clique no Botão e rode o programa", fg='white', bg='#333333')
Texto.grid(column=3,row=2)
logo2 = PhotoImage(file="reels.png",width=180, height=100)


logo = PhotoImage(file="shorts.png", width=180, height= 100)
logo.subsample(3,3)

var = IntVar()
rb_youtube = Radiobutton(Janela, text="Executar função do YouTube", variable=var, value=1, font="arial")
rb_youtube.grid(column=3, row=2)
rb_instagram = Radiobutton(Janela, text="Executar função do Instagram", variable=var, value=2, font="arial")
rb_instagram.grid(column=3, row=3)
def executar():
    if var.get() == 1:
        youtube()
    elif var.get() == 2:
        instagram()
botao_executar = Button(Janela, text="Executar", command=executar)
botao_executar.grid(column=3, row=4)


Janela.mainloop()