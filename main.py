import time
import pyautogui
from tkinter import*

def youtube():
    pyautogui.PAUSE = 0.3
    pyautogui.hotkey("win", "r")
    pyautogui.write("cmd")
    pyautogui.press("enter")
    pyautogui.write("start www.youtube.com")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.press("f11")
    time.sleep(2)
    pyautogui.click(x=1751, y=25)
    time.sleep(1)
    pyautogui.click(x=1660, y=73)


def instagram():
    pyautogui.PAUSE = 0.3
    pyautogui.hotkey("win", "r")
    pyautogui.write("cmd")
    pyautogui.press("enter")
    pyautogui.write("start www.instagram.com")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("f11")
    time.sleep(2)
    pyautogui.click(x=62, y=464)
    time.sleep(1)
    pyautogui.click(x=942, y=626)



Janela = Tk()
Janela.title("automatizar insta e shorts")
Janela.geometry("500x500")
Texto = Label(Janela, text="Clique no Botão e rode o programa")
Texto.grid(column=1, row=1)
logo2 = PhotoImage(file="reels.png",width=180, height=100)
botao = Button(Janela,image=logo2 ,command=lambda:instagram())
logo = PhotoImage(file="shorts.png", width=180, height= 100)
logo.subsample(3,3)

botao.grid(column=1, row=2)
botao2 = Button(Janela,image=logo, command=lambda:youtube())
botao2.grid(column=2, row=2)
def sair():
    Janela.destroy()

botao3 = Button(Janela,text="sair",command=lambda:sair())
botao3.grid(column=9, row=9)



Janela.mainloop()