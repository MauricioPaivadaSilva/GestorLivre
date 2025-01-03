# A interface gráfica será dividida em duas partes, uma para a pesquisa e outra para o registro.

# Na pesquisa haverá um campo para a inserção dos termos que condizirão a busca no banco de dados, e esse campo ficara sentralizado, com um botão de pesquisar ao lado.

# No cadastro haverá campos para a inserção dos dados e no final da página haverá um botão de cadastrar. Após cadastrar, uma pop-up deve aparecer dizendo se o cadastro foi concluído e qual o id do documento.

# Importante: Deve haver um seletor de tipo de documento (livro, artigo, revista,...)

import tkinter as tk
from functools import partial

from src.connect import connect
from src.view import view

DARKPURPLE = "#301934"
PURPLE = "#800080"
LIGHTPURPLE = "#D8BFD8"

root = tk.Tk()
root.title("GestorLivre")
root.geometry("1280x720")
root.state('zoomed')
root.configure(bg=DARKPURPLE)

def menu():
    mb = tk.Menu(root)
    mb.add_command(label="Procurar", command=window_find)
    mb.add_command(label="Cadastrar", command=window_register)
    root.config(menu=mb)

def clear():
    for widget in root.winfo_children():
        widget.destroy()

def window_find():
    clear()
    menu()

    up = tk.Frame(root, bg=DARKPURPLE, height=100)
    down = tk.Frame(root, bg=PURPLE)

    up.pack(side=tk.TOP, fill=tk.BOTH, expand=False)
    down.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
    down.grid_columnconfigure(0, weight=1)

    def find():
        # Limpa todos os widgets do frame down for widget in down.
        for widget in down.winfo_children():
            widget.destroy()

        term = arg.get()
        results = connect.find(term=term)
        for i, result in enumerate(results):
            result_button = tk.Button(down, text=f"{result[1]} - {result[2]}", font="Times 14", anchor="w", bg=LIGHTPURPLE, command=partial(view, result=result, theme=LIGHTPURPLE))
            result_button.grid(row=i+1, column=0, padx=10, pady=5, columnspan=2, sticky="w")

    arg = tk.Entry(up, width=40, font="Times 12")
    arg.grid(row=0, column=1, padx=10, pady=10)

    fd = tk.Button(up, text="Buscar", font="Times 12", command=find)
    fd.grid(row=0, column=2, padx=10, pady=10)

def window_register():
    clear()
    menu()

window_find()

root.mainloop()