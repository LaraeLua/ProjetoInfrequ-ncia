from tkinter import *
from tkinter import Tk
from tkinter import messagebox
import pymysql
import datetime

agora = datetime.datetime.now()

corVerde = "#00FF00"
corBranca = "#fff"
corLaranja = "#da4f1c"
corPreta = "#000000"
corRoxo = "#8A2BE2"


janela = Tk()
janela.title('Login')
janela.geometry('500x350')
janela.configure(background=corBranca)
janela.resizable(width=FALSE, height=FALSE)

   
def CadastraJan():
    
    from Cadastro import Cadastro
    Cadastro()
   
#criando a aba login
def menu():
    
    armazenar_nome = email.get()
    armazenar_senha = senha.get()
    
    
    connection = pymysql.connect(host="localhost", 
                                    user="root", 
                                    passwd="", 
                                    database="infrequencia")
    cursor = connection.cursor()

    query = (f'SELECT * FROM cadastro WHERE email = "{armazenar_nome}" AND senha = "{armazenar_senha}"')
    cursor.execute(query)
    results = cursor.fetchall()    
    connection.commit()
    connection.close()

    if results:

       for i in results:
        from Menu import menu
        menu()

        connection = pymysql.connect(host="localhost",
                                     user="root",
                                     passwd="",
                                     database="infrequencia")
        cursor = connection.cursor()

        query = (f'INSERT INTO login(nome, data) VALUES ("{armazenar_nome}", "{agora}")')
        cursor.execute(query)
        connection.commit()
        connection.close()



    else:
     messagebox.showinfo("Aviso", 'Usuário e senha inválidos!')



#dividindo a janela
frame_cima = Frame(janela, width=500, height=50, relief='flat', bg=corRoxo)
frame_cima.grid(row=0, column=0, pady=5, padx=0, sticky=NSEW)

#configurando o frame cima
l_login = Label(frame_cima, text='LOGIN', anchor=NE, font=("Arial", 20, "bold"), bg=corRoxo, fg=corBranca, padx=3, pady=5)
l_login.place(x=200, y=3)


emailEnt = Label(janela, text='Usuário', font=("Arial", 15, "bold"), fg=corRoxo, bg=corBranca)
emailEnt.place(x=85, y=130)

email = Entry(janela, width=40, bg=corBranca, fg=corRoxo)
email.place(in_= emailEnt, x=88, y=0, height=30)

senhaEnt = Label(janela, text='Senha', font=("Arial", 15, "bold"), fg=corRoxo, bg=corBranca)
senhaEnt.place(x=85, y=180)


senha = Entry(janela, show="*", width=40, bg=corBranca, fg=corRoxo)
senha.place(in_= senhaEnt, x=88, y=0, height=30)

botaoEnt = Button(janela, width=15, text='Entrar', font=("Arial", 10, "bold"), fg=corBranca, bg=corRoxo, command = menu)
botaoEnt.place(x=85, y=250)

botaoCad = Button(janela, width=15, text='Cadastrar', font=("Arial", 10, "bold"), fg=corBranca, bg=corRoxo, command = CadastraJan)
botaoCad.place(x=290, y=250)

janela.mainloop()
