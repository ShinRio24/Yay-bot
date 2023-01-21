import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import sys
from os.path import exists
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()

def display(s):
    t = 1
    while exists("exports/yay{}".format(t)): t += 1

    with open('exports/yay{}.txt'.format(t), 'w') as f:
        f.write(s)
    f.close()


def boot():
    try:

        global driver

        try:
            driver.close()
            driver.quit()
        except NameError:
            driver = None

        PATH = 'C:\Program Files (x86)\chromedriver1.exe'


        driver = webdriver.Chrome(PATH)

        time.sleep(2)
        driver.get('https://yay.space/?modalMode=login')
        driver.maximize_window()

        time.sleep(10)

        display("relogin")

        credentials = driver.find_elements(By.CLASS_NAME, "Input")
        credentials[0].send_keys(os.getenv("yay1Email"))
        time.sleep(4)
        credentials[1].send_keys(os.getenv("yay1Pass"))
        time.sleep(2)

        signin = driver.find_elements(By.CLASS_NAME, "Button--icon-login")
        signin[0].click()
        time.sleep(3)
        time.sleep(6)

        while True:
            runmain()
            display("single loop")
    except:
        time.sleep(5)
        boot()

def runmain():
    time.sleep(10)
    driver.get('https://yay.space/timeline')

    time.sleep(20)

    content = driver.find_elements(By.CLASS_NAME, "Heart__path")
    bad = driver.find_elements(By.CLASS_NAME, "Heart__path--liked")

    if content is None:
        display('Not found so restarting')
        time.sleep(5)
        runmain()
    else:
        display(str(len(content))+" "+ str(len(bad)))
        for x in content:
            if x not in  bad:
                try:
                    if x.is_displayed() and x.is_enabled():
                        driver.implicitly_wait(10)
                        try:
                            x.click()
                        except:
                            pass
                        driver.implicitly_wait(1)
                        time.sleep(random.randint(5,25)/10)
                except:
                    pass

        frunmain()

def frunmain():
    time.sleep(10)

    driver.get('https://yay.space/timeline')
    time.sleep(20)

    content = driver.find_elements(By.CLASS_NAME, "Heart__path")
    bad = driver.find_elements(By.CLASS_NAME, "Heart__path--liked")

    if content is None:
        display('Not found so restarting')
        time.sleep(5)
        frunmain()
    else:
        display(str(len(content))+" "+ str(len(bad)))
        if len(bad) == 0:
            display('taking break')
            time.sleep(600)

        else:
            for x in content:
                if x not in bad:
                    try:
                        if x.is_displayed() and x.is_enabled():
                            driver.implicitly_wait(10)
                            try:
                                x.click()
                            except:
                                pass
                            driver.implicitly_wait(1)
                            time.sleep(random.randint(5,25)/10)
                    except:
                        pass

            frunmain()

def runYay():
    print('yaybot main running')
    sys.setrecursionlimit(100000)
    configure()

    while True:
        try:
            boot()
            display("how double boot")
        except:
            pass


if __name__ == '__main__':
    runYay()