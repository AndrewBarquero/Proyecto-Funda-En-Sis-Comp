import tkinter as tk
from PIL import Image, ImageTk

ventana_principal = tk.Tk()
ventana_principal.title("Pantalla Principal")
ventana_principal.geometry("575x425+750+200")
ventana_principal.resizable(False, False)

imagen1 = Image.open("Pantalla principal.PNG")  
imagen_tk = ImageTk.PhotoImage(imagen1)
imagen_inicio = tk.Label(ventana_principal, image=imagen_tk)
imagen_inicio.pack()

#------------------------Ventana del juego----------------------
def ventana_juego():
    ventana_principal.withdraw()

    ventana_juego1 = tk.Toplevel(ventana_principal)
    ventana_juego1.title("Seccion de Analisis")
    ventana_juego1.geometry("400x550+725+300")
    ventana_juego1.resizable(False, True)
#------------------------Ventana acerca de nosotros-------------
def ventana_info():
    ventana_principal.withdraw()

    ventana_informacion = tk.Toplevel(ventana_principal)
    ventana_informacion.title("Seccion de Analisis")
    ventana_informacion.geometry("400x550+725+300")
    ventana_informacion.resizable(False, True)
#---------------------------------------------------------------

boton_play = tk.Button(imagen_inicio,width=6 ,relief="groove", bd=10,bg="RoyalBlue4",fg="White", text="Jugar", command=ventana_juego).place(relx= 0.41, rely=0.45)
boton_info = tk.Button(imagen_inicio,width=15 ,relief="groove", bd=10,bg="RoyalBlue4",fg="White", text="Acerca de nosotros", command=ventana_info).place(relx= 0.36, rely=0.6)
boton_cierre1 = tk.Button(imagen_inicio, width=5 ,relief="groove", bd=10,bg="RoyalBlue4",fg="White" , text = "Salir", command=ventana_principal.destroy).place(relx=0.42, rely=0.8)

ventana_principal.mainloop()


