import undetected_chromedriver as uc
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import json
import os
import requests
from selenium.webdriver.common.by import By
os.system("rm -rf rawr")
os.system("cp -r rawrz rawr")
options = uc.ChromeOptions()
a = True
low_word = "abcdefghijklkmnopqrstuvwxyz"
upper_word = "ABDCEFGHIJKLMNOPQRSTUVWXYZ"
number = "1234567890"
symbols = "!@#$%&*"
username_for = low_word
password_for = low_word + upper_word + number + symbols
long_password = 16
long_username = 12
with open("proxy.txt") as f:
    lines = f.readlines()
PROXY = random.choice(lines)
options.add_argument('--no-first-run --no-service-autorun --password-store=basic') #wlacz to jak juz nie bedzie dev test
options.user_data_dir = "rawr"
options.add_argument("--window-size=1920,1080")
options.add_argument('--user-data-dir=rawr')
options.add_argument("--remote-debugging-port=38223")
options.add_argument('--proxy-server=%s' % PROXY)
driver = uc.Chrome(options=options, version_main=105)  # version_main allows to specify your chrome version instead of following chrome global version
driver.set_window_size(1920, 1080)

print("rawr")
print('Current Time:', time.ctime(time.time()))
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
headers = {'Authorization': 'e54a4490de5045589e0c98283821c783'}
time.sleep(5)
def playvideo():
  try:
    if(driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[31]/div[2]/div[1]/button').get_attribute("title")=="Play (k)"):
      driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[31]/div[2]/div[1]/button').click()
  except:
    pass

response = requests.get(
    "https://proxy.webshare.io/api/v2/proxy/ipauthorization/", 
    headers={"Authorization": "	bh0id07r7u2gdme0q7r8v9m8r6pziwocgrgjuscc"}
)
response.json()

time.sleep(3)

print(PROXY)
driver.get('https://bluezczatu.hckrteam.com/link')
time.sleep(1)
    
print(PROXY)
driver.get('https://bluezczatu.hckrteam.com/link')
time.sleep(3)
