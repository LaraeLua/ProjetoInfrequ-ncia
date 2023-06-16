from tkinter import *
from tkinter import Tk
from tkinter import messagebox
import pymysql
import datetime 

class Login:
    pass

agora = datetime.datetime.now()

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


janela = Tk()
janela.title('Login')
janela.geometry('500x350')
janela.configure(background=corBranca)
janela.resizable(width=FALSE, height=FALSE)
center(janela)

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
           
            connection = pymysql.connect(host="localhost", 
                                        user="root", 
                                        passwd="", 
                                        database="infrequencia")
            
            cursor = connection.cursor()
    
            sql = (f'SELECT * FROM cadastro WHERE senha = "{armazenar_senha}" AND cargo = "Professor"')

            cursor.execute(sql)

            myresult = cursor.fetchall()

            if myresult:
                
                janela.destroy()

                connection = pymysql.connect(host="localhost", 
                                    user="root", 
                                    passwd="", 
                                    database="infrequencia")
                cursor = connection.cursor()

                query = (f'INSERT INTO login (nome, data) VALUES ("{armazenar_nome}", "{agora}")')
                cursor.execute(query)
                print(query)   
                connection.commit()
                connection.close()

                from MenuProf import MenuProf
                MenuProf()
                
            else:
                janela.destroy()

                connection = pymysql.connect(host="localhost", 
                                    user="root", 
                                    passwd="", 
                                    database="infrequencia")
                cursor = connection.cursor()

                query = (f'INSERT INTO login (nome, data) VALUES ("{armazenar_nome}", "{agora}")')
                cursor.execute(query)
                print(query)    
                connection.commit()
                connection.close()

                from MenuSec import MenuCoord
                MenuCoord()        
        
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

senha = Entry(janela, show='***', width=40, bg=corBranca, fg=corRoxo)
senha.place(in_= senhaEnt, x=88, y=0, height=30)

botaoEnt = Button(janela, width=15, text='Entrar', font=("Arial", 10, "bold"), fg=corBranca, bg=corRoxo, command = menu)
botaoEnt.place(x=190, y=280)


janela.mainloop()