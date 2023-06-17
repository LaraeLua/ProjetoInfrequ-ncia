from tkinter import *
from tkinter import Tk

corVerde = "#00FF00"
corBranca = "#fff"
corLaranja = "#da4f1c"
corPreta = "#000000"
corRoxo = "#8A2BE2"

class MenuProf:
    pass

def Chamada_1():
    janela.destroy() 
    from Chamada_1 import Chamada_1
    Chamada_1()
    return

def Chamada_2():
    janela.destroy() 
    from Chamada_2 import Chamada_2
    Chamada_2()
    return

def Chamada_3():
    janela.destroy() 
    from Chamada_3 import Chamada_3
    Chamada_3()
    return

def center(janela):
    janela.update_idletasks()

    width = janela.winfo_width()
    frm_width = janela.winfo_rootx() - janela.winfo_x()
    janela_width = width + 2 * frm_width

    height = janela.winfo_height()
    titlebar_height = janela.winfo_rooty() -janela.winfo_y()
    janela_height = height + titlebar_height + frm_width

    x = janela.winfo_screenwidth() // 2 - janela_width // 2
    y = janela.winfo_screenheight() // 2 - janela_height // 2

    # this is the line that will center your window
    janela.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    janela.deiconify()

janela = Tk()
janela.title('Menu')
janela.geometry('500x350')
janela.configure(background=corBranca)
janela.resizable(width=FALSE, height=FALSE)
center(janela)

#dividindo a janela
frame_cima = Frame(janela, width=500, height=50, relief='flat', bg=corRoxo)
frame_cima.grid(row=0, column=0, pady=5, padx=0, sticky=NSEW)

#configurando o frame cima
l_login = Label(frame_cima, text='Menu', anchor=NE, font=("Arial", 20, "bold"), bg=corRoxo, fg=corBranca, padx=3, pady=5)
l_login.place(x=200, y=3)

botaoCad = Button(janela, width=15, text='1º : Informática', font=("Arial", 10, "bold"), fg=corBranca, bg=corRoxo, command = Chamada_1)
botaoCad.place(x=185, y=120)

botaoCad = Button(janela, width=15, text='2º : Informática', font=("Arial", 10, "bold"), fg=corBranca, bg=corRoxo, command = Chamada_2)
botaoCad.place(x=185, y=155)

botaoCad = Button(janela, width=15, text='3º : Informática', font=("Arial", 10, "bold"), fg=corBranca, bg=corRoxo, command = Chamada_3)
botaoCad.place(x=185, y=190)


janela.mainloop()