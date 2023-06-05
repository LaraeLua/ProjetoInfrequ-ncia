from tkinter import *
from tkinter import ttk
from tkinter import messagebox    
import pymysql


corRoxo = "#8A2BE2"

class Chamada:
    pass

def popular():
    tv.delete(*tv.get_children())
    connection = pymysql.connect(host="localhost",
                                    user="root",
                                    passwd="",
                                    database="infrequencia")
    cursor = connection.cursor()

    query = ("SELECT numero, nome, horario, data FROM frequencia")
    cursor.execute(query)
    results = cursor.fetchall()
    connection.commit()
    connection.close()
    if results:

       for i in results:
        tv.insert("","end", values = i)



def inserir():
    if vnmr.get()=="" or vnome.get()=="" or vhor.get()=="" or vdata.get()=="":
        messagebox.showinfo(title="ERRO", message="Digite todos os dados")
        return
    else:
        tv.insert("","end", values=(vnmr.get(), vnome.get(), vhor.get(), vdata.get()))

    vnmr.delete(0, END)
    vnome.delete(0, END)
    vhor.delete(0, END)
    vdata.delete(0, END)
    vnmr.focus()

    armazenar_nmr = vnmr.get()
    armazenar_nome = vnome.get()
    armazenar_hor = vhor.get()
    armazenar_data = vdata.get()

    connection = pymysql.connect(host="localhost",
                                user="root",
                                passwd="",
                                database="infrequencia")
    cursor = connection.cursor()

    query = (f'INSERT INTO frequencia(numero, nome, horario, data) VALUES ("{armazenar_nmr}", "{armazenar_nome}",  "{armazenar_hor}",  "{armazenar_data}")')
    cursor.execute(query)
    connection.commit()
    connection.close()


app = Tk()
app.title("Sistema Infrequencia")
app.geometry('550x350')


lbnmr = Label(app, text="Número")
vnmr= Entry(app)

lbnome = Label(app, text="Nome")
vnome= Entry(app)

lbhor = Label(app, text="Horário")
vhor = Entry(app)

lbdata =Label(app, text="Data")
vdata = Entry(app)

tv = ttk.Treeview(app, columns=('numero', 'nome', 'horario', 'data'), show='headings')
tv.column('numero', minwidth=0, width=60)
tv.column('nome', minwidth=0, width=250)
tv.column('horario', minwidth=0, width=100)
tv.column('data', minwidth=0, width=100)
popular()


tv.heading('numero', text="Número")
tv.heading('nome', text="Nome")
tv.heading('horario', text="Horário")
tv.heading('data', text="Data")

btn_inserir = Button(app, text="Inserir", command= inserir)

lbnmr.grid(column=0, row=0, stick='w')
vnmr.grid(column=0, row=1)

lbnome.grid(column=1, row=0, stick='w')
vnome.grid(column=1, row=1)

lbhor.grid(column=2, row=0, stick='w')
vhor.grid(column=2, row=1, stick='w')

lbdata.grid(column=3, row=0, stick='w')
vdata.grid(column=3, row=1)

tv.grid(column=0, row=3, columnspan=4, pady=5)

btn_inserir.grid(column=1, row=4)

app.mainloop()


