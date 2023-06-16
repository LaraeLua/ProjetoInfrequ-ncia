from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
import datetime 

aberto = datetime.datetime.now()   

corRoxo = "#8A2BE2"

class Chamada_2:
    pass


def inserir():    
    global armazenar_nmr
    global armazenar_nome
    global armazenar_hor
    global armazenar_serie
    global hoje

    if vnmr.get()=="" or vnome.get()=="" or vhor.get()=="" or vserie.get()=="":
        messagebox.showinfo(title="ERRO", message="Digite todos os dados")
        return
    
    else:
        tv.insert("","end", values=(vnmr.get(), vnome.get(), vhor.get(), vserie.get()))

        hoje = datetime.datetime.now()
        armazenar_nmr = vnmr.get()
        armazenar_nome = vnome.get()
        armazenar_hor = vhor.get()
        armazenar_serie = vserie.get()

        connection = pymysql.connect(host="localhost",
                                    user="root",
                                    passwd="",
                                    database="infrequencia")
        cursor = connection.cursor()

        query = (f'INSERT INTO segundo (numero, nome, horario, serie, data) VALUES ("{armazenar_nmr}", "{armazenar_nome}",  "{armazenar_hor}",  "{armazenar_serie}", "{hoje}")')
        cursor.execute(query)
        print(query)
        connection.commit()
        connection.close()
        
        vnmr.delete(0, END)
        vnome.delete(0, END)
        vhor.delete(0, END)
        vserie.focus()


def deletar(): 
    if messagebox.askokcancel(title="CONFIRME", message="Você deseja deletar? "):

        item_selecionado = tv.selection()[0]
        tv.delete(item_selecionado)
    
        global armazenar_nmr
        global armazenar_nome
        global armazenar_hor
        global armazenar_serie


        connection = pymysql.connect(host="localhost",
                                    user="root",
                                    passwd="",
                                    database="infrequencia")
        cursor = connection.cursor()

        query = (f'DELETE FROM segundo WHERE numero = "{armazenar_nmr}" and nome = "{armazenar_nome}" and horario = "{armazenar_hor}" and serie = "{armazenar_serie}" and data = "{hoje}"')
        cursor.execute(query)
        print(query)
        connection.commit()
        connection.close()

    else:
        pass


def editar():    
    global hoje
    time_diff = hoje - aberto
    print(f"Seu aniversário é daqui a {time_diff}")

    selected_item = tv.selection()[0]
    tv.item(selected_item, values=(vnmr.get(), vnome.get(), vhor.get(), vserie.get()))

    connection = pymysql.connect(host="localhost",
                                    user="root",
                                    passwd="",
                                    database="infrequencia")
    cursor = connection.cursor()

    query = (f'UPDATE segundo SET numero = "{vnmr.get()}", nome = "{vnome.get()}", horario = "{vhor.get()}" WHERE numero = "{vnmr.get()}" and data = "{hoje}"')
    cursor.execute(query)
    print(query)
    connection.commit()
    connection.close()

    vnmr.delete(0, END)
    vnome.delete(0, END)
    vhor.delete(0, END)
    vserie.delete(0, END)



def clicker(e):
    
    selected = tv.focus()
    values = tv.item(selected, 'values')
    
    vnmr.insert(0, values[0])
    vnome.insert(0, values[1])
    vhor.insert(0, values[2])
    vserie.insert(0, values[3])


def voltar():
    app.destroy()
    from MenuProf import MenuProf
    MenuProf()

def center(app):
    
    app.update_idletasks()

    width = app.winfo_width()
    frm_width = app.winfo_rootx() - app.winfo_x()
    app_width = width + 2 * frm_width

    height = app.winfo_height()
    titlebar_height = app.winfo_rooty() -app.winfo_y()
    app_height = height + titlebar_height + frm_width

    x = app.winfo_screenwidth() // 2 - app_width // 2
    y = app.winfo_screenheight() // 2 - app_height // 2

    # this is the line that will center your window
    app.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    app.deiconify()

app = Tk()
app.title("Sistema de Infrequência")
app.geometry('730x500')
app.resizable(width=FALSE, height=FALSE)
center(app)

lbnmr = Label(app, text="Número", fg="#8A2BE2", font=("Arial", 12, "bold"), padx=22)
lbnome = Label(app, text="Nome", fg="#8A2BE2", font=("Arial", 12, "bold"), padx=16)
lbhor = Label(app, text="Aula", fg="#8A2BE2", font=("Arial", 12, "bold"), padx=80)
lbserie =Label(app, text="Série", fg="#8A2BE2", font=("Arial", 12, "bold"), padx=22)

num = IntVar()
vnmr = ttk.Combobox(app, textvariable= num, width= 7)
vnmr['values'] = ["01", "02", "03", "04","05", "06", "07", "08", "09", 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20, 21, 
                    22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45]
vnmr.current(0)
vnmr.delete(0, END) 

alunos = StringVar()
vnome = ttk.Combobox(app, textvariable= alunos, width= 60)
vnome['values'] = ["Adriel Levi de Sousa Vieira", 
                    "Ana Luiza Bezerra de Freitas", 
                    "Antonia Vladia de Sousa Moreira",
                    "Antonio Anderson Faustino Andre",
                    "Carlos Eduardo de Sousa Lima",
                    "Cleber Lucas da Costa Macedo",
                    "Daniel Bezerra Silva Filho",
                    "Davi Moreira Silva",
                    "Eloisa Braga Farias",
                    "Gabriela Angelo Ribeiro",
                    "Gian Kleberth Barros Costa",
                    "Iann Carlos Lima Vieira",
                    "Isaac da Silva Lima"
                    "James Soares Costa",
                    "João Hélio Paulo de Souza",
                    "Joao Pedro Ferreira de Araujo",
                    "João Pedro Mota do Nascimento",
                    "Juan Guilherme Menezes Lima",
                    "Kailane Silva dos Reis",
                    "Lais Queiroz Costa e Silva",
                    "Lara Jemily Moreira Amaro da Silva",
                    "Lilian Vitória Santos Viana",
                    "Lucas de Sousa Santil",
                    "Luiz Fernando Soares Braga",
                    "Macia Kelly da Silva Araújo",
                    "Maria Geovana Quaresma Torres",
                    "Maria Mirella Oliveira Silva",
                    "Murilo Roger Farias Tabosa",
                    "Natanyell Romão Rodrigues",
                    "Pablo Moreira Santos",
                    "Rebeca Keren Pereira Lino",
                    "Rhanna Luiza Oliveira da Silva",
                    "Rikson de Oliveira Justino",
                    "Rommel Rishian Cavalcante Ferreira",
                    "Ryan Victor da Silva Matias",
                    "Thiago Emanuel Moura Honorato",
                    "Victor da Silva Mendes",
                    "Victor Kelvin Smyth Nascimento Sales",
                    "Warley da Silva Marques",
                    "Warley Pereira de Oliveira Filho",
                    "Yago Saulo Nascimento Medeiros",
                    "Yanne Beatriz Siqueira Costa"
                   ]
vnome.current(0)
vnome.delete(0, END)

hora = StringVar()
vhor = ttk.Combobox(app, textvariable= hora, width= 7)
vhor['values'] = ["1º", "2º", "3º", "4º", "5º", "6º", "7º", "8º", "9º"]
vhor.current(0)
vhor.delete(0, END)

ano = StringVar()
vserie = ttk.Combobox(app, textvariable= ano, width= 7, state=DISABLED)
vserie['values'] = ["1º", "2º", "3º"]
vserie.current(1)

tv = ttk.Treeview(app, columns=('numero', 'nome', 'horario', 'serie'), show='headings')

tv.column('numero', minwidth=10, width=90)
tv.column('nome', minwidth=70, width=428)
tv.column('horario', minwidth=10, width=90)
tv.column('serie', minwidth=10, width=90)

tv.heading('numero', text="Número")
tv.heading('nome', text="Nome")
tv.heading('horario', text="Aula")
tv.heading('serie', text="Série")

btn_voltar = Button(app, text="Voltar", command= voltar, bg="#8A2BE2", fg="#fff",font=("Arial", 12, "bold"),)
btn_inserir = Button(app, text="Inserir", command= inserir, bg="#8A2BE2", fg="#fff",font=("Arial", 12, "bold"))
btn_deletar = Button(app, text="Deletar", command= deletar, bg="#8A2BE2", fg="#fff",font=("Arial", 12, "bold"))
btn_editar = Button(app, text="Editar", command= editar, bg="#8A2BE2", fg="#fff",font=("Arial", 12, "bold"))

lbnmr.place(x=0, y= 5)
vnmr.place(x=25, y= 30)

lbnome.place(x=107, y= 5)
vnome.place(x=125, y= 30)

lbhor.place(x=462, y= 5)
vhor.place(x=544, y= 30)

lbserie.place(x=609, y= 5)
vserie.place(x=634, y= 30)

tv.place(x=15, y=70)
tv.configure(height=16)

btn_voltar.place(y=440, x=80)
btn_inserir.place(y=440, x=248)
btn_deletar.place(y=440, x=415)
btn_editar.place(y=440, x=585)

tv.bind("<Double-1>", clicker)

app.mainloop()