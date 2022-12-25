import pyautogui as pg 
from time import sleep
sleep(3)
pg.leftClick(819,372)
#the code below will find the coordinate of your current location of mouse .
print(pg.position())



# x= pg.locateCenterOnScreen('laugh.png')
# print(x)
# pg.click(x)
# pg.press('left') 

# x=pg.alert('This displays some text with an OK button.')
# print(x)
# y=pg.confirm('This displays text and has an OK and Cancel button.')
# print(y)
# a=pg.prompt('This lets the user type in a string and press OK.')
# print(a)