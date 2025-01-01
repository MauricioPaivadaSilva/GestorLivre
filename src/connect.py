import sqlite3 as db

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
            subtitle = name[1].strip()
        else:
            title = self.title

        if self.tfile == "Livro":
            reference = "@book{" + code + self.date + ", author={" + author + "}, title={" + title + "}, subtitle={" + subtitle + "}, year={" + self.date + "}, publisher={" + self.editor + "}, address={" + self.local + "}, edition={" + self.edition + "},}"
        elif self.tfile == "Artigo":
            reference = "@article{" + code + self.date + ", author={" + author + "}, title={" + title + "}, subtitle={" + subtitle + "}, year={" + self.date + "}, publisher={" + self.editor + "}, address={" + self.local + "}, edition={" + self.edition + "},}"
        else:
            reference = "@inproceedings{" + code + self.date + ", author={" + author + "}, title={" + title + "}, subtitle={" + subtitle + "}, year={" + self.date + "}, publisher={" + self.editor + "}, address={" + self.local + "}, edition={" + self.edition + "},}"
        
        self.save(reference=reference)

    def save(self, reference):
        con = db.connect("data.db")

        cursor = con.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS docs (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            local TEXT NOT NULL,
            edition TEXT,
            editor TEXT NOT NULL,
            date TEXT NOT NULL,
            reference TEXT NOT NULL,
            type TEXT NOT NULL
        )
        ''')

        cursor.execute('''
        INSERT INTO docs (title, author, local, edition, editor, date, reference, type) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.title, self.author, self.local, self.edition, self.editor, self.date, reference, self.tfile))

        con.commit()
        con.close()

    def find(term):
        con = db.connect("data.db")

        cursor = con.cursor()

        cursor.execute('SELECT * FROM docs WHERE title LIKE ? OR author LIKE ?', ('%' + term + '%', '%' + term + '%'))

        result = cursor.fetchall()

        print(result)

        con.close()