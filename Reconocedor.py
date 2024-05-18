import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr

# Inicialización del reconocedor y el micrófono
reconocedor = sr.Recognizer()
microfono = sr.Microphone()

def pushed_button():
    # Cambia el color del botón para indicar que está escuchando
    boton_iniciar.config(bg='red', text='Escuchando...')
    resultado.set("Di algo...")
    ventana.update()  # Actualiza la interfaz para reflejar los cambios
    #Inicia proceso de reconocimiento
    iniciar_reconocimiento()
 
 
def iniciar_reconocimiento():

    try:
    
        with microfono as source:
            reconocedor.adjust_for_ambient_noise(source)  # Ajuste por ruido ambiente
            audio = reconocedor.listen(source)
            
        text = reconocedor.recognize_google(audio, language='es-ES')
        resultado.set(f"Dijiste: {text}")
        
    except sr.UnknownValueError:
        messagebox.showerror("Error", "No se entendió lo que dijiste. Intenta de nuevo.")
    
    except sr.RequestError as e:
        messagebox.showerror("Error", f"Error al conectarse con el servicio de reconocimiento: {e}")
    
    finally:
        # Restablece el color y el texto del botón
        boton_iniciar.config(bg='SystemButtonFace', text='Iniciar Reconocimiento')


# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Reconocimiento de Voz")

# Variable para mostrar el resultado
resultado = tk.StringVar()

# Botón para iniciar el reconocimiento
boton_iniciar = tk.Button(ventana, text="Iniciar Reconocimiento", command= lambda: pushed_button())
boton_iniciar.pack(pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, textvariable=resultado)
etiqueta_resultado.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
