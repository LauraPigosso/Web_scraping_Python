from tkinter import *
from conexao import conexao, cursor
from tkinter import ttk

from inserir_livros import listar_livros


class Janela():

    def __init__(self):
        self.janela = Tk()
        self.tela()
        self.frames()
        self.botao()
        self.lista_frame2()
        self.Atualizar()
        self.dropdown()
        self.select_list()
        self.janela.mainloop()

    def tela(self):  # cria a tela
        self.janela.title('Magalu')
        self.janela.configure(background='#fdfaf9')
        self.janela.geometry('700x500')
        self.janela.resizable(True, True)
        self.janela.maxsize(width=700, height=500)

    def frames(self):
        self.frame_1 = Frame(self.janela, bg='#7fc8f8')
        self.frame_1.place(relx=0.03, rely=0.10, relwidth=0.94, relheight=0.11)  # Criar cabeçario

        self.frame_2 = Frame(self.janela, bg='#7fc8f8', highlightthickness=0.5, highlightbackground="#9c9a92")
        self.frame_2.place(relx=0.03, rely=0.50, relwidth=0.94, relheight=0.45)  # Criar quadro de mostragem

    # Botão para atualizar
    def botao(self):
        self.btAtualizar = Button(self.frame_1, text="ATUALIZAR", command=self.Atualizar)
        self.btAtualizar.place(relx=0.15, rely=0.28, relwidth=0.3, relheight=0.5)

    # Quadro de mostragem
    def lista_frame2(self):
        self.listaLiv = ttk.Treeview(self.frame_2, height=3, columns=("", "editora", "nome", "preco"))
        self.listaLiv.heading('#0', text='')
        self.listaLiv.heading('#1', text='ID')
        self.listaLiv.heading('#2', text='Editora')
        self.listaLiv.heading('#3', text='Nome')
        self.listaLiv.heading('#4', text='Preço')

        self.listaLiv.column('#0', width=5)
        self.listaLiv.column('#1', width=35)
        self.listaLiv.column('#2', width=188)
        self.listaLiv.column('#3', width=188)
        self.listaLiv.column('#4', width=70)

        self.listaLiv.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        # Barra de Rolagem
        self.scroolLista = Scrollbar(self.frame_2, orient='vertical', bg='#ffe45e')
        self.listaLiv.configure(yscrollcommand=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

    def Atualizar(self):  # atualizar a tabela de mostragem
        from inserir_livros import limpa
        from inserir_livros import listar_livros

    def dropdown(self):  # Faz um menu de escolha de editoras para o usuario

        self.Tipver = StringVar(self.frame_1)
        self.Tipv = ("Apple", "Galera", "Record", "Rocco", "Compainha")
        self.Tipver.set("ESCOLHA UMA EDITORA")
        self.popupMenu = OptionMenu(self.frame_1, self.Tipver, *self.Tipv)
        self.popupMenu.place(relx=0.53, rely=0.28, relwidth=0.3, relheight=0.5)

        


    def select_list(self):
        self.listaLiv.delete(*self.listaLiv.get_children())
        for i in listar_livros():
            self.listaLiv.insert(parent='', index=0, values=i)


Janela()
