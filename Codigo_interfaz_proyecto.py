import tkinter as tk
from PIL import Image, ImageTk
import time
import serial

ser = serial.Serial('COM3', 115200) #Puerto




#---------------------------Ventana principal----------------------------------------------
ventana_principal = tk.Tk()
ventana_principal.title("Pantalla Principal")
ventana_principal.geometry("575x425+650+200")
ventana_principal.resizable(False, False)

imagen1 = Image.open("Pantalla principal.PNG")  
imagen_tk = ImageTk.PhotoImage(imagen1)
imagen_inicio = tk.Label(ventana_principal, image=imagen_tk)
imagen_inicio.pack()
#------------------------------------------------------------------------------------






#------------------------Ventana donde se seleciona el modo de juego ----------------------
def modo_de_juego():
    ventana_principal.withdraw()

    ventana_juego1 = tk.Toplevel(ventana_principal)
    ventana_juego1.title("Modos de juego")
    ventana_juego1.geometry("515x375+675+250")
    ventana_juego1.resizable(False, True)

    imagen2 = Image.open("Fondo.PNG")  
    tk_fondo = ImageTk.PhotoImage(imagen2)
    imagen_fondo = tk.Label(ventana_juego1, image=tk_fondo)
    imagen_fondo.image = tk_fondo
    imagen_fondo.pack()

    def volver1():
        ventana_juego1.destroy()
        ventana_principal.deiconify()
    ventana_juego1.protocol("WM_DELETE_WINDOW", volver1)

    boton_cierre2 = tk.Button(imagen_fondo, width=5 ,relief="groove", bd=10,bg="RoyalBlue4",fg="White" , text = "Volver", command=volver1).place(relx=0.42, rely=0.8)
#--------------------------------------------------------------------------------------

    #Las siguientes funciones y botones hechos por Chatcito:
    def encender():
        ser.write(b'ON\n')

    def apagar():
        ser.write(b'OFF\n')

    btn1 = tk.Button(imagen_fondo, text="Encender", command=encender)
    btn1.place(relx=0.42, rely=0.5)

    btn2 = tk.Button(imagen_fondo, text="Apagar", command=apagar)
    btn2.place(relx=0.42, rely=0.3)

#------------------------Ventana acerca de nosotros---------------------------------------

def info():
    ventana_principal.withdraw()

    ventana_informacion = tk.Toplevel(ventana_principal)
    ventana_informacion.title("Seccion de Analisis")
    ventana_informacion.geometry("400x550+725+300")
    ventana_informacion.resizable(False, True)

#-------------------------------------------------------------------------------------------





#------------------Botones pantalla principal------------------------------------------------
boton_play = tk.Button(imagen_inicio,width=6 ,relief="groove", bd=10,bg="RoyalBlue4",fg="White", text="Jugar", command=modo_de_juego).place(relx= 0.41, rely=0.45)
boton_info = tk.Button(imagen_inicio,width=15 ,relief="groove", bd=10,bg="RoyalBlue4",fg="White", text="Acerca de nosotros", command=info).place(relx= 0.36, rely=0.6)
boton_cierre1 = tk.Button(imagen_inicio, width=5 ,relief="groove", bd=10,bg="RoyalBlue4",fg="White" , text = "Salir", command=ventana_principal.destroy).place(relx=0.42, rely=0.8)
#------------------------------------------------------------------------------------------



ventana_principal.mainloop()


