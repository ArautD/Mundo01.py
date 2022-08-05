"""Desafios
    .Queremos automatizar o BackUp de arquivos do Sistema
    .No nosso exemplo, vamos ter que criar um processo que 
faça o upload de 1 arquivo no Google Drive de formaa automática e rápida"""
import time
import pyautogui

pyautogui.alert("O cod. Vai começar a trabalhar")
pyautogui.PAUSE = 0.5 #Intervalo de 0.5 segundos entre os processos
#Inicio do processo de abertura do navegador
pyautogui.press('winleft')
pyautogui.write('Opera')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write("https://drive.google.com/drive/u/1/folders/15MrMvbG4XaEDpjshH9lmTeA10iSkhbBL")
pyautogui.press("enter")
#Entrar no DeskTOP
pyautogui.hotkey("winleft","d")
#Arquivo in click
pyautogui.moveTo(394, 833)
pyautogui.mouseDown()
pyautogui.moveTo(1129,939)
pyautogui.hotkey("alt", "tab")
time.sleep(1)
pyautogui.mouseUp()



