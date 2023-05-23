from selenium import webdriver
from selenium.webdriver.common.by import By
from inserir_livros import inserir, limpa


class Magalu:
    def __init__(self):
        self.dados_biblioteca = {
            "apple": "https://www.magazineluiza.com.br/livros/l/li/brand---apple/",
            "galera": "https://www.magazineluiza.com.br/livros/l/li/brand---galera/",
            "record": "https://www.magazineluiza.com.br/livros/l/li/brand---record/",
            "rocco": "https://www.magazineluiza.com.br/livros/l/li/brand---rocco/",
            "compainha": "https://www.magazineluiza.com.br/livros/l/li/brand---companhia-das-letras/",
            "nome": "/html/body/div[1]/div/main/section[4]/div[4]/div/ul/li[&nome&]/a/div[3]/h2",
            "preco": "/html/body/div[1]/div/main/section[4]/div[4]/div/ul/li[$preco$]/a/div[3]/div/div/p[2]"

        }

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        limpa()
        self.pega_apple()
        self.pega_galera()
        self.pega_record()
        self.pega_rocco()
        self.pega_compainha()

    def pega_apple(self):
        self.driver.get(self.dados_biblioteca["apple"])
        try:
            for a in range(1, 11):
                editora = "apple"
                nome = self.driver.find_element(By.XPATH, self.dados_biblioteca["nome"].replace('&nome&', str(a))).text
                preco = self.driver.find_element(By.XPATH,self.dados_biblioteca["preco"].replace('$preco$', str(a))).text.replace("R$", "").replace(",", ".")
                print(preco)
                inserir(editora, nome, preco)
        finally:
            pass

    def pega_galera(self):
        self.driver.get(self.dados_biblioteca["galera"])
        try:
            for b in range(1, 11):
                editora = "galera"
                nome = self.driver.find_element(By.XPATH, self.dados_biblioteca["nome"].replace('&nome&', str(b))).text
                preco = self.driver.find_element(By.XPATH,self.dados_biblioteca["preco"].replace('$preco$', str(b))).text.replace("R$", "").replace(",", ".")
                inserir(editora, nome, preco)
        finally:
            pass

    def pega_record(self):
        self.driver.get(self.dados_biblioteca["record"])
        try:
            for c in range(1, 11):
                editora = "record"
                nome = self.driver.find_element(By.XPATH, self.dados_biblioteca["nome"].replace('&nome&', str(c))).text
                preco = self.driver.find_element(By.XPATH,self.dados_biblioteca["preco"].replace('$preco$', str(c))).text.replace("R$", "").replace(",", ".")
                inserir(editora, nome, preco)

            print('')
        finally:
            pass

    def pega_rocco(self):
        self.driver.get(self.dados_biblioteca["rocco"])
        try:
            for d in range(1, 11):
                editora = "rocco"
                nome = self.driver.find_element(By.XPATH, self.dados_biblioteca["nome"].replace('&nome&', str(d))).text
                preco = self.driver.find_element(By.XPATH,self.dados_biblioteca["preco"].replace('$preco$', str(d))).text.replace("R$", "").replace(",", ".")
                inserir(editora, nome, preco)

            print('')
        finally:
            pass

    def pega_compainha(self):
        self.driver.get(self.dados_biblioteca["compainha"])
        try:
            for o in range(1, 11):
                editora = "rocco"
                nome = self.driver.find_element(By.XPATH, self.dados_biblioteca["nome"].replace('&nome&', str(o))).text
                preco = self.driver.find_element(By.XPATH,self.dados_biblioteca["preco"].replace('$preco$', str(o))).text.replace("R$", "").replace(",", ".")
                inserir(editora, nome, preco)
            print('')
        finally:
            pass


Magalu()
