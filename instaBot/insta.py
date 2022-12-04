from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
s =Service("C:/Users/anshs/Downloads/chromedriver_win32/chromedriver.exe")
driver=webdriver.Chrome(service = s)
driver.get("https://www.instagram.com")
time.sleep(3)
username = driver.find_element(By.XPATH,"""//*[@id="loginForm"]/div/div[1]/div/label/input""")
username.send_keys("anshbjp_19")
password = driver.find_element(By.XPATH,"""//*[@id="loginForm"]/div/div[2]/div/label/input""")
password.send_keys("ansh@999")
password.send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element(By.XPATH,"""/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a""").click()
time.sleep(3)
driver.find_element(By.XPATH,"""/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]""").click()
time.sleep(3)
driver.find_element(By.XPATH,"""/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button""").click()
time.sleep(3)
user1 = driver.find_element(By.XPATH,"""/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input""").send_keys("lavish__saxena_75")
time.sleep(3)
driver.find_element(By.XPATH,"""/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]""").click()
time.sleep(3)
driver.find_element(By.XPATH,"""/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button/div""").click()
time.sleep(3)
for i in range(0,5):
    message=driver.find_element(By.XPATH,"""/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea""")
    message.send_keys("Hello")
    message.send_keys(Keys.ENTER)
    time.sleep(3)

time.sleep(180)