import tkinter as tk

def mudar_tema(valor):
    if valor == 1:
        root.config(bg="lightblue")
    elif valor == 2:
        root.config(bg="lightgreen")
    elif valor == 3:
        root.config(bg="lightyellow")
    print(f"Tema {valor} selecionado")

root = tm.Tk()
root.title("Menu com Radio Buttons")
root.geometry("400x300")
cu



