from tkinter import *
from tkinter import Tk
from tkinter import messagebox
import pymysql


corVerde = "#00FF00"
corBranca = "#fff"
corLaranja = "#da4f1c"
corPreta = "#000000"
corRoxo = "#8A2BE2"

class Cadastro:
    pass

janela = Tk()
janela.resizable(width=FALSE, height=FALSE)
janela.title("Cadastre-se")
janela.configure(background=corBranca)
janela.geometry("500x350")

# Definição que vai "pegar" o texto da lbl e salvar em uma variável global
def salvar_dados():

    armazenar_nome = email.get()
    armazenar_senha = senha.get()
    
    if armazenar_nome and armazenar_senha:
        print(armazenar_nome, armazenar_senha)
    
    
        connection = pymysql.connect(host="localhost", 
                                    user="root", 
                                    passwd="", 
                                    database="infrequencia")
        cursor = connection.cursor()

        query = (f'INSERT INTO cadastro(email, senha) VALUES ("{armazenar_nome}", "{armazenar_senha}")')
        cursor.execute(query)
        connection.commit()
        connection.close()
        messagebox.showinfo ("Aviso", 'Usuário Cadastrado!')
    else:
        messagebox.showinfo("Aviso", 'Usuário e senha inválidos!')


frame_cima = Frame(janela, width=500, height=50, relief='flat', bg=corRoxo)
frame_cima.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)


cadastrar = Label(frame_cima, text='CADASTRO', anchor=NE, font=("Arial", 20, "bold"), bg=corRoxo, fg=corBranca, padx=3, pady=5)
cadastrar.place(x=170, y=3)

emailCad = Label(janela, text='Usuário', font=("Arial", 15, "bold"), fg=corRoxo, bg=corBranca)
emailCad.place(x=85, y=130)

email = Entry(janela, width=40, bg=corBranca, fg=corRoxo)
email.place(in_=emailCad, x=88, y=0, height=30)

senhaCad = Label(janela, text='Senha', font=("Arial", 15, "bold"), fg=corRoxo, bg=corBranca)
senhaCad.place(x=85, y=180)

senha = Entry (janela, show="*", width=40, bg=corBranca, fg=corRoxo)
senha.place(in_=senhaCad, x=88, y=0, height=30)

botaoCad = Button(janela, width=15, text='Cadastrar', font=("Arial", 10, "bold"), fg=corBranca, bg=corRoxo,  command=salvar_dados)
botaoCad.place(x=290, y=250)

janela.mainloop()


