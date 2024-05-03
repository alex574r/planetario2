from tkinter import*
v1=Tk()

v1.geometry('700x500')
v1.config(bg='black')
#v1.iconbitmap("")
imagenL = PhotoImage(file="planeta1.gif")
lblimagen = Label(v1,image=imagenL)
lblimagen.place(x=0, y=0)

menu=Menu(v1)
v1.config(menu=menu)

File=Menu(menu,tearoff=0)
File.add_command(label = "Nuevo Proyecto")
File.add_command(label = "Abrir")
File.add_command(label = "Guardar")
File.add_separator()
File.add_command(label="Salir")

Edit=Menu(menu,tearoff=0)
Edit.add_command(label="Copiar")
Edit.add_command(label="Pegar")
Edit.add_command(label="Cortar")

Ayuda=Menu(menu,tearoff=0)
Ayuda.add_command(label="Help")
File.add_separator()
Ayuda.add_command(label="About")

menu.add_cascade(label = "Archivo", menu=File)
menu.add_cascade(label = "Editar", menu=Edit)
menu.add_cascade(label = "Ayuda", menu=Ayuda)

v1.mainloop()