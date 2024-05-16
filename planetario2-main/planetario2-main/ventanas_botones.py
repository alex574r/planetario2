from tkinter import *
from tkinter import messagebox

def show_frame(frame):
    frame.tkraise()

def button_action_panel1():
    print("Botón del Panel 1 presionado")
    messagebox.showinfo("Panel 1", "Esta es una acción del Panel 1")

def button_action_panel2():
    print("Botón del Panel 2 presionado")
    messagebox.showinfo("Panel 2", "Esta es una acción del Panel 2")

v1 = Tk()
v1.geometry('1080x720')
v1.config(bg='black')
v1.resizable(False,False)
# Definir los paneles (frames)
frame1 = Frame(v1, bg='black')
frame2 = Frame(v1, bg='black')

for frame in (frame1, frame2):
    frame.place(x=0, y=0, width=1080, height=720)

# Panel 1 con la primera imagen y botón
imagenL1 = PhotoImage(file="planeta1.gif")
lblimagen1 = Label(frame1, image=imagenL1)
lblimagen1.place(x=0, y=0)
button1 = Button(frame1, text="Acción Panel 1", command=button_action_panel1)
button1.place(x=1000, y=600)  # Ubicado en la esquina inferior derecha del Panel 1

# Panel 2 con la segunda imagen y botón
imagenL2 = PhotoImage(file="Neptuno.gif")
lblimagen2 = Label(frame2, image=imagenL2)
lblimagen2.place(x=0, y=0)
button2 = Button(frame2, text="Acción Panel 2", command=button_action_panel2)
button2.place(x=10, y=10)  # Ubicado en la esquina superior izquierda del Panel 2

menu = Menu(v1)
v1.config(menu=menu)

File = Menu(menu, tearoff=0)
File.add_command(label="Nuevo Proyecto")
File.add_command(label="Abrir")
File.add_command(label="Guardar")
File.add_separator()
File.add_command(label="Salir", command=v1.quit)

Edit = Menu(menu, tearoff=0)
Edit.add_command(label="Copiar")
Edit.add_command(label="Pegar")
Edit.add_command(label="Cortar")

Ayuda = Menu(menu, tearoff=0)
Ayuda.add_command(label="Help")
Ayuda.add_separator()
Ayuda.add_command(label="About")

menu.add_cascade(label="Archivo", menu=File)
menu.add_cascade(label="Editar", menu=Edit)
menu.add_cascade(label="Ayuda", menu=Ayuda)

# Añadir una opción en el menú Archivo para cambiar de panel
File.add_command(label="Mostrar Panel 1", command=lambda: show_frame(frame1))
File.add_command(label="Mostrar Panel 2", command=lambda: show_frame(frame2))

# Mostrar el primer panel al inicio
show_frame(frame1)

v1.mainloop()

