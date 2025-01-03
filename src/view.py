import tkinter as tk

class view:
    def __init__(self, result, theme):

        fontB = "Times 12 bold"
        font = "Times 12"

        self.root = tk.Tk()
        self.root.title(result[1])
        self.root.geometry("1200x675")
        self.root.configure(bg=theme)

        self.title = tk.Label(self.root, text="Título:", font=fontB, bg=theme)
        self.title.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.titleInfo = tk.Message(self.root, text=result[1], font=font, anchor="w", width=500, bg=theme)
        self.titleInfo.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.author = tk.Label(self.root, text="Autor:", font=fontB, bg=theme)
        self.author.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.authorInfo = tk.Message(self.root, text=result[2], font=font, anchor="w", width=500, bg=theme)
        self.authorInfo.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.key = tk.Label(self.root, text="Chamada:", font=fontB, bg=theme)
        self.key.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.keyInfo = tk.Message(self.root, text=result[0], font=font, anchor="w", width=500, bg=theme)
        self.keyInfo.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.local = tk.Label(self.root, text="Local:", font=fontB, bg=theme)
        self.local.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.localInfo = tk.Message(self.root, text=result[3], font=font, anchor="w", width=500, bg=theme)
        self.localInfo.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.edition = tk.Label(self.root, text="Edição:", font=fontB, bg=theme)
        self.edition.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.editionInfo = tk.Message(self.root, text=result[4], font=font, anchor="w", width=500, bg=theme)
        self.editionInfo.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        self.editor = tk.Label(self.root, text="Editora:", font=fontB, bg=theme)
        self.editor.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.editorInfo = tk.Message(self.root, text=result[5], font=font, anchor="w", width=500, bg=theme)
        self.editorInfo.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        self.date = tk.Label(self.root, text="Data:", font=fontB, bg=theme)
        self.date.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.dateInfo = tk.Message(self.root, text=result[6], font=font, anchor="w", width=500, bg=theme)
        self.dateInfo.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        self.type = tk.Label(self.root, text="Tipo:", font=fontB, bg=theme)
        self.type.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.typeInfo = tk.Message(self.root, text=result[8], font=font, anchor="w", width=500, bg=theme)
        self.typeInfo.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        name = result[2].split(" ")
        author = name[len(name) - 1].upper() + ","
        for i in name:
            if i != name[len(name) - 1]:
                author += " " + i
            else:
                pass

        comp = ""
        if ":" in result[1]:
            comp = result[1].split(":")
        else:
            comp = result[1]

        self.referenceABNT = tk.Label(self.root, text="Referência ABNT:", font=fontB, bg=theme)
        self.referenceABNT.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.referenceABNTInfo = tk.Text(self.root, font=font, wrap="word", width=60, height=5)
        self.referenceABNTInfo.grid(row=7, column=1, padx=10, pady=5, sticky="w")
        self.referenceABNTInfo.insert(tk.END, f"{author}. ")
        if ":" in result[1]:
            self.referenceABNTInfo.insert(tk.END, comp[0], "bold")
            self.referenceABNTInfo.insert(tk.END, f": {comp[1]}. {result[4]} ed. {result[3]}: {result[5]}, {result[6]}.")
        else:
            self.referenceABNTInfo.insert(tk.END, result[1], "bold")
            self.referenceABNTInfo.insert(tk.END, f". {result[4]} ed. {result[3]}: {result[5]}, {result[6]}.")
        self.referenceABNTInfo.config(state=tk.DISABLED)
        self.referenceABNTInfo.tag_configure("bold", font="Times 12 bold")

        self.referenceTEX = tk.Button(self.root, text="Referência LaTex", font=font, command=lambda:self.copy(result[7]))
        self.referenceTEX.grid(row=8, column=1, padx=10, pady=5, sticky="w")

    def copy(self, reference):
        self.root.clipboard_clear()
        self.root.clipboard_append(reference)
        self.root.update()
        self.referenceTEX.config(text="Copiado!", font="Times 12 bold")

    def iniciar_interface(self):
        self.root.mainloop()