import tkinter as tk
from PIL import Image, ImageTk
import time
import serial
import random

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

        #----------------------------Ventana del juego de transmision-----------------------
    def transmision():
        ventana_juego1.withdraw()

        ventana_transmision = tk.Tk()
        ventana_transmision.title("Modo transmision")
        ventana_transmision.geometry("500x400+650+200")
        ventana_transmision.resizable(False, False)

        

        texto_juego_transmision = tk.Label(ventana_transmision, text="Cuando presione el boton empezara el juego")
        texto_juego_transmision.config(bg="RoyalBlue4", fg="SlateGray3", font=('Arial', 10, 'bold'))
        texto_juego_transmision.place(relx=0.15, rely=0.4)

        palabras_juego_transmision = ["SOS","NO","SI","CAJA", "GATO", "SOL", "RATON", "LAPIZ", "RELOJ", "REGLA", "BOMBA", "PANTALLA", "CELULAR", 
                                      "SIETE", "GRANDE", "CABALLO", "SAL", "MANGO", "AZUL", "ARBOL", "INGENIERIA","VOLTAJE", "CORRIENTE"]
        
        def juego_transmision():
            texto_juego_transmision.config(text="¿listo?")
            time.sleep(2)
            texto_juego_transmision.config(text="3")
            time.sleep(2)
            texto_juego_transmision.config(text="2")
            time.sleep(2)
            texto_juego_transmision.config(text="1")

   

            
        boton_start = tk.Button(ventana_transmision, width=5 ,relief="groove", bd=10,bg="RoyalBlue4",fg="White" , text = "Start", command=juego_transmision).place(relx=0.42, rely=0.2)
        
        texto_juego_transmision
        texto_juego_transmision






        def volver_modo():
            ventana_transmision.destroy()
            ventana_juego1.deiconify()
        ventana_transmision.protocol("WM_DELETE_WINDOW", volver_modo)

        boton_cierre_transimision = tk.Button(ventana_transmision, width=5 ,relief="groove", bd=10,bg="RoyalBlue4",fg="White" , text = "Volver", command=volver_modo).place(relx=0.42, rely=0.8)


    #-----------------------------------------------------------------------------------


    imagen2 = Image.open("Fondo.PNG")  
    tk_fondo = ImageTk.PhotoImage(imagen2)
    imagen_fondo = tk.Label(ventana_juego1, image=tk_fondo)
    imagen_fondo.image = tk_fondo
    imagen_fondo.pack()

    titulo_modo_de_juego = tk.Label(imagen_fondo, width=5 , text="SELECCIONE EL MODO DE JUEGO")
    titulo_modo_de_juego.config(height=2, width=28, bg="RoyalBlue4", fg="SlateGray3", font=('Arial', 15, 'bold'))
    titulo_modo_de_juego.place(relx=0.15, rely=0.1)

    boton_modo_1 = tk.Button(imagen_fondo, width=20 ,relief="groove", bd=10,bg="RoyalBlue4",fg="White" , text = "Modo Transmision Simple", command=transmision ).place(relx=0.31, rely=0.3)
    boton_modo_2 = tk.Button(imagen_fondo, width=22 ,relief="groove", bd=10,bg="RoyalBlue4",fg="White" , text = "Modo Escucha y Transmision", ).place(relx=0.30, rely=0.5)


    def volver1():
        ventana_juego1.destroy()
        ventana_principal.deiconify()
    ventana_juego1.protocol("WM_DELETE_WINDOW", volver1)

    boton_cierre2 = tk.Button(imagen_fondo, width=5 ,relief="groove", bd=10,bg="RoyalBlue4",fg="White" , text = "Volver", command=volver1).place(relx=0.42, rely=0.8)
#--------------------------------------------------------------------------------------





""" -------------------------------------------------Codigos utiles ----------------
    def enviar_texto():
        texto = entrada.get()
        texto = texto.upper()
        ser.write((texto + "\n").encode())

    entrada = tk.Entry(imagen_fondo,width=30)
    entrada.place(relx=0.42, rely=0.5)

    boton_buzz = tk.Button(imagen_fondo,text="Enviar a Raspberry",command=enviar_texto)
    boton_buzz.place(relx=0.42, rely=0.6)

"""    
"""
    #Las siguientes funciones y botones hechos por Chatcito:
    def encender():
        ser.write(b'ON\n')

    def apagar():
        ser.write(b'OFF\n')

    btn1 = tk.Button(imagen_fondo, text="Encender", command=encender)
    btn1.place(relx=0.42, rely=0.3)

    btn2 = tk.Button(imagen_fondo, text="Apagar", command=apagar)
    btn2.place(relx=0.42, rely=0.5)
"""#---------------------------------------------------------------------------------------


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


