from tkinter import *
from tkinter import ttk
from tkinter import messagebox    
import pymysql


corRoxo = "#8A2BE2"

class Relatorio:
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




app = Tk()
app.title("Relatório")
app.geometry('550x280')

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

tv.grid(column=0, row=3, columnspan=4, padx=20)


app.mainloop()


