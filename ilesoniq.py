from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import random

import threading

num_threads = 5

def do_request():
        
    while True:
        rand = random.randint(0, 49)
        with open('last_names.txt') as f:
            last_name = f.readlines()[rand].strip('\n')

        rand = random.randint(0, 99)
        with open('first_names.txt') as f:
            first_name = f.readlines()[rand].strip('\n')

        with open('visa.json') as f:
            data = json.load(f)
            random_CC = (data[rand]["CreditCard"]["CardNumber"])

        with open('addresses.json') as f:
            data = json.load(f)
            address = (data[rand]["address"])
            city    = (data[rand]["city"])
            state   = (data[rand]["state"])
            zip     = (data[rand]["zip"])


        url = 'https://strongergateway.com/en_ca/unlock-content-now-validation?chosenOptions%5Bimage%5D=&chosenOptions%5Bimage2x%5D=&lead=63ebdfde5e154'
        driver = webdriver.Chrome()
        driver.get(url)

        time.sleep(0.5)
        cc_name  = driver.find_element(By.ID, 'cardHolder')
        cc_num   = driver.find_element(By.ID, 'cardNumber')
        cc_expM  = driver.find_element(By.ID, 'cardExpireDropdownMonth')
        cc_expY  = driver.find_element(By.ID, 'cardExpireDropdownYear')
        cc_cvv   = driver.find_element(By.ID, 'cardCvv')
        pay_bttn = driver.find_element(By.ID, 'buttonPay')

        rand_month = random.randint(1, 12)
        rand_year  = random.randint(2024, 2028)
        rand_cvv   = random.randint(100, 999)

        cc_name.send_keys(f"{first_name} {last_name}")
        cc_num.send_keys(random_CC)
        cc_expM.send_keys(f"{rand_month:02d}")
        cc_expY.send_keys(f"{rand_year}")
        cc_cvv.send_keys(rand_cvv)
        pay_bttn.click()
        # time.sleep(25)
        driver.close()


threads = []
for i in range(num_threads):
    t= threading.Thread(target=do_request)
    t.daemon = True
    threads.append(t)

for i in range(num_threads):
    threads[i].start()

for i in range(num_threads):
    threads[i].join()