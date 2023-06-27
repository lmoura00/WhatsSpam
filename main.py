from tkinter import messagebox
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import *
import urllib
import time
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


from tkinter.filedialog import *

def arquivo():
    global tabela
    arquivoCaminho = askopenfilename()
    tabela = pd.read_excel(arquivoCaminho)
    arquivoSelect = Label(janela, text=arquivoCaminho, font="arial 15 underline")
    arquivoSelect.place(x=230, y=180)
def enviar():
    global texto
    global numero
    numero = num.get()
    navegador = webdriver.Chrome()
    navegador.get("https://web.whatsapp.com")
    global colunaNum
    # esperar a tela do whatsapp carregar
    while len(navegador.find_elements(By.ID, 'side')) < 1: # -> lista for vazia -> que o elemento não existe ainda
        time.sleep(1)
    time.sleep(5) # só uma garantia

    for linha in tabela.index:
        # enviar uma mensagem para a pessoa
        telefone = tabela.loc[linha, numero]
        texto = text.get().encode("utf-8")
        texto = urllib.parse.quote(texto)

        # enviar a mensagem
        link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"

        navegador.get(link)
        # esperar a tela do whatsapp carregar -> espera um elemento que só existe na tela já carregada aparecer
        while len(navegador.find_elements(By.ID, 'side')) < 1:  # -> lista for vazia -> que o elemento não existe ainda
            time.sleep(1)
        time.sleep(5)  # só uma garantia

        # você tem que verificar se o número é inválido
        if len(navegador.find_elements(By.XPATH, '//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[1]')) < 1:
            # enviar a mensagem
            navegador.find_element(By.XPATH,
                                   '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button/span').click()


            time.sleep(5)
    messagebox.showinfo(title="AVISO", message="As mensagens foram enviadas com sucesso.")
janela = Tk()
janela.title("ENVIAR MENSAGENS")
janela.geometry("800x400")
janela.configure(background="#222")
janela.resizable(False, False)



titulo = Label(janela, text="TESTE DE ENVIO", font="arial 20 underline bold")
titulo.place(x=250, y=1)
botaoProcurar = Button(janela, command=arquivo ,text="PROCURAR ARQUIVO", font="arial 15 underline", fg="#fff", bg="#2f2f2f", borderwidth=1, border=2 )
botaoProcurar.place(x=2, y=180, bordermode="outside")
textMessage = Label(janela, text="MENSAGEM", font="arial 15 underline")
textMessage.place(x=2, y=50)
text = Entry(janela, font="arial 15 underline", width=28)
text.place(x=132, y=50)
text.focus()
numCollum = Label(janela, text="NOME DA COLUNA", font="arial 15 underline")
numCollum.place(x=2, y=80)
num = Entry(janela, font="arial 15 underline")
num.place(x=220, y=80)
botaoEnviar = Button(janela, text="ENVIAR", command=enviar)
botaoEnviar.place(x=2, y=350)





janela.mainloop()
