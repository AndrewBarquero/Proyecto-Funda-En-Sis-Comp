import tkinter as tk
from PIL import Image, ImageTk
import random
import serial
import time

# ===================== SERIAL =====================
ser = serial.Serial('COM3', 115200, timeout=1)
time.sleep(2)

# ===================== VENTANA PRINCIPAL =====================
ventana_principal = tk.Tk()
ventana_principal.title("Pantalla principal")
ventana_principal.geometry("575x425+650+200")
ventana_principal.resizable(False, False)

imagen1 = Image.open("Pantalla principal.PNG")
imagen_tk = ImageTk.PhotoImage(imagen1)
imagen_inicio = tk.Label(ventana_principal, image=imagen_tk)
imagen_inicio.pack()

# ===================== CIERRE SEGURO =====================
def cerrar_todo():
    try:
        ser.write(b"OFF\n")
        ser.flush()
        time.sleep(0.2)
        ser.close()
    except:
        pass
    ventana_principal.destroy()

ventana_principal.protocol("WM_DELETE_WINDOW", cerrar_todo)

# ===================== MODOS DE JUEGO =====================
def modo_de_juego():
    ventana_principal.withdraw()

    ventana_juego1 = tk.Toplevel(ventana_principal)
    ventana_juego1.title("Modos de juego")
    ventana_juego1.geometry("515x375+675+250")
    ventana_juego1.resizable(False, False)




    #-------------------------------------------------------Juego de transmision---------------------------------------------------
    def transmision():

        ventana_juego1.withdraw()

        ventana_transmision = tk.Toplevel(ventana_principal)
        ventana_transmision.title("Modo transmisión")
        ventana_transmision.geometry("500x400+650+200")
        ventana_transmision.resizable(False, False)

        #Texto del juego para dar instrucciones y mostrar puntaje 
        texto_juego = tk.Label(
            ventana_transmision,
            text="Presiona Start para comenzar",
            bg="RoyalBlue4",
            fg="White",
            font=('Arial', 10, 'bold')
        )
        texto_juego.pack(pady= 150)

        #Posibles palabras que se escucharan en morse
        palabras = [
            "SOS","NO","SI","CAJA","GATO","SOL","RATON","LAPIZ","ZAPATO"
            "RELOJ","REGLA","HORROR","BOMBA","TRAMPA","PANTALLA","CELULAR",
            "CELULA","SIETE","GRANDE","CABALLO","SAL","MANGO", "FOTO"
            "AZUL","ARBOL","INGENIERIA","VOLTAJE","CORRIENTE","INVENCIBLE"
            ]

        
        fases = [
            {"fase": 1, "msg": "FASE 1 - Velocidad normal"},
            {"fase": 2, "msg": "FASE 2 - Más rápido"},
            {"fase": 3, "msg": "FASE 3 - Máxima velocidad"}
        ]

        fase_actual = 0
        palabra_actual = ""
        puntaje_total = 0

        entrada = tk.Entry(ventana_transmision, width=20)
        entrada.place(relx=0.37, rely=0.5)

        # ---------- LÓGICA DEL JUEGO ----------
        def juego_transmision():
            nonlocal fase_actual, palabra_actual

            #Pregunta si ya termino las 3 fases del juego, si terminaron las 3 fases, lo lleva a la ventana del puntaje
            if fase_actual >= len(fases):
                pedir_nombre()
                return

            fase = fases[fase_actual]
            texto_juego.config(text=fase["msg"])
            ventana_transmision.update()

            #Envia la fase a la rasberry para la velocidad del juego
            ser.write(f"FASE{fase['fase']}\n".encode())
            time.sleep(1)

            #Se escoje una palabra random del repertorio de posibles palabras
            palabra_actual = random.choice(palabras)
            entrada.delete(0, tk.END) #Limpia la entrada para escribir la siguiente palabra

            ser.write(b"OFF\n")
            time.sleep(0.1)
            ser.write((palabra_actual + "\n").encode())

            texto_juego.config(text="Escucha el Morse...")
            fase_actual += 1 #Pasa a la siguiente fase
        

        def analisis_puntaje(): #Funcion para valorar que tan parecida es la palabra que se dijo con la que el usuario cree que es
            nonlocal puntaje_total
            respuesta = entrada.get().upper() #Toma la palabra que se escribe en la entrada (la pasa a mayusculas)
            puntaje_fase = 0

            for i in range(min(len(palabra_actual), len(respuesta))): #Toma el rango de la palabra mas corta para que no se tomen espacios vacios
                if palabra_actual[i] == respuesta[i]:
                    if fase_actual == 1:
                        puntaje_fase += 10
                    elif fase_actual == 2:
                        puntaje_fase += 15
                    elif fase_actual == 3:
                        puntaje_fase += 20

            puntaje_total += puntaje_fase
            texto_juego.config(
                text=f"Puntaje fase: {puntaje_fase}\nPuntaje total: {puntaje_total}"
            )

        # ---------- GUARDAR PUNTAJE ----------
        def pedir_nombre(): #Funcion que abre una ventana cuando acaba el juego y le pide el nombre al usuario para guardar su puntaje
            ventana_nombre = tk.Toplevel(ventana_transmision)
            ventana_nombre.title("Guardar puntaje")
            ventana_nombre.geometry("300x150+500+400")
            ventana_nombre.resizable(False, False)

            tk.Label(
                ventana_nombre,
                text=f"Puntaje final: {puntaje_total}",
                font=("Arial", 12, "bold")
            ).pack(pady=10)

            tk.Label(ventana_nombre, text="Nombre del jugador:").pack()
            entrada_nombre = tk.Entry(ventana_nombre)
            entrada_nombre.pack(pady=5)

            def guardar(): #Funcion que toma el nombre del usuario y su puntaje y los agrega a la .txt  con las lista de usuarios
                nombre = entrada_nombre.get().strip()
                if nombre:
                    with open("puntajes.txt", "a", encoding="utf-8") as f:
                        f.write(f"{nombre},{puntaje_total}\n")
                    ventana_nombre.destroy()

            tk.Button(ventana_nombre, text="Guardar", command=guardar).pack(pady=10)


        def volver():
            ser.write(b"OFF\n")
            ser.flush()
            ventana_transmision.destroy()
            ventana_juego1.deiconify()

        ventana_transmision.protocol("WM_DELETE_WINDOW", volver)
        
        
        #---------Botones del interfaz------------
        tk.Button(
            ventana_transmision,
            text="Start",
            bg="RoyalBlue4",
            fg="White",
            width=8,
            command=juego_transmision
        ).place(relx=0.43, rely=0.2)

        tk.Button(
            ventana_transmision,
            text="Calcular puntaje",
            bg="RoyalBlue4",
            fg="White",
            width=15,
            command=analisis_puntaje
        ).place(relx=0.39, rely=0.65)

        tk.Button(
            ventana_transmision,
            text="Volver",
            bg="RoyalBlue4",
            fg="White",
            width=8,
            command=volver
        ).place(relx=0.43, rely=0.8)
    #------------------------------------------------------Fin juego de transmision----------------------------------------------------




    imagen2 = Image.open("Fondo.PNG")
    fondo_tk = ImageTk.PhotoImage(imagen2)
    fondo = tk.Label(ventana_juego1, image=fondo_tk)
    fondo.image = fondo_tk
    fondo.pack()

    tk.Button(
        fondo,
        text="Modo Transmisión Simple",
        bg="RoyalBlue4",
        fg="White",
        width=22,
        command=transmision
    ).place(relx=0.3, rely=0.35)

    tk.Button(
        fondo,
        text="Volver",
        bg="RoyalBlue4",
        fg="White",
        width=8,
        command=lambda: (ventana_juego1.destroy(), ventana_principal.deiconify())
    ).place(relx=0.42, rely=0.8)

# ===================== BOTONES PRINCIPALES =====================
tk.Button(
    imagen_inicio,
    text="Jugar",
    bg="RoyalBlue4",
    fg="White",
    width=6,
    command=modo_de_juego
).place(relx=0.41, rely=0.45)

tk.Button(
    imagen_inicio,
    text="Salir",
    bg="RoyalBlue4",
    fg="White",
    width=6,
    command=cerrar_todo
).place(relx=0.42, rely=0.8)

ventana_principal.mainloop()

"""
Comandos para guardar a gitgub:
1- git status
2- git add .
3- git commit -m "Mensaje"
4- git push -u origin main
"""