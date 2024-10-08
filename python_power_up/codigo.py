# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# instalar pip install PyAutoGUI
#  python.exe -m pip install --upgrade pip

import pyautogui
import time

#pyautogui.writre -> escrever um texto
#pyautogui.press -> apertar uma tecla
#pyautogui.click -> clicar em algum lugar da tela
#pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.3

#abrir o navegador (chrome)

pyautogui.press ('win')
pyautogui.write ('chrome')
pyautogui.press ('enter')

#entrar no link

pyautogui.write ('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press ('enter')
time.sleep (3)

#Passo 2: Fazer login

# selecionar o campo e-mail

pyautogui.click (x=1094, y=557)

#escrever o e-mail

pyautogui.write ('exemplo@gmail.com')

#passando para o próximo campo

pyautogui.press ('tab')

#escrever senha

pyautogui.write ('aleatoria')

#clique no botão login

pyautogui.click (x=1077, y=763)

time.sleep (3)