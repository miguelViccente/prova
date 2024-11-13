import tkinter as tk
from tkinter import messagebox

# Função de exemplo para mostrar uma mensagem
def sobre():
    messagebox.showinfo("Sobre", "Este é um exemplo de menu no Tkinter.")

def sair():
    root.quit()

# Criando a janela principal
root = tk.Tk()
root.title("Exemplo de Menu no Tkinter")
root.geometry("400x300")

# Criando a barra de menus
barra_menu = tk.Menu(root)

# Criando o menu "Arquivo"
menu_arquivo = tk.Menu(barra_menu, tearoff=0)  # tearoff=0 evita o "desanexar" do menu
menu_arquivo.add_command(label="Novo", command=lambda: print("Novo arquivo"))
menu_arquivo.add_command(label="Abrir", command=lambda: print("Abrir arquivo"))
menu_arquivo.add_separator()  # Linha separadora
menu_arquivo.add_command(label="Sair", command=sair)

# Criando o menu "Ajuda"
menu_ajuda = tk.Menu(barra_menu, tearoff=0)
menu_ajuda.add_command(label="Sobre", command=sobre)

# Adicionando os menus na barra de menus
barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)
barra_menu.add_cascade(label="Ajuda", menu=menu_ajuda)

# Configurando a janela principal para usar a barra de menus
root.config(menu=barra_menu)

# Iniciando o loop principal do Tkinter
root.mainloop()
