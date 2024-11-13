import tkinter as tk

def abrir_arquivo():
    print("Abrir arquivo...")

def salvar_arquivo():
    print("Salvar arquivo...")

def cortar():
    print("Cortar...")

def copiar():
    print("Copiar...")

# Criando a janela principal
root = tk.Tk()
root.title("Menu com Separadores")
root.geometry("400x300")

# Criando a barra de menus
barra_menu = tk.Menu(root)

# Menu Arquivo com opções
menu_arquivo = tk.Menu(barra_menu, tearoff=0)
menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
menu_arquivo.add_command(label="Salvar", command=salvar_arquivo)

# Adicionando um separador
menu_arquivo.add_separator()

# Menu Editar com opções
menu_editar = tk.Menu(barra_menu, tearoff=0)
menu_editar.add_command(label="Cortar", command=cortar)
menu_editar.add_command(label="Copiar", command=copiar)

# Adicionando os menus à barra de menus
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)
barra_menu.add_cascade(label="Editar", menu=menu_editar)

# Configurando a janela para usar a barra de menus
root.config(menu=barra_menu)

# Iniciando o loop principal
root.mainloop()
