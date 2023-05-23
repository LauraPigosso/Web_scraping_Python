from selenium import webdriver
from selenium.webdriver.common.by import By
import mysql.connector


# import mysql.connector


class Web:
    def __init__(self):
        self.dados_legais = {
            "Site": "https://asloterias.com.br/lista-de-resultados-da-mega-sena?ordenacao=sorteio",
            "Sorteados": "/html/body/main/div[2]/div/div/div[1]"
        }

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.dados = []
        self.buscar_dados()
        self.atualizar_tabela()

    def buscar_dados(self):
        self.driver.get(self.dados_legais["Site"])
        faz1 = self.driver.find_element(By.XPATH, self.dados_legais["Sorteados"]).text
        faz2 = faz1.splitlines()

        for i in faz2:
            if i == "":
                pass
            elif i[0].isnumeric():
                lista_separada = i.split(sep=" - ")  # separar
                self.dados.append(lista_separada)

        for l in self.dados:
            if " " in l[2]:
                l[2] = l[2].split()

        for i in self.dados:
            print(i)

    def atualizar_tabela(self):
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="loteria"
        )
        cursor = conexao.cursor()

        cmd = f"TRUNCATE TABLE loterialegal"
        cursor.execute(cmd)
        conexao.commit()

        for a in self.dados:
            comando = f"INSERT INTO loterialegal (id, data, col1, col2, col3, col4, col5, col6) values ('{a[0]}', '{a[1]}', '{a[2][0]}',  '{a[2][1]}', '{a[2][2]}', '{a[2][3]}', '{a[2][4]}',  '{a[2][5]}')"
            cursor.execute(comando)
            conexao.commit()
        cursor.close()
        conexao.close()
        # print(dados)
