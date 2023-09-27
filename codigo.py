    #Passo a Passo do projeto
    #Passo 1 : Entrar no Sistema da Empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

#pyautogui.click -> clicar com o mouse
#pyautogui.write -> escrever um texto
#pyautogui.press -> Apertar uma tecla   
#pyautogui.hotkey -> atalho (combinação de teclas)

pyautogui.PAUSE = 0.5

# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
#entrar no link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#esperar o site carregar
time.sleep(3)

#Passo 2 : Fazer Login
pyautogui.click(x=-880, y=365)
time.sleep(1)
pyautogui.write("iagocleber@gmail.com") 
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

#Passo 3: importar a base de dados de produtos
# py -m pip install pandas numpy openpyxl
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:

    #Passo 4 : Cadastrar 1 produto
    pyautogui.click(x=-934, y=252)

    codigo = tabela.loc[linha,"codigo"]

    #preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(str("obs"))
    # apertar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")        


    pyautogui.scroll(50000)



#passo 5: Repetir o cadastro para todos os produtosobs