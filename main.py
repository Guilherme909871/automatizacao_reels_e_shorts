import time
import pyautogui
from tkinter import*
import webbrowser

def youtube():
    webbrowser.open("https://youtube.com")
    time.sleep(2)
    pyautogui.press("f11")
    time.sleep(2)
    pyautogui.click(x=1751, y=25)
    time.sleep(1)
    pyautogui.click(x=1660, y=73)


def instagram():
    webbrowser.open("https://instagram.com")
    time.sleep(2)
    pyautogui.press("f11")
    time.sleep(2)
    pyautogui.click(x=62, y=464)
    time.sleep(1)
    pyautogui.click(x=942, y=626)



Janela = Tk()
Janela.title("automatizar insta e shorts")
Janela.geometry("800x800")
Texto = Label(Janela, text="Clique no Botão e rode o programa", bg="yellow", fg="red")
Texto.grid(column=3,row=2)
#2 = PhotoImage(file="n.png")
#imagem = Label(Janela, image=imagem2)
#imagem.grid(column=0,row=0)

logo2 = PhotoImage(file="reels.png",width=180, height=100)
botao = Button(Janela,image=logo2 ,command=lambda:instagram())
logo = PhotoImage(file="shorts.png", width=180, height= 100)
logo.subsample(3,3)

botao.grid(column=3, row=4)
botao2 = Button(Janela,image=logo, command=lambda:youtube())
botao2.grid(column=4, row=4)
def sair():
    Janela.destroy()

botao3 = Button(Janela,text="sair",command=lambda:sair())
botao3.grid(column=9, row=9)



Janela.mainloop()