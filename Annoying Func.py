import random 
import pyautogui as pg
import time 
word=('JAHANZAIB')
time.sleep(8)
for i in range(50):
    a=random.choice(word)
    pg.write("you are  "+ word)
    pg.press('enter')
    
    