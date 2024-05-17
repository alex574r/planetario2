from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def show_frame(frame):
    frame.tkraise()

def button_action_panel1():
    print("Botón del Panel 1 presionado")
    messagebox.showinfo("Panel 1", "Esta es una acción del Panel 1")

def button_action_panel2():
    print("Botón del Panel 2 presionado")
    messagebox.showinfo("Panel 2", "Esta es una acción del Panel 2")

def button_action_panel3():
    print("Botón del Panel 3 presionado")
    messagebox.showinfo("Panel 3", "Esta es la acción del panel 3")

def button_action_panel4():
    print("Botón del Panel 4 presionado")
    messagebox.showinfo("Panel 4", "Esta es la acción del panel 4")    
    
# Redimensionar las imágenes usando Pillow
def resize_image(image_path, size=(1080, 720)):
    image = Image.open(image_path)
    image = image.resize(size, Image.LANCZOS)  # Usar Image.LANCZOS para mejor calidad de redimensionado
    return ImageTk.PhotoImage(image)

v1 = Tk()
v1.geometry('1080x720')
v1.config(bg='black')
v1.resizable(False, False)  # Hacer la ventana no redimensionable

# Redimensionar las imágenes
imagenL1 = resize_image("planeta1.gif")
imagenL2 = resize_image("Neptuno.gif")
imagenL3 = resize_image("Venus.gif")
imagenL4 = resize_image("Tierra.gif")

# Definir los paneles
frame1 = Frame(v1, bg='black')
frame2 = Frame(v1, bg='black')
frame3 = Frame(v1, bg='black')
frame4 = Frame(v1, bg='black')

# Poner los paneles
for frame in (frame1, frame2,frame3, frame4):
    frame.place(x=0, y=0, width=1080, height=720)

# Panel 1 con la primera imagen y botones
lblimagen1 = Label(frame1, image=imagenL1)
lblimagen1.place(x=0, y=0)
button1 = Button(frame1, text="Acción Panel 1", command=button_action_panel1)
button1.place(relx=0.5, rely=0.5, anchor=CENTER)  # Ubicado en el centro del Panel 1
switch_button1 = Button(frame1, text="Ir a Panel 2", command=lambda: show_frame(frame2))
switch_button1.place(relx=0.5, rely=0.1, anchor=N)  # Ubicado en la parte superior del Panel 1
switch_button2 = Button(frame1, text="Ir a Panel 3", command=lambda: show_frame(frame3))
switch_button2.place(relx=0.5, rely=0.2, anchor=N)  # Ubicado en la parte superior del Panel 1
switch_button3 = Button(frame1, text="Ir a Panel 4", command=lambda: show_frame(frame4))
switch_button3.place(relx=0.5, rely=0.3, anchor=N)  # Ubicado en la parte superior del Panel 1

# Panel 2 con la segunda imagen y botones
lblimagen2 = Label(frame2, image=imagenL2)
lblimagen2.place(x=0, y=0)
button2 = Button(frame2, text="Acción Panel 2", command=button_action_panel2)
button2.place(relx=0.5, rely=0.5, anchor=CENTER)  # Ubicado en el centro del Panel 2
switch_button2 = Button(frame2, text="Ir a Panel 1", command=lambda: show_frame(frame1))
switch_button2.place(relx=0.5, rely=0.1, anchor=N)  # Ubicado en la parte superior del Panel 2
switch_button3 = Button(frame2, text="Ir a Panel 3", command=lambda: show_frame(frame3))
switch_button3.place(relx=0.5, rely=0.2, anchor=N)  # Ubicado en la parte superior del Panel 2
switch_button4 = Button(frame2, text="Ir a Panel 4", command=lambda: show_frame(frame4))
switch_button4.place(relx=0.5, rely=0.3, anchor=N)  # Ubicado en la parte superior del Panel 2

# Panel 3 con la tercera imagen y botones
lblimagen3 = Label(frame3, image=imagenL3)
lblimagen3.place(x=0, y=0)
button3 = Button(frame3, text="Acción Panel 3", command=button_action_panel3)
button3.place(relx=0.5, rely=0.5, anchor=CENTER)  # Ubicado en el centro del Panel 3
switch_button5 = Button(frame3, text="Ir a Panel 1", command=lambda: show_frame(frame1))
switch_button5.place(relx=0.5, rely=0.1, anchor=N) # Ubicado en la parte superior del Panel 3
switch_button6 = Button(frame3, text="Ir a Panel 2", command=lambda: show_frame(frame2))
switch_button6.place(relx=0.5, rely=0.2, anchor=N) # Ubicado en la parte superior del Panel 3
switch_button7 = Button(frame3, text="Ir a Panel 4", command=lambda: show_frame(frame4))
switch_button7.place(relx=0.5, rely=0.3, anchor=N) # Ubicado en la parte superior del Panel 3

#Panel 4 con la cuarta imagen y botones
lblimagen4 = Label(frame4, image=imagenL4)
lblimagen4.place(x=0, y=0)
button4 = Button(frame4, text="Acción Panel 4", command=button_action_panel4)
button4.place(relx=0.5, rely=0.5, anchor=CENTER) # Ubicado en el centro del Panel 4
switch_button8 = Button(frame4, text="Ir a Panel 1", command=lambda: show_frame(frame1))
switch_button8.place(relx=0.5, rely=0.1, anchor=N) # Ubicado en la parte superior del Panel 4
switch_button9 = Button(frame4, text="Ir a Panel 2", command=lambda: show_frame(frame2))
switch_button9.place(relx=0.5, rely=0.2, anchor=N) # Ubicado en la parte superior del Panel 4
switch_button10 = Button(frame4, text="Ir a Panel 3", command=lambda: show_frame(frame3))
switch_button10.place(relx=0.5, rely=0.3, anchor=N) # Ubicado en la parte superior del Panel 4

menu = Menu(v1)
v1.config(menu=menu)

Acciones = Menu(menu, tearoff=0)
Acciones.add_command(label="Volver a menú principal", command=lambda: show_frame(frame1))
Acciones.add_separator()
Acciones.add_command(label="Salir", command=v1.quit)

Planetas = Menu(menu, tearoff=0)
Planetas.add_command(label="Ir a Panel 1", command=lambda: show_frame(frame1))
Planetas.add_command(label="Ir a Panel 2", command=lambda: show_frame(frame2))
Planetas.add_command(label="Ir a Panel 3", command=lambda: show_frame(frame3))
Planetas.add_command(label="Ir a Panel 4", command=lambda: show_frame(frame4))

Ayuda = Menu(menu, tearoff=0)
Ayuda.add_command(label="Help")
Ayuda.add_separator()
Ayuda.add_command(label="About")

menu.add_cascade(label="Acciones", menu=Acciones)
menu.add_cascade(label="Planetas", menu=Planetas)
menu.add_cascade(label="Ayuda", menu=Ayuda)

#Mostrar el primer panel al inicio
show_frame(frame1)

v1.mainloop()