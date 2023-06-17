from tkinter import *
from tkinter import Tk
from tkinter import messagebox
import pymysql

def Login():
    janela.destroy()
    from Login import Login
    Login()
    
    
corVerde = "#00FF00"
corBranca = "#fff"
corLaranja = "#da4f1c"
corPreta = "#000000"
corRoxo = "#8A2BE2"

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


def salvar_dados():

    global armazenar_nome
    global armazenar_senha
    global cargo
    global disciplina

    
    armazenar_nome = email.get()
    armazenar_senha = senha.get()
    cargo = opts.get()
    disciplina = discVar.get()
    
    if armazenar_nome and armazenar_senha and cargo == "Professor" and disciplina:
        
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
            messagebox.showinfo("Aviso", 'Usuário já existe!')
            
        else:
    
            connection = pymysql.connect(host="localhost", 
                                        user="root", 
                                        passwd="", 
                                        database="infrequencia")
            cursor = connection.cursor()

            query = (f'INSERT INTO cadastro(email, senha, cargo, disciplina) VALUES ("{armazenar_nome}", "{armazenar_senha}", "{cargo}", "{disciplina}")')
            cursor.execute(query)
            connection.commit()
            connection.close()
            messagebox.showinfo ("Aviso", 'Usuário Cadastrado!')

            email.delete(0, END)
            senha.delete(0, END)
            opts.set(0)
            discVar.delete(0, END)

    elif armazenar_nome and armazenar_senha and cargo == "Coordenação":
        
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
            messagebox.showinfo("Aviso", 'Usuário já existe!')
            
        else:
            
            connection = pymysql.connect(host="localhost", 
                                        user="root", 
                                        passwd="", 
                                        database="infrequencia")
            cursor = connection.cursor()

            query = (f'INSERT INTO cadastro(email, senha, cargo) VALUES ("{armazenar_nome}", "{armazenar_senha}", "{cargo}")')
            cursor.execute(query)
            connection.commit()
            connection.close()
            messagebox.showinfo ("Aviso", 'Usuário Cadastrado!')

            email.delete(0, END)
            senha.delete(0, END)
            opts.set(0)
            discVar.delete(0, END)

    else:
        messagebox.showinfo("Aviso", 'Preencha todos os campos!')


def estado():
    cargo = opts.get()

    if cargo == "Professor":
        discVar['state'] = NORMAL
    
    else:
        discVar.delete(0, END)
        discVar['state'] = DISABLED



janela = Tk()
janela.resizable(width=FALSE, height=FALSE)
janela.title("Cadastre-se")
janela.configure(background=corBranca)
janela.geometry("500x450")
center(janela)

global email
global senha

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

opts = StringVar()
opts.set(0)
prof = Radiobutton(janela, text='Professor(a)', font=("Arial", 10, "bold"), fg=corPreta, bg=corBranca, variable = opts, value= "Professor", command=estado)
prof.place(x=100, y=270, anchor = 'w')

coord = Radiobutton(janela, text='Coordenação', font=("Arial", 10, "bold"), fg=corPreta, bg=corBranca, variable = opts, value="Coordenação", command=estado)
coord.place(x=290, y=270, anchor = 'w')

disc = Label(janela, text='Disciplina', font=("Arial", 12, "bold"), fg=corRoxo, bg=corBranca)
disc.place(x=84, y=300)

discVar = Entry (janela, width=40, bg=corBranca, fg=corRoxo, state=DISABLED)
discVar.place(in_=disc, x=88, y=0, height=30)

botaologa = Button(janela, width=15, text='Login', font=("Arial", 10, "bold"), fg=corBranca, bg=corRoxo, command = Login)
botaologa.place(x=85, y=380)

botaoCad = Button(janela, width=15, text='Cadastrar', font=("Arial", 10, "bold"), fg=corBranca, bg=corRoxo,  command= salvar_dados)
botaoCad.place(x=290, y=380)


janela.mainloop()


