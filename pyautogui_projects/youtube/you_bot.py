import pyautogui as pg
from time import sleep

class youtube:
    def open():
        pg.press("win")
        sleep(1)
        pg.typewrite("cmd")
        sleep(1)
        pg.press("enter")
        sleep(2)
        #opening brave
        pg.typewrite("start brave https://www.youtube.com/")
        sleep(1)
        pg.press("enter")
        sleep(3)
    
    def search():
   