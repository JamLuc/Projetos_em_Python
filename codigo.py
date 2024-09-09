## Passo 1: entrar no sistema da empresa
    ##https://dlp.hashtagtreinamentos.com/python/intensivao/login
## Passo 2: Fazer login
## Passo 3: Pegar/importar base de dados 
## Passo 4: Cadastrar um produto
## Passo 5: Repetir passo 4 até cadastrar todos os produtos
## pyautogui biblioteca de automacão

## pyautogui.click --- clicar com o mouse
## pyautogui.write --- escrever um texto
## pyautogui.press --- apertar 1 tecla
## pyautogui.scroll ---  rolar a tela para cima ou para baixo

import pyautogui
import time




pyautogui.PAUSE = 0.5
    ## Passo 1: entrar no sistema da empresa
    # abrir o navegador 
    # entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press('win') ## abrindo windows
pyautogui.write('edge') ## digitando nome navegador
pyautogui.press('enter') ## entra no navegador
pyautogui.write("https://osite.com/endereco") # entrar no site
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=743, y=360)
pyautogui.hotkey("ctrl", "a")       
pyautogui.write("seuemail@hotmail.com")
pyautogui.press('tab')
pyautogui.write("senha")
pyautogui.press('tab')
pyautogui.press('enter')


import pandas as pd
tabela = pd.read_csv("nomeDoarquivo.csv")


print(tabela)
for linha in tabela.index: 



    # Cadastrando Produtos
    #codigo
    # Os produtos a seguir são exemplos de como podem ser cadastrados automaticamente.
    pyautogui.click(x=811, y=235)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    #marca
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    #tipo
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)

    #categoria
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    #preco_unitario
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    #custo
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    #obs
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != 'nan':
        pyautogui.write(obs)

    #enviar

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)


