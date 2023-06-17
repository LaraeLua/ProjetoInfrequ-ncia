from tkinter import *
from tkinter import ttk
import pymysql
from reportlab.pdfgen import canvas
import datetime 
from subprocess import call

data_atual = datetime.date.today()

corRoxo = "#8A2BE2"
corBranca = "#fff"

def popular():    
    tv.delete(*tv.get_children())
    connection = pymysql.connect(host="localhost", 
                                    user="root",
                                    passwd="", 
                                    database="infrequencia")
    cursor = connection.cursor()

    query = ("SELECT numero, nome, horario, serie FROM segundo")
    cursor.execute(query)
    results = cursor.fetchall()     
    connection.commit()
    connection.close()
    if results:
        
       for i in results:      
        tv.insert("","end", values = i)

def voltar():
    app.destroy()
    
    call(["python", "ProjetoInfrequencia-main\\MenuSec.py"])

def salvar():
    connection = pymysql.connect(host="localhost", 
                                    user="root",
                                    passwd="", 
                                    database="infrequencia")
  
    cursor = connection.cursor()
    comando_SQl = "SELECT numero, nome, horario, serie FROM segundo"
    cursor.execute(comando_SQl)
    dados_lidos = cursor.fetchall()   

    conn = pymysql.connect(host="localhost", 
                                    user="root",
                                    passwd="", 
                                    database="infrequencia")
  
    cursor = conn.cursor()
    comando = "SELECT nome FROM login ORDER BY ID DESC LIMIT 1"
    cursor.execute(comando)
    prof = cursor.fetchall() 

    y = 0
    pdf = canvas.Canvas("Faltosos_2°A.pdf")
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(150, 805, "Alunos faltosos:")        
    pdf.setFont("Times-Bold", 15)
    pdf.drawString(50, 805, str(data_atual))
    pdf.drawString(0, 805, str(prof))
    pdf.setFont("Times-Bold", 12)

    pdf.drawString(46, 750, "Número:")
    pdf.drawString(116, 750, "Nome:")
    pdf.drawString(406, 750, "Horário:")
    pdf.drawString(496, 750, "Série:")

    for i in range(0, len(dados_lidos)):
        y = y + 50
        
        pdf.drawString(50, 770 -y, str(dados_lidos[i][0]))
        pdf.drawString(120, 770 -y, str(dados_lidos[i][1]))
        pdf.drawString(410, 770 -y, str(dados_lidos[i][2]))
        pdf.drawString(500, 770 -y, str(dados_lidos[i][3]))
    pdf.save()
    
def buscar():
    armazenar_data = data.get()

    
    connection = pymysql.connect(host="localhost", 
                                    user="root",
                                    passwd="", 
                                    database="infrequencia")
  
    cursor = connection.cursor()
    comando_SQl = f'SELECT numero, nome, horario, serie FROM segundo WHERE data LIKE "%{armazenar_data}%" ORDER BY nome'
    cursor.execute(comando_SQl)
    print(comando_SQl)
    results = cursor.fetchall()     
    connection.commit()
    connection.close()
    if results:
        
       for i in results:      
        tv.insert("","end", values = i)



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
app.title("Relatório")
app.geometry('730x500')
center(app)

frame_cima = Frame(app, width=730, height=50, relief='flat', bg=corRoxo)
frame_cima.grid(row=0, column=0, pady=5, padx=0, sticky=NSEW)

#configurando o frame cima
relat = Label(frame_cima, text='Relatório: 2º Informática', anchor=NE, font=("Arial", 20, "bold"), bg=corRoxo, fg=corBranca, padx=3, pady=5)
relat.place(x=220, y=3)

data = Entry(app, width= 30)
data.place(x=400, y= 70)

buscar = Button(app, text="Pesquisar", command= buscar, bg="#8A2BE2", fg="#fff",font=("Arial", 8, "bold"))
buscar.place(x=590, y=68)

tv = ttk.Treeview(app, columns=('numero', 'nome', 'horario', 'serie'), show='headings')
tv.column('numero', minwidth=10, width=90)
tv.column('nome', minwidth=70, width=428)
tv.column('horario', minwidth=10, width=90)
tv.column('serie', minwidth=10, width=90)


tv.heading('numero', text="Número")
tv.heading('nome', text="Nome")
tv.heading('horario', text="Horário")
tv.heading('serie', text="Série")

btn_voltar = Button(app, text="Voltar", command= voltar, bg="#8A2BE2", fg="#fff",font=("Arial", 12, "bold"))
btn_voltar.place(x=248, y=460)

btn_salvar = Button(app, text="Salvar", command= salvar, bg="#8A2BE2", fg="#fff",font=("Arial", 12, "bold"))
btn_salvar.place(x=415, y=460)

tv.place(x=15, y=100)
tv.configure(height=16)

app.mainloop()