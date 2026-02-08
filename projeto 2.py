
import pyautogui    
import time 

pyautogui.PAUSE = 0.4
pyautogui.press("win")
pyautogui.write("chome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=849, y=454)
pyautogui.write("rafaelpradofelipe200@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345")
pyautogui.click(x=951,y=627)
time.sleep(3)

import pandas as pd 
tabela = pd.read_csv("produtos.csv")
print(tabela)



pyautogui.click(x= 821, y=344)


for linha in tabela.index:
   
    pyautogui.click(x=755, y=277)
    
    codigo = tabela.loc[linha, "codigo"]
   
    pyautogui.write(str(codigo))
   
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") 
    
    pyautogui.scroll(9000)




