# ============================================================
# SISTEMA DE PUNTAJES PARA TKINTER
# GUARDAR TOP 10 EN ARCHIVO TXT
# ============================================================

# ============================================================
# IMPORTAR LIBRERÍAS
# ============================================================

import tkinter as tk

# ============================================================
# FUNCIÓN: GUARDAR PUNTAJE
# ============================================================
# Esta función:
# 1. Abre el archivo "puntajes.txt"
# 2. Agrega un nuevo puntaje
# 3. NO borra los anteriores
# ============================================================

def guardar_puntaje(nombre, puntaje):

    # "a" significa APPEND
    # Agrega información al final del archivo
    archivo = open("puntajes.txt", "a")

    # Escribe:
    # nombre,puntaje
    # y luego un salto de línea
    archivo.write(f"{nombre},{puntaje}\n")

    # Cierra el archivo
    archivo.close()

# ============================================================
# FUNCIÓN: LEER PUNTAJES
# ============================================================
# Esta función:
# 1. Lee TODO el archivo
# 2. Convierte cada línea en una lista
# 3. Retorna todos los puntajes
# ============================================================

def leer_puntajes():

    # TRY:
    # intenta abrir el archivo
    try:

        archivo = open("puntajes.txt", "r")

    # EXCEPT:
    # si el archivo no existe
    except:

        # retorna lista vacía
        return []

    # Lee todas las líneas
    lineas = archivo.readlines()

    # Cierra el archivo
    archivo.close()

    # Lista donde guardaremos los puntajes
    puntajes = []

    # Recorre cada línea del archivo
    for linea in lineas:

        # Elimina saltos de línea
        linea = linea.strip()

        # Divide usando la coma
        # Ejemplo:
        # "Andrew,200"
        # se convierte en:
        # nombre = Andrew
        # puntaje = 200
        nombre, puntaje = linea.split(",")

        # Agrega a la lista
        puntajes.append([nombre, int(puntaje)])

    return puntajes

# ============================================================
# FUNCIÓN: ORDENAR PUNTAJES
# ============================================================
# Ordena de MAYOR a MENOR
# ============================================================

def ordenar_puntajes(lista):

    # x[1] significa:
    # usar el puntaje para ordenar
    lista.sort(key=lambda x: x[1], reverse=True)

    return lista

# ============================================================
# FUNCIÓN: MOSTRAR TOP 10 EN TKINTER
# ============================================================
# 1. Lee los puntajes
# 2. Los ordena
# 3. Muestra los 10 mejores
# ============================================================

def mostrar_top10():

    # Borra texto anterior
    texto_top.delete("1.0", tk.END)

    # Lee puntajes
    puntajes = leer_puntajes()

    # Ordena puntajes
    puntajes = ordenar_puntajes(puntajes)

    # Título
    texto_top.insert(tk.END, "====== TOP 10 ======\n\n")

    # min(10, len(puntajes))
    # evita errores si hay menos de 10 jugadores
    for i in range(min(10, len(puntajes))):

        # Obtiene nombre
        nombre = puntajes[i][0]

        # Obtiene score
        score = puntajes[i][1]

        # Inserta en pantalla
        texto_top.insert(
            tk.END,
            f"{i+1}. {nombre} - {score}\n"
        )

# ============================================================
# FUNCIÓN: SIMULAR PARTIDA
# ============================================================
# Esta función simula:
# 1. Obtener datos de los Entry
# 2. Guardar puntaje
# 3. Actualizar Top 10
# ============================================================

def terminar_partida():

    # Obtiene nombre del jugador
    nombre = entrada_nombre.get()

    # Obtiene puntaje
    puntaje = entrada_puntaje.get()

    # Verifica que el puntaje sea número
    if puntaje.isdigit():

        # Convierte a entero
        puntaje = int(puntaje)

        # Guarda en archivo
        guardar_puntaje(nombre, puntaje)

        # Actualiza top
        mostrar_top10()

# ============================================================
# CREAR VENTANA
# ============================================================

ventana = tk.Tk()

ventana.title("Sistema de Puntajes")

ventana.geometry("500x500")

# ============================================================
# TÍTULO
# ============================================================

titulo = tk.Label(
    ventana,
    text="Guardar Puntajes",
    font=("Arial", 16)
)

titulo.pack(pady=10)

# ============================================================
# ENTRY NOMBRE
# ============================================================

label_nombre = tk.Label(
    ventana,
    text="Nombre:"
)

label_nombre.pack()

entrada_nombre = tk.Entry(
    ventana,
    width=30
)

entrada_nombre.pack(pady=5)

# ============================================================
# ENTRY PUNTAJE
# ============================================================

label_puntaje = tk.Label(
    ventana,
    text="Puntaje:"
)

label_puntaje.pack()

entrada_puntaje = tk.Entry(
    ventana,
    width=30
)

entrada_puntaje.pack(pady=5)

# ============================================================
# BOTÓN GUARDAR
# ============================================================

boton = tk.Button(
    ventana,
    text="Guardar Puntaje",
    command=terminar_partida
)

boton.pack(pady=10)

# ============================================================
# ÁREA DE TEXTO TOP 10
# ============================================================

texto_top = tk.Text(
    ventana,
    width=40,
    height=15
)

texto_top.pack(pady=10)

# ============================================================
# MOSTRAR TOP AL INICIAR
# ============================================================

mostrar_top10()

# ============================================================
# EJECUTAR VENTANA
# ============================================================

ventana.mainloop()