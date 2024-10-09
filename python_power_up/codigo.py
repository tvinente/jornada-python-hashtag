# Passo a passo do projeto

# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# instalar pip install PyAutoGUI
# python.exe -m pip install --upgrade pip

import time
import pyautogui
import pandas as pd

# pyautogui.writre -> escrever um texto
# pyautogui.press -> apertar uma tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)

pyautogui.press ('win')
pyautogui.write ('chrome')
pyautogui.press ('enter')

# entrar no link

pyautogui.write ('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press ('enter')
time.sleep (3)

# Passo 2: Fazer login

# selecionar o campo e-mail

pyautogui.click (x=1407, y=421)

# escrever o e-mail

pyautogui.write ('exemplo@gmail.com')

# passando para o próximo campo

pyautogui.press ('tab')

# escrever senha

pyautogui.write ('aleatoria')

# clique no botão login

pyautogui.click (x=1077, y=763)

time.sleep (3)

# Passo 3: Importar a base de produtos para cadastro

#import pandas as pd

tabela = pd.read_csv ('produtos.csv')

print (tabela)

# Passo 4: Cadatrar produto

for linha in tabela.index:
    # cliclar no campo de código

    pyautogui.click (x=1082, y=489)

    # pegar da tabela o valor do campo que a gente quer preencher

    codigo = tabela.loc [linha, 'codigo']

    # preencher o campo

    pyautogui.write (str (codigo))

    # passar para o próximo campo

    pyautogui.press ('tab')

    # preencher o campo

    pyautogui.write (str (tabela.loc[linha, 'marca']))
    pyautogui.press ('tab')
    pyautogui.write (str (tabela.loc[linha, 'tipo']))
    pyautogui.press ('tab')
    pyautogui.write (str (tabela.loc[linha, 'categoria']))
    pyautogui.press ('tab')
    pyautogui.write (str (tabela.loc[linha, 'preco_unitario']))
    pyautogui.press ('tab')
    pyautogui.write (str (tabela.loc[linha, 'custo']))
    pyautogui.press ('tab')

    obs = tabela.loc[linha, 'obs']

    if not pd.isna (obs):
        pyautogui.write (str (tabela.loc[linha, 'obs']))
    pyautogui.press ('tab')

     # cadastra o produto (botao enviar)

    pyautogui.press ('enter')

    # dar scroll de tudo pra cima

    pyautogui.scroll (5000)

    #Passo 5: Repetir o processo de cadastro até o fim