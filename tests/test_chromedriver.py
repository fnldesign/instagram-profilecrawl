import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

# ********************************************** 
# *** Before Start - Instructions to Execute ***
# **********************************************
# A - Execute On Linux Ubuntu on WSL2 
# 1 - Install Required Linux Libs
# apt-get install -y libglib2.0-0=2.50.3-2 \
#    libnss3=2:3.26.2-1.1+deb9u1 \
#    libgconf-2-4=3.2.6-4+b1 \
#    libfontconfig1=2.11.0-6.7+b1
# 2 - Configure Chrome Executable on WSL2 according instruction at https://cloudbytes.dev/snippets/run-selenium-and-chrome-on-wsl2
# 2 - Install selenium dependency
# pip install selenium
# 3 - Download & Unzip appropriate webdriver at https://sites.google.com/chromium.org/driver/home?authuser=0
# e.g. wget https://chromedriver.storage.googleapis.com/103.0.5060.24/chromedriver_linux64.zip
# unzip chromedriver_linux64.zip
# 4 - Change Driver Path on line 27
# 5 - Run Tests
# python ./test_chromedriver.py

# B - Execute On Windows
# TODO: Instruction in progress

logging.basicConfig(level=logging.INFO)
logging.info('Loading ChromeDriver')
driver_options = webdriver.ChromeOptions()
driver_options.add_argument('--headless')
driver = webdriver.Chrome(options=driver_options)  # Optional argument, if not specified will search path. See options at https://peter.sh/experiments/chromium-command-line-switches/
logging.info('Loading ChromeDriver OK')

logging.info('Loading http://www.google.com/')
driver.get('http://www.google.com/')
logging.info('Loading http://www.google.com/ OK')

time.sleep(5) # Let the user actually see something!

logging.info('Sending Query [ChromeDriver] to Google Search')
search_box = driver.find_element(By.NAME, 'q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5) # Let the user actually see something!
logging.info('Sending Query [ChromeDriver] to Google Search OK')

logging.info('Finish Test OK')
driver.quit()