# Criar a comunicação com o DB em forma de "API", que ira utilizar as informações mínimas estipuladas em #1.

# A comunicação deve ser feita em duas etapas, esta primeira etapa ficará responsável por registrar as informações no banco de dados.

# Ainda não haverá o banco de dados, apenas será feito o modelo para o registro!

class register:
    def __init__(self, author, title, edition, local, editor, date, tfile):
        self.author = author
        self.title = title
        self.edition = edition
        self.local = local
        self.editor = editor
        self.date = date
        self.tfile = tfile

        self.reg()

    def reg(self):

        title = ""
        subtitle = ""

        reference = ""

        name = self.author.split(" ")
        code = name[len(name) - 1].upper()
        author = name[len(name) - 1].upper() + ","
        for i in name:
            if i != name[len(name) - 1]:
                author = author + " " + i
            else:
                pass
        
        if ":" in self.title:
            name = self.title.split(":")
            title = name[0]
            code = code + "_" + title.split(" ")[0].upper()
            subtitle = name[1]
        else:
            title = self.name

        if self.tfile == "Livro":
            reference = "@book{" + code + self.date + ", author={" + author + "}, title={" + title + "}, subtitle={" + subtitle + "}, year={" + self.date + "}, publisher={" + self.editor + "}, address={" + self.local + "}, edition={" + self.edition + "},}"
        elif self.tfile == "Artigo":
            reference = "@article{" + code + self.date + ", author={" + author + "}, title={" + title + "}, subtitle={" + subtitle + "}, year={" + self.date + "}, publisher={" + self.editor + "}, address={" + self.local + "}, edition={" + self.edition + "},}"
        else:
            reference = "@inproceedings{" + code + self.date + ", author={" + author + "}, title={" + title + "}, subtitle={" + subtitle + "}, year={" + self.date + "}, publisher={" + self.editor + "}, address={" + self.local + "}, edition={" + self.edition + "},}"

        