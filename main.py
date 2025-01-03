import tkinter as tk
from tkinter import ttk
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

    fontB = "Times 12 bold"
    font = "Times 12"

    options = ["Livro", "Artigo", "Periódico"]

    root.configure(bg=LIGHTPURPLE)

    def vf(): 
        ts = all([titleInfo.get(), authorInfo.get(), editionInfo.get(), editorInfo.get(), localInfo.get(), dateInfo.get(), tpInfo.get()])
        return ts 

    def send():

        if vf() == True:
            connect(authorInfo.get(), titleInfo.get(), editionInfo.get(), localInfo.get(), editorInfo.get(), dateInfo.get(), tpInfo.get())

            verify = connect.find(term=titleInfo.get())
            if (titleInfo.get() == verify[0][1]) and (tpInfo.get() == verify[0][8]):
                popup = tk.Toplevel()
                popup.title("Conluído")
                popup.minsize(500, 200)
                popup.maxsize(500, 200)
                content = tk.Message(popup, text=f"{tpInfo.get()} {titleInfo.get()} cadastrado!\nChamada: {verify[0][0]}", width=450)
                content.pack(pady=10)

                closed = tk.Button(popup, text="Fechar", command=popup.destroy)
                closed.pack(pady=10)
            else:
                popup = tk.Toplevel()
                popup.title("Erro")
                popup.minsize(500, 200)
                popup.maxsize(500, 200)
                content = tk.Message(popup, text=f"{tpInfo.get()} {titleInfo.get()} Não cadastrado!", width=450)
                content.pack(pady=10)

                closed = tk.Button(popup, text="Fechar", command=popup.destroy)
                closed.pack(pady=10)

        else:
            popup = tk.Toplevel()
            popup.title("Erro")
            popup.minsize(300, 100)
            popup.maxsize(300, 100)
            content = tk.Message(popup, text="Por favor, preencha todos os campos.", width=250)
            content.pack(pady=10)
            closed = tk.Button(popup, text="Fechar", command=popup.destroy)
            closed.pack(pady=10)

    title = tk.Label(root, text="Título:", font=font, bg=LIGHTPURPLE)
    title.grid(row=0, column=0, padx=10, pady=5)
    titleInfo = tk.Entry(root, font=font, width=50)
    titleInfo.grid(row=0, column=1, padx=10, pady=5)

    author = tk.Label(root, text="Autor:", font=font, bg=LIGHTPURPLE)
    author.grid(row=1, column=0, padx=10, pady=5)
    authorInfo = tk.Entry(root, font=font, width=50)
    authorInfo.grid(row=1, column=1, padx=10, pady=5)

    edition = tk.Label(root, text="Edição:", font=font, bg=LIGHTPURPLE)
    edition.grid(row=2, column=0, padx=10, pady=5)
    editionInfo = tk.Entry(root, font=font, width=50)
    editionInfo.grid(row=2, column=1, padx=10, pady=5)

    editor = tk.Label(root, text="Editora:", font=font, bg=LIGHTPURPLE)
    editor.grid(row=3, column=0, padx=10, pady=5)
    editorInfo = tk.Entry(root, font=font, width=50)
    editorInfo.grid(row=3, column=1, padx=10, pady=5)

    local = tk.Label(root, text="Local:", font=font, bg=LIGHTPURPLE)
    local.grid(row=4, column=0, padx=10, pady=5)
    localInfo = tk.Entry(root, font=font, width=50)
    localInfo.grid(row=4, column=1, padx=10, pady=5)

    date = tk.Label(root, text="Data:", font=font, bg=LIGHTPURPLE)
    date.grid(row=5, column=0, padx=10, pady=5)
    dateInfo = tk.Entry(root, font=font, width=50)
    dateInfo.grid(row=5, column=1, padx=10, pady=5)

    tp = tk.Label(root, text="Tipo:", font=font, bg=LIGHTPURPLE)
    tp.grid(row=6, column=0, padx=10, pady=5)
    tpInfo = ttk.Combobox(root, values=options)
    tpInfo.grid(row=6, column=1, padx=10, pady=5)

    sendB = tk.Button(root, text="Cadastrar", font=font, command=send)
    sendB.grid(row=7, column=1, padx=10, pady=5)

window_find()

root.mainloop()