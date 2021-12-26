from tkinter import *
import sqlite3
with sqlite3.connect("clasesdevig.db") as db:
    cursor =db.cursor()

window = Tk()

cursor.execute(""" CREATE TABLE IF NOT EXISTS info (id integer PRIMARY KEY AUTOINCREMENT, estudiante text NOT NULL, nota text NOT NULL);
""")

def add_new_user():
    new_username = estudiante.get()
    new_grade = nota.get()

    cursor.execute("SELECT COUNT (*) from info WHERE estudiante = '" + new_username +"' ")
    result = cursor.fetchone()

    if int(result[0]) > 0:
        error["text"] = "Error: Username already exists."
    else:
        error["text"] = "Added new user"
        cursor.execute("INSERT INTO info(estudiante,nota) VALUES(?,?)", (new_username, new_grade))
        db.commit()

error = Message(text = "Agregar alumno/a:")
error.place(x = 30, y = 0)
error.config(padx=0)

label_1 = Label(text = "Escribir estudiante:")
label_1.place(x = 30, y = 40)
label_1.config(bg = "lightblue", padx=0)

estudiante = Entry(text = "")
estudiante.place(x=150, y=40, width = 200, height = 25)

label_2 = Label(text = "Escribir nota:")
label_2.place(x = 30, y = 80)
label_2.config(bg = "lightblue", padx=0)

nota = Entry(text = "")
nota.place(x=150, y=80, width = 200, height = 25)

button = Button(text = "Agregar", command = add_new_user)
button.place(x=150, y=120, width = 75, height = 35)

window.geometry("450x180")

window.title('Base de datos - Las clases de Vig')

window.mainloop()
